# S117 The Avida work against the semantics - how it will be lined up, written before mapping

*Written 1 October 2026 by the one Opus 5.5 agent of log S117 (decisions S56, S68: one agent, no subagent, no workflow), and committed before any unit is mapped, any verdict given or anything computed. The job is the owner's S69 ("Ok. Send out a worker to see if and how Avida work lines up with the semantics exactly.") and S70 ("Oh and no need for GLM to review. I can't really make sense of the results you handed me. So I need a relationship mapped so I can see more clearly what doesn't work and why."). There is **no GLM check** of this job (S70). An earlier agent for this job was stopped seconds after it started and wrote nothing. Avida is described in the owner's terms (S61, `records/Semantics - Avida terms, given by the owner.md`); the semantics in its own terms, as its latest text and formal core define them, never redefined to make a match. Nothing in the semantics is changed by this job; any change it suggests is listed for the owner, not applied.*

## 1. What is lined up against what

**The semantics.** The latest text, `tests/107 The semantics, standing alone, after round 4.md` (cited "L" + line), and its maths after round 4, `results/S107 Round 4 - maths after the reading/` (formal core, formal claims with their status after round 4, the model program `model after round 4`, owner questions, parked items, inventions register). Bridges already made: S108 Part A round 2's dependency map and candidate definitions (after the cross-examination), S110's three files after the cross-examination (error correction from constructor theory's perspective; the change map; when something in a creative agent is knowledge). S109 Part B is held (S57): read, not settled.

**The Avida work.** S111 (the three properties measured), S112 (what had to be removed and what it is), S113 (which execution environments learn), S114 (Astra's reply checked; the restart audit), S115 (the eight Astra replies checked), S116 (the routine runs), each in its latest form ("after the cross-examination" and "settled" files where they exist), with plain files 111 to 116, and their raw output in the scratch space (read only).

## 2. The units of the semantics

A **unit** is one thing of the semantics that can line up or not. There are **284**, listed by `tools/s117_list_the_units_of_the_semantics.py` (counted from the files, not by hand):

| kind | count | where |
|---|---|---|
| numbered definitions of the formal core | 118 | D0.1 to D18.2, `formal core, after round 4.md` |
| worked encodings of the formal core | 9 | E1 to E9, the same file, §17 |
| formal claims after round 4 | 142 | FC01 to FC110 with their .newN; status after round 4: 133 hold on all models tried, 2 counterexample found (FC23, FC63), 7 not tested |
| named terms of the text that the formal core does not define | 15 | T01 to T15, below |

The named terms: T01 the constitutive conjecture (L17); the six commitments of Part I, T02 faithfulness without assessors (L67), T03 fallibility without error-as-work (L69), T04 conjecture, criticism, action (L71), T05 recursive scrutiny with operative return (L73), T06 substrate independence with physical conditions (L75), T07 two provenances, not one (L77); T08 creativity lives in construction, selection produces the raw material (L13, grievance 6 at L47); T09 premises taken as given, the costly gamble (L397); T10 an inexplicit representation is not an absent one (L407 to L409); T11 closing an episode is a choice (L429); T12 explanatory barriers (L495); T13 error correction (the word, L397); T14 recognized difficulty (L429); T15 complete and creative critical episodes (L429). The formal core quotes some of these lines but defines none of them.

## 3. The Avida things available

Named here before any unit is mapped, in the owner's terms:

1. **An Avida program** (instruction sequence) and its run on Avida's virtual CPU, in the world or alone in the test CPU (analyze mode).
2. **Instructions**, and three ways of changing them: **instruction change** (a copying mistake), the one-in-twenty added or removed instruction at each split (S114), and **instruction ablation** (an instruction replaced by nop-X, the do-nothing instruction).
3. **The Avida execution environment**: the tasks (9 two-number logic tasks, 77 in all), the rewards, the three input numbers and the fixed order in which they are handed out, resources, and Avida's code that checks a task.
4. **The program population**, **program replication**, **computational selection**, **Avida fitness**, **program ancestry**.
5. **Observed computational behavior**: task performance, viability (functional execution), exact copying, speed.
6. **What S111 to S116 measured**: required and removable instructions; the "circuits" of S112 (the small wiring diagrams the task outputs pass through, with their routes); minimal removal sets (singles, pairs, triples); the environment variants of S112 (instruction meanings changed, input numbers changed, the input channel removed); the six environments of S113 over time; the restart audit (S114); the Astra designs checked in S115 (the two founders of reply 4; the giving choice of reply 2; reply 8's environments); S116's eight-input yardstick, order check, competition and extension.
7. **The people studying Avida**: the owner's decisions, Claude's plans written before running, the runs, the GLM checks and their settlements. This is not Avida; it is kept apart as its own Avida-side thing because some units of the semantics may line up with the work done *about* Avida rather than with Avida itself.

## 4. The four verdicts, and what earns each

For each unit, **a counterpart is named before its conditions are checked**, and every alternative counterpart considered is reported, with why it was not taken; none is silently chosen.

- **LINES UP EXACTLY**: an Avida counterpart plays the same role as the unit, and every condition the unit states holds of it, or fails of it, exactly as the semantics says it should. For a claim (FC, argument): the claim's antecedent is met by the counterpart and its conclusion holds there, computed where it can be, argued from the text where it cannot. For a definition: each clause has a counterpart that meets it.
- **LINES UP IN PART**: a counterpart plays the role, some conditions match and some do not; the result says which.
- **DOES NOT LINE UP**: a counterpart exists (something in Avida in the nearest role), but a condition of the unit is false of it, or its role differs from the unit's.
- **NOTHING IN AVIDA**: nothing in Avida, or in the Avida work, plays the unit's role.

Two marks go with a verdict where they apply. **Computed** (a number from the raw output, from analyze mode, or from a copy of the model program) or **argued** (from the text and the Avida records). **Turns on a reading**: where the verdict changes with a reading the text or the owner has left open, both verdicts are given and the reading is named; none is chosen.

A unit about one of the text's own worked examples (the pole, the balances, the matrices, the two-layer episode) is NOTHING IN AVIDA unless Avida has a case in the same role; such units are kept in their own group so they do not swell the other counts. A unit that is a mathematical property of a definition (for example that "one kind on C" is an equivalence relation) gets the verdict of the definition's counterpart: if the definition lines up exactly, the property holds of the counterpart by proof, and the result says "argued".

**The reverse list.** What the Avida work shows that the semantics has no term for, each with where it was shown. A thing goes on the reverse list only if no unit of the semantics names it; things the semantics names under another word are mapped, not listed.

## 5. How the units will be grouped, so the map stays readable

Fifteen groups, in plain names, in the order of the text (each holds the units whose formal-core section or text lines fall in it; a claim that spans sections goes with its first section unless its subject is plainly another):

1. The frame: what the semantics takes from outside (§0; T01)
2. Things, their parts and their changes (§1, §2)
3. Questions and the changes they ask about (§3)
4. Telling parts apart by how they respond to changes: kinds (§4)
5. When something counts as an account: the test of an explanation (§5, §6)
6. Which parts do the work: routes and critical blocks (§7)
7. Rivals, conflicts, problems and tests (§8, §10)
8. Arguments, criticism and use (§9; T09, T13)
9. Histories, carriers and where a correspondence came from: selected, constructed, declared (§11, §12.1 to §12.4; T07, T08)
10. Standing for something: representation, prediction and surprise (§12.5 to §12.9; T10)
11. Making something new: construction, newness and origin (§13; T11, T14, T15)
12. Repair and created explanation (§14)
13. The physical side: tasks, keeping a capability, ownership (§15; T06)
14. Going on without limit, and the whole structure: recursion, universality, classes, what would rule the semantics out, the dependence order (§16, §18; T02 to T05, T12)
15. The text's own worked examples (§17, E1 to E9, and the claims about them)

The map draws the groups on one side and the Avida things of section 3 on the other; a line is a relation of a group (or a unit) to an Avida thing, or to nothing, marked by its verdict. A group's line carries the verdict most of its units have, with the counts; every unit is listed inside its group with its own verdict.

## 6. What will be computed, and how

All in Avida only, or in a copy of the model program; nothing that copies itself runs on the real machine. Raw output is read, never written; new output goes to the scratch space `s117/`. Scripts are `tools/s117_*.py`, each with a plain note at its top.

- **C1. S112's circuit as an explanation, on the instruction-ablation contract.** S112 offered, for each program and task, a circuit (its routes) as what the task "is". Read as an explanatory candidate (Part V) for the question "does this program still do this task after this one instruction is ablated?", its answer at each ablation is "stops" exactly when the ablated instruction lies on every route. Condition (A) asks that this answer equal the program's at every pair of the contract. From S112's raw single-ablation results and traces (no new Avida runs): for every program and task, at every ablation that leaves the copying, whether the circuit's answer equals Avida's; the share of programs at which (A) holds at every ablation; the failures split into "required but off the circuit" and "on the circuit but not required".
- **C2. Same outputs, different organizations.** From S112's environment variants (raw output): programs whose observed computational behavior is the same in the world's test (one kind on that coarse contract) are grouped, and each group is checked for splitting under a change of what one instruction means (nand read as nor; nand read as and), under other input numbers, and under reordered inputs. A group that splits is an Avida instance of the text's claims that a coarser contract identifies more components and a finer one can separate them (FC04) and that an input-output description does not fix an account (Argument 9, FC101).
- **C3. Underdetermination at changes the population never met (Argument 3).** On the program populations S116 saved at update 50,000 (18 runs), in analyze mode with stock Avida: each distinct instruction sequence is run on the world's numbers in the world's order and in the five other orders, and per program it is recorded whether it copies itself and does NOT. Argument 3's antecedent at an unseen order is met when the population holds both a program that does NOT in the world's order and in that order, and one that does NOT in the world's order and not in that order. Counted per run, weighted by programs.
- **C4. Avida-derived cases in a copy of the model program.** The model program after round 4 is copied to `s117/model_copy/` (the repository's program is not edited) and fed small cases built from what S112 recorded (one-bit values, which is exact for these logic tasks): (MC1) one program, as a single block, as an explanatory candidate for the world's task question: (E) computed; its provenance computed by the model's own Sel and Con under two readings of what its history contains (the environment's code that checks the task counted, or not, as an occurrence that represents the survival condition and the task); and (Suff)'s defeat condition computed for an assessor who holds an argument, not using (E), that the program is not an explanation; (MC2) two programs that both do the task in the world's order and differ at an order the world never gives: fidelity on the history and on a wider contract, and underdetermination (D12.9); (MC3) a program that does the task in two places: routes, contributory and indispensable (D7.2, D7.5); (MC4) an instruction ablation against the semantics' deletion, on a program with an extra read.
- **Existing numbers** from S111 to S116 are cited from their files (latest form) where they already answer a unit's condition; each citation names the file and section.
- **Limits**: every Avida run under `timeout` and `nice -n 19`; at most 3 Avida processes at once; about 2 CPU-hours in all; anything more is recorded as proposed.

## 7. What would count against "the Avida work lines up with the semantics"

- Most units of the groups that are about explanation as such (groups 5 to 12) coming out DOES NOT LINE UP or NOTHING IN AVIDA.
- A unit whose conditions Avida's counterpart meets while its conclusion fails: that would be against the semantics as well as against the line-up (for example, a population that admits a differing survivor at an unseen change while the selected program's value there is fixed by its history, against Argument 3; or a candidate meeting (E) with a provenance not declared that an argument not using (E) rules out as an explanation, against (Suff)).
- A unit whose verdict flips on a reading the text leaves open: that counts against "exactly", whichever way the reading goes, and is reported as such.

And what would count for it: the definitions Avida can instantiate (organizations, contracts, kinds, routes, selection, retained capability) lining up exactly, with the claims about them computed to hold on Avida's data.

## 8. What is not tested

- No new evolutionary runs, no new Avida code, no change to Avida (analyze mode on saved populations only).
- S115's batches 4 to 9 and Astra's new environments (the owner's word is awaited).
- Part B (held, S57) and every question the owner left open: what knowledge is; how "causes itself" is read; S111's open question on resisting change; S112's two readings; whether a capability tied to the world's input order counts as learned; which environment to pursue. Where a unit's verdict touches one of these, the result says so and leaves it open.
- No outside model is called (S70: no GLM; no Atria, Mimo or OpenAI).
- The worked examples of the text are not rebuilt in Avida.

## 9. Departures from this plan

Any departure will be recorded in the results file, section "Departures", with why.
