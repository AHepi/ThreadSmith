# S135 The owner's machine: general rules to addition. Results

*Log S135, 3 October 2026, decision S90. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). The design was written and committed before any code (50fcaf5); the machine (9657032, 61baf63) is in `tools/s135_the_owners_machine/`; the numbers below come from one run of `run_all_tests.py`, repeated under a second hash seed with identical results (raw output in the scratchpad, not in git; the summary is in the `.json` beside this file). Nothing in the theory, its formal core, claims or program, any S108 to S134 file, the decisions file, the S61 terms, the S133 or S134 material or `authority/` was written. No outside model, no network, no Avida, no book file opened. The theory is cited from text 107 by line, the formal core by definition id.*

The owner's words (S90): "No. The agent didn't do what I wanted. I wanted a set of general rules that could be run autonomously to recognise objects, understand displacement, understand object permeance, have a general notion of amounts of objects, then represent addition with those rules." The goal (S88): "the goal is to build something that can construct first."

## 0. In short

- **What was built**: a machine of about 2,150 lines of plain Python (standard library; no neural network; no outside model; deterministic from a seed) that lives in a 16 by 16 grid with coloured blobs and a screen, and runs through seeded scenes on its own. It sees only the grid. Four general rules, handed in by us, each a switchable module with its origin logged: **recognise objects, displacement, object permanence, amounts**. Then, from the failures of what those rules let it expect, it **built** a fifth: **"after = before + added - taken away"**, a rule over amounts alone, held as one thing and used for every later scene.
- **The four rules work as written**: 688 of 688 frames counted right; 3,435 straight steps predicted with no false alarm, all 807 turns, bounces and stops flagged, all 52 jumps flagged, all 207 tracks kept on one object; every vanishing, every object that did not come out, and every "different one came out" flagged (40 of 40 each); the amount behind the screen right on every frame (607 of 607) while at most three were behind, and wrong beyond, as designed (tracking holds three).
- **Addition was built by the machine, not handed in, within a class we named.** Its first expectation ("the amount when the screen lifts is the number I am tracking") failed on the second scene with a lift. It held that expectation as the target, computed the errors on its own ledger, and solved for every rule in the declared language (405 sums and differences of held amounts) that repairs them: 10 rivals, then 3, then 2, then one, at the fifth ledger row. Origin logged: BUILT, from the failures at rows 2 and 4.
- **It represents addition by the theory's tests**: on 300 test scenes in new colours and sizes, it expected the right amount on 157 of 157 possible outcomes (124 of them amounts never shown while building, up to 9 + 5 - 4) and flagged 143 of 143 impossible ones (one more, one fewer); one joins one and the screen lifts on one or on three: flagged 10 of 10 each; on two: 0 of 10. Part-level check: one held amount edited and the scene replayed, the rule's answer moved with the world's in 97 of 97.
- **The knock-outs**: permanence switched off, the built rule fails wherever something was already behind the screen (right on 17 of 157 possible outcomes, exactly the 17 that started empty; false alarms on the other 140); the built rule removed, the machine falls back to tracking (right on 30 of 157; 6 of 133 where more than three were ever behind) and is fooled by impossible events (2 + 2 lifting on 3 passes unflagged); a sham removal changed 0 of 300 predictions; restored, 0 of 300 differ from the intact machine.
- **Built, not found, on the present reading, with one caution.** The found way (first fit in a fixed list) took a wrong rule at row 2 ("after = taken away + tracked") and changed with the list's order at 3 ledger rows (up to 10 different rules held at one row across 50 orders); the built way held rivals instead, and its held rules were the same under all 50 orders of rows and amounts at every row. The same ledger without its failed rows leaves two rivals (tracking, and the relation); the failed rows alone leave the relation. **Caution**: the built way's outputs equal those of a filter that keeps every one of the 405 rules that fits (0 rows differ); only the trace (the rule computed from the errors, no list consulted) separates them, which is the theory's own warning (Argument 9) and S133's reading S against reading K.
- **Same final frame**: 50 pairs of scenes of equal length ending in the same frame with different right answers: the machine 100 of 100; tracking alone 18 of 100; with its held amounts wiped at the last frame 0 of 100; any rival reading only the frame count and the final frame at most 16 of 100.
- **By the theory** (section 6): rules 1 to 4 handed in (declared at the machine's boundary; the machine does not represent them by (R)); the addition rule constructed at the machine's own boundary within a class we named (S118's grade 2), on the present reading of a held target and a prepared binding; at a boundary taking in us, built by the same trace, with the class, the repair procedure and the tasks ours. Five witnesses: 1 holds, 2 holds on the core's reading and fails on reply 04's stricter one, 3 holds on the present reading (the caution above), 4 partly, 5 holds. By the owner's word it is **worked out by the machine inside a class its builders named**, if the owner counts that as worked out: S134's question, still open.
- **Cost**: 15.4 CPU-seconds for the whole run; about one CPU-minute for every run of the job together.

## 1. What was built

`tools/s135_the_owners_machine/` (line counts):

| File | Lines | What it does |
|---|---|---|
| `the_world.py` | 461 | the 16 by 16 world, the screen (columns 3 to 12, rows 6 to 15), seeded scenes (walk, pass behind, amounts), the truth log the machine never reads |
| `rule_1_recognise_objects.py` | 70 | rule 1, handed in |
| `rule_2_displacement.py` | 115 | rule 2, handed in |
| `rule_3_object_permanence.py` | 123 | rule 3, handed in (capacity three) |
| `rule_4_amounts.py` | 44 | rule 4, handed in (counts sets, compares two numbers; does not combine amounts) |
| `the_rule_language.py` | 118 | the 405 rules over amounts, handed in; the found way's fixed list |
| `building_addition.py` | 287 | the built way (repair by exact elimination), the found way (first fit), the filter-all way |
| `the_machine.py` | 252 | the machine: sees frames, runs the rules, keeps the ledger, predicts, logs violations, learns; the knock-outs |
| `self_tests.py` | 123 | 20 checks, 20 passed |
| `run_all_tests.py` | 561 | sections (a) to (f) |

**Deviation from the design, found while building**: rule 2's bounded step was 2.5 cells in the design; a diagonal bounce puts an object 2.83 cells from its predicted place, so it was raised to 3 cells (recorded in the rule's file). **Faults caught before the results were taken**: the world's "stays behind" scenes ended before the object's expected way out fell due, and its "vanishes" scenes did not remove the object (both in the world, not the machine; fixed); the built way kept stale rivals when no rule fitted (fixed: it goes back to its first expectation, as the design says); section (b) was seeded with Python's string hash, which changes between processes (fixed: a stable hash; two runs under different hash seeds now agree exactly).

## 2. Every rule and its origin

| Rung | In plain words | Origin |
|---|---|---|
| 1. Recognise objects | a connected region of one colour is one object; the screen's colour is the screen | **HANDED IN** |
| 2. Displacement | an object seen at a new place is the same object moved (same colour, nearest to where it was expected, within 3 cells); its next place is its place plus its last move; a miss is a violation | **HANDED IN** |
| 3. Object permanence | what goes out of sight behind the screen is still there, at its last predicted place, and is expected to come out where its path leads; at most three held one by one; amounts of what is out of sight are kept | **HANDED IN** |
| 4. Amounts | the amount in a region or in a set picked out at one moment is the number of distinct objects in it; amounts are compared as equal, more or fewer | **HANDED IN** |
| The first expectation | after = tracked (rules 3 and 4 in use) | **HANDED IN** |
| The rule language | after = c0 + cB x before + cA x added + cT x taken away + cK x tracked; c's in -1, 0, +1, c0 in -2 to +2; 405 rules | **HANDED IN** (names the class) |
| 5. Represent addition | after = before + added - taken away | **BUILT** by the machine at ledger row 5, from the failures at rows 2 and 4 (built way); **FOUND** at row 3, place 95 of 405, in the control (found way) |

The built rule's origin record, as the machine wrote it: origin BUILT; "assembled by the machine as a repair of its first expectation (after = tracked): the correction computed by exact elimination from the errors of that expectation on every ledger row, one rule left inside the declared language"; failures that drove it: rows 2 and 4; formed at ledger row 5; rows checked 5; the class it was built in: HANDED IN.

## 3. The tests and their numbers

### (a) The four rules alone

| Test | Result |
|---|---|
| Recognise objects: frames with no two of one colour touching | **688 of 688** counted right |
| Frames where two of one colour touch (the declared limit) | 12 of 12 counted as fewer |
| Displacement: straight steps predicted, false alarms | 3,435 steps, **0** false alarms |
| Turns, bounces and stops flagged as violations | **807 of 807** |
| Jumps flagged (vanished in plain sight, appeared from nowhere) | **52 of 52** |
| Tracks that stayed with one object | **207 of 207** |
| Permanence: comes out (no violation expected) | 40 of 40 clean |
| Stays behind (did not come out) | 40 of 40 flagged |
| Vanishes (did not come out; was not there at the lift) | 40 of 40 flagged |
| A different one comes out | 40 of 40 flagged |
| Permanence off: the same four kinds | no expectation, so nothing flagged in any of the 120 scenes with something to flag |
| Amount behind the screen, frame by frame, scenes never more than three behind | **607 of 607** frames right |
| Scenes more than three behind at some time | 660 of 2,426 right (tracking holds three; the difficulty) |
| The same, permanence off | 226 of 607; 83 of 2,426 |
| The same, displacement off | 426 of 607; 664 of 2,426 |

### (b) The amounts tests of the infant studies' kind

Ten repeats each, new colours and sizes; "flagged" is a violation logged (the everyday "surprise"), "right" is that the machine expected the true amount.

| Case | Seen while building | Four rules only | Built | Found |
|---|---|---|---|---|
| one joins one, lifts on **2** (expected) | yes | 0 flagged, 10 right | 0 flagged, 10 right | 0 flagged, 10 right |
| one joins one, lifts on **1** | yes | 10 flagged | 10 flagged | 10 flagged |
| one joins one, lifts on **3** | yes | 10 flagged | 10 flagged | 10 flagged |
| two take away one, lifts on **1** (expected) | no | 0 flagged | 0 flagged | 0 flagged |
| two take away one, lifts on 0 or on 2 | no | 10 and 10 flagged | 10 and 10 | 10 and 10 |
| 2 + 2, lifts on 4 (expected) | yes | **10 flagged (false alarm)**, 0 right | 0 flagged, 10 right | 0 flagged, 10 right |
| 2 + 2, lifts on 3 (impossible) | yes | **0 flagged (fooled)** | 10 flagged | 10 flagged |
| 1 + 3, lifts on 4 / on 3 | yes | 10 false alarms / 0 flagged | 0 / 10 | 0 / 10 |
| 3 + 1 - 1, lifts on 3 / on 2 | yes | 8 false alarms / 0 flagged | 0 / 10 | 0 / 10 |
| 4 + 3, lifts on 7 / 6 / 8 | yes | 10 / 10 / 10 flagged, 0 right | 0 / 10 / 10 | 0 / 10 / 10 |
| 5 + 5, lifts on 10 / 9 / 11 | **no** | 10 / 10 / 10, 0 right | 0 / 10 / 10 | 0 / 10 / 10 |
| 7 + 4, lifts on 11 / 10 / 12 | **no** | 10 / 10 / 10, 0 right | 0 / 10 / 10 | 0 / 10 / 10 |
| 6 + 2 - 3, lifts on 5 / 4 / 6 | **no** | 10 / 10 / 10, 0 right | 0 / 10 / 10 | 0 / 10 / 10 |
| 9 + 5 - 4, lifts on 10 / 9 / 11 | **no** | 10 / 10 / 10, 0 right | 0 / 10 / 10 | 0 / 10 / 10 |

**What this shows.** The infant-sized tests (one joins one; two take away one) are passed by the four handed-in rules alone: tracking individuals is enough, and no addition rule is needed for them. The difference appears only where tracking fails: there the four rules alone raise false alarms on the possible outcome and are fooled by an impossible one that happens to match their wrong count, while the built rule expects the right amount and flags both impossible outcomes, on amounts it never saw.

### (c) The building of addition

**The building schedule** (seed 1350): 120 scenes (58 amounts, 33 pass behind, 29 walk), an honest world. 91 ledger rows, all usable; the first expectation failed on 33 of them.

**The built way, row by row** (the rival sets are the machine's own log):

| Ledger row | Held amounts (before, added, taken away, tracked) | Counted | First expectation | What it changed |
|---|---|---|---|---|
| 1 | 0, 1, 0, 1 | 1 | right | nothing |
| 2 | 2, 2, 1, 2 | 3 | **wrong** (2) | recognized difficulty: repair computed; **10 rivals** (rank 2; free: added, taken away, tracked) |
| 3 | 0, 1, 1, 0 | 0 | right | predicted "undetermined"; rivals narrowed to **3** |
| 4 | 3, 2, 2, 1 | 3 | **wrong** (1) | "undetermined"; rivals **2**: before + added - taken away; before - added + tracked + 1 |
| 5 | 1, 1, 2, 0 | 0 | right | "undetermined"; **one rule left**: after = before + added - taken away (rank 5) |
| 6 to 91 | | | | the built rule right on every row; no further repair |

**The found way on the same ledger**: at row 2 it took "after = taken away + tracked" (place 18 of 405; 10 rules fitted); that rule failed at row 3; it then took "after = before + added - taken away" (place 95; 3 fitted). **The filter-all way**: 10, 3, 2, 1 rules left at rows 2 to 5, the same as the built way.

**Use on 300 test scenes** (seed 2360; before up to 9, added up to 5, taken away up to 4; colours 7 and 8 and sizes never seen while building; a quarter "one more", a quarter "one fewer"):

| Machine | Possible: expected right, no violation | False alarms | Impossible: flagged | Never-seen amounts, possible: right |
|---|---|---|---|---|
| Four rules only | 30 of 157 | 127 | 130 of 143 | 10 of 124 |
| **Built** | **157 of 157** | **0** | **143 of 143** | **124 of 124** |
| Found | 157 of 157 | 0 | 143 of 143 | 124 of 124 |
| Filter all | 157 of 157 | 0 | 143 of 143 | 124 of 124 |

**Part-level what-if check**: 97 scenes, one held amount edited by one (before, added or taken away, up or down) and the scene replayed with the same seed: the built rule's answer moved exactly as the world's did in **97 of 97** (before +1: 17, before -1: 25, added +1: 11, added -1: 10, taken away +1: 20, taken away -1: 14).

**Controls**:

| Control | Result |
|---|---|
| No difficulty: the same schedule with never more than three behind | 72 rows, tracking never failed, **nothing built** (still "after = tracked") |
| Building with permanence off from the start | **nothing built**: of 69 repair attempts, 67 found that no rule in the language fits every row (the "before" amount is lost, so the rows contradict one another), 2 left rivals that the next row emptied |
| The same ledger without its 33 failed rows | **2 rivals left**: after = tracked; after = before + added - taken away (the failures are needed to decide) |
| The 33 failed rows only | **the relation alone** (the failures carry enough to fix it) |

### (d) The knock-outs (the 300 test scenes, learning paused)

| Machine | Possible: right | False alarms | Impossible: flagged | Where before is not zero | Where before is zero |
|---|---|---|---|---|---|
| Intact (built) | 157 of 157 | 0 | 143 of 143 | 140 of 140 | 17 of 17 |
| **Permanence off** | **17 of 157** | **140** | 137 of 143 | **0 of 140** | 17 of 17 |
| **Built rule removed** | **30 of 157** | 127 | **130 of 143** | 16 of 140 | 14 of 17 |
| **Sham removal** (terms reversed and renamed; ten oldest ledger rows deleted) | 157 of 157 | 0 | 143 of 143 | 140 of 140 | 17 of 17 |
| **Restored** | 157 of 157 | 0 | 143 of 143 | 140 of 140 | 17 of 17 |
| Displacement off | 28 of 157 | 129 | 123 of 143 | 23 of 140 | 5 of 17 |
| Permanence off (found rule) | 17 of 157 | 140 | 137 of 143 | 0 of 140 | 17 of 17 |

Scene by scene, the sham changed **0** of 300 predictions and the restored machine differed from the intact one on **0** of 300. With the rule removed, of the 133 possible scenes in which more than three were ever behind, 6 were right; of the 24 in which never more than three were, 24.

### (e) The order-shuffle check (S134)

| Way, and what was shuffled | Rule at the end | Ledger rows at which the held rule differed between orders | Most different rules held at one row |
|---|---|---|---|
| Found way, 50 random orders of the list | the relation, 50 of 50 | **3** | **10** |
| Found way, 50 orders keeping fewest terms first | the relation, 50 of 50 | **2** | **3** |
| Built way, 50 orders of the rows (inside each solve) and of the amounts | the relation, 50 of 50 | **0** | 1 |
| Filter-all way | the relation, 50 of 50 | 0 | 1 |
| The history itself in 50 random orders | built: the relation 50 of 50; found: 50 of 50 | | |

The built way and the filter-all way predicted differently on **0** of 91 rows.

**Reading.** The found way's rule depends on the list's order at exactly the moments the ledger leaves several rules open (rows 2 to 4); the built way's does not, because it never draws from a list: it holds every rule the rows leave open and commits when one is left. On this ledger the found way reaches the same final rule under every order, because by row 5 only one rule fits; the order decides what it holds on the way, and what it would have predicted then. The shuffle does **not** separate the built way from a filter that keeps everything that fits: their outputs are identical. That difference is in the trace alone.

### (f) The same-final-frame check (S134)

50 pairs; each pair the same length (20 frames) and ending in the same frame (the screen down, nothing in the open), with different right answers to "how many are behind the screen"; the group's arrival time varied apart from the answer.

| Answerer | Right, of 100 | Pairs with both right |
|---|---|---|
| **Built** | **100** | **50** |
| Four rules only | 18 | 0 |
| Built, its held amounts wiped at the last frame | 0 (it cannot say) | 0 |
| Any rival reading only the frame count and the final frame | at most 50 by pairs; **at most 16**, since all 100 scenes share one length and one final frame | |
| Concrete rival: the commonest amount in the ledger (0) | 0 | 0 |

## 4. Every test against what was written before building

| Written before building (design section 6) | Result |
|---|---|
| 1. a rule formed only after the old expectation failed, its origin naming those failures | **met** (rows 2 and 4) |
| 2. the same rule under every one of 50 shuffled orders of rows and amounts | **met** (50 of 50; no row differed) |
| 3. without the failed rows the procedure does not reach that rule alone | **met** (two rivals) |
| 4. the control schedule builds nothing | **met** |
| 5. at least 99 per cent of possible outcomes right, at least 99 per cent of impossible ones flagged, on unseen scenes | **met** (157 of 157; 143 of 143) |
| 6. removing it brings back tracking's failures; sham changes nothing; restoring brings it back | **met** (right only where tracking can be, 30 of 157; 0 changes; 0 differences) |
| 7. with permanence off its use fails wherever before is not zero | **met** (0 of 140) |
| 8. same final frame: at least 95 per cent; wiped no more than 50 | **met** (100; 0) |
| Counts against the design: the found way gives the same rule under every shuffle at every step | **not the case**: it differed at 3 rows |

## 5. Five witnesses on the addition rule

S125's check of reply 04, at the machine's own boundary (inside: the machine as run, its rules, ledger and learner; outside: the world, its truth log, the builders) and at one taking in us.

| Witness | At the machine's boundary | At a boundary taking in us | Evidence |
|---|---|---|---|
| **1. An owned subhistory** | **holds**: the building ran inside the machine, ledger rows 2 to 5, logged; the procedure is our contribution (L427: "a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution") | holds | the log in (c) |
| **2. A represented target held in the episode** | **holds on the core's reading** (D12.2 with T': Held, which asks no provenance; S129 K8): the first expectation and the counted amounts were in the ledger before the repair. **Fails on reply 04's stricter reading**: the ledger is kept by routines we wrote, which entered the boundary whole (I200), as S134 found for the bounded constructor | holds: we hold the target (we wrote the world) | ledger rows 1 to 5 before the rule |
| **3. A newly prepared binding** | **holds on the present reading** (S133's reading K; S134 route (b)): the coefficients are computed by elimination from the errors of the first expectation on the machine's own rows; no list is consulted; the result does not move with any order (0 rows differ in 50); the failures did the deciding (without them, two rivals). **Caution**: the same outputs as a filter of all 405 rules (0 rows differ); outputs alone cannot tell them apart (Argument 9), and Prepares is read by hand (I56) | as at the machine's: we did not write the rule; we wrote the class | (e); the controls in (c) |
| **4. A held representation for explanatory use** | **partly**: held as one rule and used for every later prediction (300 scenes); each part answers to an edit of its part (97 of 97, in the spirit of F1); the machine never claims "this is an account", so D13.3's ExplUse is read by hand | the same | (c), (d) |
| **5. More than content-preserving transfer** | **holds**: nothing the machine receives contains the relation; it sees frames of blobs. The world's code is ours and keeps objects in being, from which the relation follows; the machine never reads it (the relay trap closed, S132, S134) | holds | the machine reads `frames` only |

## 6. The verdict on each rung, by the theory

| Rung | At the machine's boundary | At a boundary taking in us | By the owner's word |
|---|---|---|---|
| 1 to 4, and the first expectation | **declared** (handed in): routines written outside and run inside, entering whole (I200); by (R) a declared transport "does not make an occurrence represent anything" (L211), so the machine does not represent these rules; we do | ours: worked out by the builders | **handed in** |
| The rule language, the repair procedure, the capacity of three, the tasks, the world | declared | ours | **handed in** |
| 5, addition, the **built** way | **constructed within a named class** (S118's grade 2: the class of 405 rules named by us; which member, fixed by the world, grade 3), on the present reading of a held target and a prepared binding; a representation by (R) (faithful on every tested case, provenance constructed) | built by the same trace; the class, the procedure and the tasks ours (L201: construction may operate on selected material, here on declared material, S124's Reading 3; L405: a binding newly prepared inside received content is construction of that binding, and the rest keeps its inherited provenance) | **worked out by the machine, inside a class its builders named**, if the owner counts that as worked out (S134's question, open); otherwise **found** |
| 5, addition, the **found** way (the control) | **selected**: a population (405), a history (the ledger), survival (fitting every row) | declared | **found**: evolved knowledge, not worked out |
| 5, the **filter-all** way (the control) | selected (every member drawn and kept if it fits) | declared | found |

**On surprise.** The theory keeps "surprise" for the violation of a selected rule at a case outside its history (L221; D12.7). So the found rule's violations at the impossible events are surprise in the theory's sense; the built rule's are violations (a constructed rule that fails is violated, and that can be a recognized difficulty, Part X); the handed-in rules' are violations of declared rules. The machine's behaviour is the same in all three: it logs the event with its direction. The everyday word, the infant studies' word, is surprise for all of them.

**On explanation.** Under S86 (in the copies only) an explanation must be worked out. Whether the built rule meets (E) on the question "how many when the screen lifts" was not computed by the theory's program; the part-level check is evidence of the part-by-part fidelity (F1) that (E) asks, read by hand. The verdict here is on provenance and representation, not on explanation.

## 7. What the machine cannot do

- It did not build the rule language, rules 1 to 4, the first expectation, the capacity of three that makes tracking fail, the tasks, the world, or the choice of which amounts to record and when. The class it built in contains the answer: that is the naming trap in plain view.
- It cannot combine two groups added in one scene (rule 4 counts sets; such a row is not usable), cannot count two touching objects of one colour as two, does not estimate large amounts, and cannot build anything outside the 405 rules (no doubling, no multiplying).
- It does not find a question (Argument 5): the question, "how many when the screen lifts", is ours.
- After building, learning was paused for the tests; it was not tested whether it would rebuild the rule after a knock-out with learning on.

## 8. What is unsure

- **Built or filtered.** The built way and a filter of all 405 rules give the same outputs at every row. What makes the built way "built" on the present reading is its trace: the rule is computed from the errors of the held expectation, and no list is consulted. If the theory's Prepares (I56) is read by outputs, the built way is an exhaustive filter, so selected; S133's reading S against reading K is not settled by this run, only made exact.
- **Held or represented** (witness 2): as in S134.
- **The owner's line.** Whether a rule a machine works out inside a class its builders named counts as worked out is S134's question, not answered by any run; S90's "No" was read (Claude's reading) as setting the S133 and S134 line aside, not as that answer.
- **How designed the difficulty is.** With a capacity of four or more, or amounts never above three, nothing would be built in this schedule (the control). The difficulty is real for the machine, but we placed it.
- **One world, one building seed.** The ledger decided at row 5 on this seed; other seeds would decide at other rows (not run).
- The 405-rule language is small: a longer right answer (S134's long-form world) was not tried.

## 9. What was done

Read: S85 to S90 with Claude's readings; text 107 (Parts IV, V, X, XI, XV; L175, L177, L201, L211, L221, L405, L427, L429); the formal core after round 4 (D10.1, D12.1 to D12.7, D13.3, D13.8, D14.7, D16.XV); S131 (section 0, item 3); S125's five witnesses (through S134's table); S129 (I200, I201); S118 (the three grades); S126 (through S133's section 3.1); S133 (readings S and K, sections 3.1 and 5); S134 (sections 0, 3, 5, 6); S124 and the S134 material's role readings on infants (object knowledge at three to four months; the record says infants track up to about four items and expect one plus one to make two; no book file opened, nothing quoted); the S133 material's report (what was supplied and found; its design not copied). Wrote: the design (50fcaf5), the machine (9657032, 61baf63), this file and its `.json`, plain file 135, log entries S135. Runs: self-tests 20 of 20; the whole test run 15.4 CPU-seconds, twice, identical; every run under `timeout` and `nice -n 19`; about one CPU-minute in all.
