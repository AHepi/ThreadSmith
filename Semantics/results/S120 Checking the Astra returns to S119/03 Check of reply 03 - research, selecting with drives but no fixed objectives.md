# Check of GPT 6 Astra's reply 03: research, selecting with drives but no fixed objectives (log S120)

*Written by Claude (Opus 5.5) on 1 October 2026, decision S74, by the one agent doing the whole S120 job (S56, S68). Reply checked: `tests/S119 Returns from GPT 6 Astra/03 Return - research, selecting with drives but no fixed objectives.md` (kept unchanged), answering `tests/S119 Briefs for GPT 6 Astra/03 Research, checked - selecting with drives but no fixed objectives.md`. Avida source: 2.14.0 at commit 47f13dad, read in a fresh copy in the scratch space. Outside sources were opened on the web on 1 October 2026; where a page could not be read, that is said. In the owner's Avida terms (S61): the **execution environment** is the whole simulated world, and it is the selector under test (S72). No Avida process was run for this check. No GLM check (S70's latest word on GLM).*

## 1. What the reply offers

1. **A table of 16 lines of work** (the brief asked for at least the main ones): novelty search; minimal criterion novelty search; minimal criterion coevolution; POET; Enhanced POET; PAIRED; OMNI; learning progress; compression progress; empowerment; MAP-Elites; host-parasite coevolution in Avida; prediction and anticipation; resource-dependent Avida feedback; fluctuating Avida task environments; POWERPLAY. For each: the selector's "instinct", its memory, the grade of naming, stock or C++, a cost in lines of code, and what would count against it.
2. **One section per line of work**, each with what was read in the source paper (marked "checked", with sections and pages), how it would carry over to an Avida execution environment, and a first cheap test.
3. **Where the literature has nothing:** no selector meeting grade 3 was found, and no Avida execution environment that holds explanatory problems or directs criticism at a part. It says this is a bounded search, not a census.
4. **Shared assumptions** and three changes that would tell the readings apart: remove or freeze the selector's memory; replace adaptive changes with a replay of an earlier schedule; change unused inputs and their order.
5. **Options for Claude** with costs (CPU-hours from the owner's one-CPU-hour rule of thumb), none chosen.
6. **21 references**, all marked "checked"; R20 is the Avida source itself.

It ran no Avida experiment and says so.

## 2. Its Avida source claims (R20), checked against 47f13dad

Paths under `avida-core/source/` unless shown.

| # | Claim | Holds? | Where |
|---|---|---|---|
| 1 | Stock reaction and resource controls are in `actions/EnvironmentActions.cc`. | holds | e.g. `SetReactionValue` registered at line 1731, `IncInflow` at 1729 |
| 2 | Save and load actions are in `actions/SaveLoadActions.cc`. | holds | `LoadPopulation` and `SavePopulation` registered at lines 534-535 |
| 3 | `cPopulation::LoadPopulation` creates programs and calls `SetupInject`, with an approximate merit adjustment for saved execution offsets; it is not an exact checkpoint. | holds | `main/cPopulation.cc` from line 6820: `phenotype.SetupInject(*seq)`, then merit scaled by `gest_time / gest_remain` from the saved `gest_offset` |
| 4 | `CompeteOrganisms` aggregates trial scores and takes no arbitrary novelty score as an event argument. | holds | `actions/PopulationActions.cc`: arguments are `type`, `parents_survive` (and two described but not parsed in the constructor); `cPopulation::CompeteOrganisms` (line 8070) works from per-program trial fitness |
| 5 | A live custom selector could use a new action and `cPopulation::UpdateMerit`; nonpositive merit removes the program. | holds | `main/cPopulation.cc` line 8003: `if (new_merit <= 0) KillOrganism(ctx, cell_id);` |
| 6 | `REQUIRED_TASK`, `REQUIRED_REACTION` and `REQUIRE_SINGLE_REACTION` have stock division checks in `cOrganism.cc`; none implements novelty. | holds | `main/cOrganism.cc` `Divide_CheckViable` (from line 788): lines 793, 832 and 834 read the three settings, and the checks follow |
| 7 | The heads hardware implements `ParasiteInfectHost` as an immediate failure. | holds | `cpu/cHardwareCPU.h` line 302: `bool ParasiteInfectHost(Systematics::UnitPtr) { return false; }` |
| 8 | Stock parasite execution is in `cpu/cHardwareTransSMT.cc`, with a compatible test fixture in `avida-core/tests/parasites_log_injections/config/`. | holds | `cHardwareTransSMT::ParasiteInfectHost` at line 695; the fixture uses `HARDWARE_TYPE 2` and `instset-transsmt.cfg`, with `parasite-smt.org` and `evolved-not.org` |
| 9 | `SetEnvironmentInputs` takes three numbers with restricted, ordered high bytes; it is not a streaming protocol. | holds | `actions/EnvironmentActions.cc` near line 1018: rejects inputs unless the top bytes are 15, 51 and 85 |
| 10 | `cEnvironment::DoProcesses` handles finite resource use; `support/config/misc/environment-9resource.cfg` is a stock example. | holds | file present; `DoProcesses` in `main/cEnvironment.cc` |

**Count: 10 hold, 0 in part, 0 do not hold.**

Claim 7 matters beyond this reply: S118 listed parasites (its row 9) as a stock route to grade 3. At this commit, heads programs cannot be infected; the route needs the separate TransSMT hardware, its own instruction set and ancestor, and none of the project's saved program populations can be reused as hosts.

## 3. Its outside sources, spot-checked

Eight of the 21 sources were opened here. For each, the specific numbers the reply quotes were looked for in the source's own text (PDFs were converted to text in the scratch space; nothing from them is kept in git).

| Ref | Source | What the reply quotes | Found here | Verdict |
|---|---|---|---|---|
| R1 | Lehman and Stanley 2011, *Abandoning Objectives* (author manuscript) | hard maze solved in 39 of 40 runs, 250,000-evaluation budget | "solve the same map in 39 out of 40 runs"; budget of 250,000 evaluations | holds |
| R7 | Zhang, Lehman, Stanley, Clune, *OMNI* (arXiv 2306.01711v3) | AI2-THOR: median 13 tasks over a 0.6 success threshold, interval 11-17, one million steps, ten seeds; finite-task studies 100 million steps, ten seeds | "learns 13 (CI: 11 – 17) tasks"; "1 million time steps and are repeated 10 times"; threshold 0.6; "100 million time steps ... 10 times" | holds |
| R13 | Zaman and others 2014, PLOS Biology | 50 coevolution runs of 500,000 updates; EQU in 17 of 50 against none without parasites; parasites gone in 12; nine logic functions; hosts start with NOT | all five found in the article ("17/50 ... in none that evolved without parasites"; "In 12 runs, the parasites went extinct"; "performs only the NOT function") | holds |
| R14 | Beckmann, McKinley, Ofria 2007, adaptive sleep (author manuscript) | anticipatory sleep in 37 of 50 declining-resource runs; 500 days of 256 updates a year; sixteen reductions; an update about one instruction per program | "arose in 37 out of 50 runs"; "500 days, each of which lasts for 256 time steps (updates)"; 6.25% less each year (so 16 steps to zero); "each organism ... will execute one instruction per update" | holds (the 2,048,000-update figure is the reply's arithmetic, and it is right) |
| R17 | Lalejini and others 2021, Frontiers in Ecology and Evolution | six named functions, one subset rewarded and the other penalized, then reversed; two phases of 200,000 updates; a later condition adds 71 functions | NOT, AND, OR rewarded and NAND, AND-NOT, OR-NOT punished in ENV-A, reversed in ENV-B; "two phases that each lasted for 200,000 updates"; "adding 71 novel Boolean logic functions" | holds |
| R19 | Srivastava, Steunebrink, Schmidhuber 2012, *First Experiments with PowerPlay* (arXiv 1210.8385) | an eight-hour run, 67 new action sequences; 340 tasks including compression tasks | "Within 8 hours ... invented 67 novel action sequences"; "solutions to 340 self-generated tasks were learned. 67 of them were non-compression" | holds |
| R21 | Nahum and others 2017, ECAL (author PDF) | 60 replicates, 100,000 updates; live depletion (negative feedback) raises final fitness; replaying another population's resource history does not; positive feedback does not | 60 replicates; "evolved for 100,000 updates"; NFD better than Fixed (p = 0.0075); Paired Transplant (replayed resource levels) "significantly lower than the NFD runs"; PFD "significantly reduced mean final fitness relative to NFD" | holds |
| R16 | Schossau, Adami, Hintze 2016, Entropy | 10,000 generations, 128 repeats; predictive-information bonuses impeded full solutions | only the arXiv abstract page (1511.07962) was read; it states neuro-correlates can aid search and gives none of these numbers | **exists; numbers unverified here** |

**Seven of eight hold exactly; one is unverified, not contradicted.** The other 13 references were not opened here; their "checked" marks rest on the reply. No reference was found to be invented.

## 4. The grade table against the briefs' definitions

The briefs' grades (shared context, used strictly): **1**, a list of functions, each paid or required; **2**, a class or rule written down; **3**, no checking code computes what counts as a solution, the standard coming from something that itself changes, "such as what the world does next".

- **Every line is graded 2 (or 1 where a named function is paid).** This follows the definitions: in each mechanism some written code still judges novelty, progress, success or admission. Claude agrees with each line.
- **Prediction is graded "1/2 according to score".** The brief's own example of grade 3 is "what the world does next". The reply's reading, and reply 01's, is that when the world's next number comes from a fixed written rule, the equality check plus that rule computes what counts, so the grade does not rise. Claude agrees for a fixed rule. Whether some other source of "what the world does next" (a real outside process, or other evolving programs) would make grade 3 is not settled by any reply; **recorded for the owner, not decided** (it touches S117's open reading).
- **Host-parasite coevolution is graded 2.** S118's plan graded parasites "grade 3 for which function, grade 2 for the class". The two readings do not conflict: Avida's checking code still computes the nine named functions (grade 2 by the strict definition), while which of them pays at a given time is set by evolving parasites. The difference is in emphasis and is noted, not resolved.
- **Cost estimates are planning figures, not measurements**, as the reply says. One can be set against what was actually delivered: the reply puts a live prediction drive at 500 to 1,200 lines of C++; reply 01's working patch for a narrower version (next number only, no delayed forecasts) is 71 added lines.

## 5. What it adds beyond S115's reply 05

S115's reply 05 was research on **measuring** open-ended change (activity statistics, MODES, Channon's measures, the York overviews, POET and Enhanced POET, and Avida work by Lenski, Chow, Walker and Ofria). This reply is research on **selecting**: what a selector can be driven by when no final target is named. Apart from POET and Enhanced POET, its sources do not overlap with reply 05's. What it adds:

1. **Mechanisms of selection without a fixed final target**, each with its written-down part named: novelty and its minimal-criterion forms; coevolving challenges and solvers (MCC, PAIRED); learning progress, compression progress and empowerment; quality-diversity; a model's notion of interest (OMNI); self-set tasks with retention checks (POWERPLAY).
2. **Avida prediction work** (Beckmann 2007; Pontes 2020) and a **negative result** on paying for prediction in a neighbouring platform (Schossau 2016, numbers unverified here). Both bear on reply 01.
3. **A replay control already run in Avida** (Nahum 2017): live depletion helped where a replay of the same resource history did not. This is outside evidence, under a different design, that a selector which responds to its own program population can matter beyond the changes it makes. It is the control reply 02 builds in, and it is a reason to expect reply 02's replay arm to be informative.
4. **Two source facts that change plans:** heads programs cannot be parasitized (S118's parasite route is not a setting); a reload is not a checkpoint (as S114 found).
5. **A plain statement of where nothing was found**: no grade-3 selector and no Avida execution environment that holds problems or directs criticism.

## 6. Strengths and weaknesses

**Strengths.** Every Avida claim checked holds. Seven of eight sources checked hold to the number. It keeps grades strict and says what counts against each translation. It names the controls that would separate a responsive selector from a changing one (freeze memory; replay), which match reply 02's design and Nahum's.

**Weaknesses.** No code and no run, as the brief allowed. Line and CPU costs are estimates from a rule of thumb; the 77-task and 500,000-update costs are not measured. Most options are large (driver of 300 to 3,000 lines, or new C++). Thirteen of the 21 references were not opened here. It cannot by itself say which mechanism would make an execution environment keep finding harder things; it says so.

## 7. Runs it proposes, with costs

All are options; none is run here. CPU-hours are the reply's arithmetic from one CPU-hour per 50,000 updates (nine tasks); real costs with 77 detectors may differ.

| Option | First step | Reply's cost | Needs the owner's word |
|---|---|---|---|
| Novelty, MCNS, MAP-Elites on saved programs | score saved programs; no new run | driver 300-850 lines; small CPU | yes (new code) |
| POET or Enhanced POET | transfers between three worlds | about 18 CPU-hours plus cross-tests | yes |
| PAIRED | two program populations, matched budgets | about 12 CPU-hours | yes |
| Progress, compression, OMNI | replay saved traces with old and new models | about 6 CPU-hours plus model cost | yes |
| Host-parasite (TransSMT setup) | check infection works and lasts | about 60 CPU-hours for 3 seeds × 2 conditions × 500,000 updates, if timing scales | yes |
| Resource feedback, live against replay | stock depletion against a recorded schedule | about 12 CPU-hours; replay needs 150-500 more lines | yes |

Of these, the closest to the owner's question that is cheap is the replay comparison, and reply 02 already supplies it in code (see `02 Check of reply 02`).
