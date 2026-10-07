*For the owner: this is the brief for your outside coding agent, to add the repair step to V5 continuation memory (log S137, your yes of S93).*
*Hand it to the agent unchanged, as one file, in the V5 workspace.*

---

# Brief: add a repair step to V5 continuation memory

## 1. Purpose

V5 already recognises when its laws fail: it reports `learned_model_mismatch` or `full_family_contradiction`, and then latches. This increment adds what follows recognition: a repair that the machine builds from its own failure, checks against everything it has seen in the episode, and then uses. The result must show, in V5's own records, that each repair came from the failure that triggered it, rather than being picked from a list.

## 2. New words

- **Repair route**: the new, declared code path added by this increment, beside V5's existing forward route.
- **Repair journal**: the record of the episode's public packets and issued forces that the repair route keeps.
- **Target**: a failed learned law, held as the thing to be repaired.
- **Protected row**: a journal row the target predicted correctly (its predicted support met the observed cover).
- **Miss**: on one journal row, the exact gap, per axis and with its direction, between the target's predicted joint rectangles and the observed cover.
- **Candidate change**: one single change to the target, of a kind listed in section 4.
- **Change point**: the journal index from which a changed setting holds.
- **Rival**: a candidate change whose exact solution set (section 3d) has at least one member.
- **Undetermined**: the repair status while two or more rivals remain.
- **Own probe**: a force program the machine chooses to split its rivals.
- **Commit**: adopting the one remaining rival as a new learned law.
- **Repair status**: a new field beside V5's state, with values `none`, `searching`, `undetermined`, `committed`, `no_repair_in_class`, `resource_stop`.
- **Origin words**: **handed in** (written by the builders), **found** (picked from a list by fit), **built** (computed by the machine from its own failure, within the class the builders supplied).

## 3. What to build

**(a) The repair journal.**
Input: every accepted public packet and every issued force, from index 0.
Output: an append-only journal saved atomically beside the checkpoint, bound to the session's input-lineage hash and source versions, and carried through every save, restore and handoff.
Record: one row per index (index, packet hash, cover, issued force).
Keep V5's history-free continuation contract exactly as it is for the forward route: the forward route reads exactly what it reads now, and its outputs stay byte-identical with the journal on or off. Declare the repair route in the build plan as a new route with its own retained evidence and its own trust contract. The journal is evidence for repair, not a replacement for the carried state.

**(b) Hold the target.**
Trigger: the first change of state to `learned_model_mismatch` or `full_family_contradiction`.
Input: the learned laws that just lost support; the journal.
Output, one target record per failed learned law: its id and parameters; the index where its support ended; its last supported predicted rectangles; its claimed aim (to predict the controlled reference's next observations under the issued forces); its protected rows.
Record: a repair log (append-only, hashed in the gate log); repair status `searching`.

**(c) Blame a part.**
Input: one target; the journal.
Replay the target from index 0 under the journal's forces with V5's exact rational arithmetic, and compute the miss on every row. Then take the candidate changes of section 4 one at a time, and for each compute which misses it can close and which protected rows it would break.
Record: every candidate change tried, with the misses it closes and the protected rows it breaks, including those rejected.

**(d) Build the repair.**
Input: each candidate change that can close every miss and breaks no protected row; the journal.
Solve exactly, from the journal rows, for the set of values of the changed quantity (jointly with the initial position alternatives, and with the change points the rows allow) that fit every row. Gain, bias, beta and a velocity jump enter the predicted positions linearly, so each row gives linear inequalities with exact rational bounds. Retention enters as a power: isolate its roots with exact rationals to a tolerance stated in the build plan, and keep an interval that contains every fitting value. Values off the 648-law grid are allowed; this is how a law outside the family can come out.
Output: one solution set per candidate change; each nonempty set is a rival.
- Exactly one rival: go to (f).
- Two or more: status `undetermined`; record every rival and the splitting observation (the earliest future index and force program at which the rivals' forecast covers become disjoint); go to (e).
- None: status `no_repair_in_class`; keep the latch; record it.
Record: each rival's solution set, exactly, and the journal rows it was solved from.

**(e) Choose a test.**
Input: the rivals.
Generate force programs from a bounded set written in the build plan (for example constant forces on a small grid, within the existing limit of 1 to 16 commands), and choose the one at which the rivals' forecasts disagree most, by a measure written in the build plan before code (for example the number of rival pairs whose predicted covers become disjoint; ties broken by least effort, then by fixed order).
Output: the own probe, recorded with origin **built** and kept apart from any probe written by the builders. In ordinary calls it is a proposal; in the closed-loop test variants (section 5) the evaluator executes it, as the demo executes certified commands.

**(f) Commit and use.**
When exactly one rival remains, adopt it as a new learned law.
Record: repair id; origin **built**; the target; the misses it closed; the protected rows it kept; the kind of change, the part, the change point(s) and the solution set; the journal hash; the index at which it was committed.
Rebuild the carried state by replaying the journal from index 0 under the repaired law, then continue on the forward route as usual. Carry the remaining uncertainty in the solved value exactly, or as a containing set marked as such, so that it can only add possibilities: certificates must hold for every value in the set. Answer questions and plans under V5's conditional certificate, the certificate naming the repaired law. If the repaired law later fails, start a new repair with it as the target.

**(g) Keep the old refusals.**
Until a repair is committed, answers stay unknown and plans select nothing, exactly as now. Keep V5's five state names. A repair lifts a latch only through a recorded latch-lift event: index, previous state, repair id, journal hash. Every lift, including one from `full_family_contradiction`, appears in the repair log.

## 4. The class it builds in

The kinds of change the repair may make are written by the builders. Record this class in the build plan, before code, as **supplied**:
- **K1**: one parameter (gain, retention, a bias component, beta) takes a new value for the whole episode.
- **K2**: a change point t, after which one parameter takes a new value.
- **K3**: a change point t, at which the controlled reference's carried velocity takes a new value (a velocity jump; the hidden kick and hidden stop are of this shape).
One change per repair; exact rational arithmetic throughout. Keep the class fixed for the whole run: if no single change fits, the outcome is `no_repair_in_class`.

A law outside the 648 that comes out of step (d) is built by the machine within this supplied class. Report it that way in the provenance table (section 7), using the three origin words.

## 5. Tests, frozen before any code

Write each scene and its prediction in the build plan and record their SHA-256 fingerprints in the gate log before implementing the repair route, as V5's build plan and added case were. For each, write in advance what counts as success and what counts as failure. Preserve every failure as recorded, as V5's report already does.

- **T0 Regression.** The seven frozen scenes and the added pair: every output up to the first repair event is byte-identical to the accepted results. The existing failed qualification stays as recorded; this increment gets its own gate.
- **T1 Hidden-stop pair.** Attack: the learned laws lose support at 24. Prediction: the committed repair (or, if it ends undetermined, every remaining rival) places the change point inside a window the test author writes before running (a suggested window is 17 to 21: the true stop falls after 16, the first public difference is at 21), with zero velocity after it under the scene's forces, and support containing private truth from the commit on. Closed-loop variant: after the own probe is executed, one rival remains and it is a K3 velocity jump. Identity control: status stays `none` through 31.
- **T2 Hidden kick.** Prediction: a K3 repair with its change point in a window around the kick and a solution set containing the true post-kick velocity; a recorded latch-lift from `full_family_contradiction`; private truth contained after commit.
- **T3 Excited mass2.** The test author reads the scene definition and writes one prediction: either a K1 repair whose solution set contains the true law, or, if the true law differs from the failed learned law in more than one part, `no_repair_in_class`.
- **T4 Held-out hidden changes, at least two** (for example a change of gain at a hidden index, a reversal of bias at a hidden index), each with its prediction, written by someone other than the implementer where possible (the owner, or a session that has seen only V5's report). Seal them: only their fingerprints enter the gate log until the repair route's source is frozen and hashed.
- **T5 Zero-kick control.** No difficulty, so no repair: status `none` throughout, outputs identical to the accepted run.
- **T6 Same final observation, different histories.** At least ten pairs, each pair the same length and ending in the identical public packet, needing different repairs (for example a kick at 6 against a gain change at 6). Prediction: the two repairs differ and each contains its own truth; a rival that answers from the observation count and the final packet alone is right on at most one of each pair; with the journal emptied before the failure, no repair is built.
- **T7 Handoff.** Save and restore at least once before and once after the first failure in T1 and T2: the repair log and committed repair are identical to the uninterrupted run.

## 6. Controls that tell built from found

Run each on the same journals as the built way.

- **C1 The found way.** A fixed list: the 648 family in its existing order, then, for each learned law, K2 and K3 candidates over every change point, with values from a grid written in the build plan (the 648 grid's values for each parameter; velocities on a stated grid). Commit the first entry that fits every journal row; record its place in the list; origin **found**.
- **C2 The filter-all way.** Keep every listed entry that fits; commit when one remains, otherwise undetermined.
- **C3 Order shuffle.** Run the built way and C1 under three different orderings (seeds written in the build plan) of the list, of the journal rows and of the candidate changes tried. The built way's committed repair (kind, part, solution set) must be identical under all three; report C1's outcome per ordering.
- **C4 Failing rows removed.** The same journal cut before the first miss: no repair is built. Also call the solver directly on those rows and record what it returns (expected: several rivals, or the unchanged law).
- **C5 Knock-out, sham, restore.** Remove the committed repair: answers return to unknown and plans to none. Sham: change only the repaired law's label and the stored order of its fields: outputs unchanged apart from the label. Restore: outputs reproduce the original byte for byte.
- **C6 Copy.** Supply the correct repaired law directly as a builder-written law; record it as **handed in**; compare its outputs with the built repair's.

If the built way's outputs equal the filter-all way's on every case, say so plainly in the report: then only the recorded route (the miss computed, the part blamed, the value solved) separates built from found.

## 7. What to report

One table per scene, with:
- the repair committed, or `undetermined` with its rivals and the splitting observation, or `no_repair_in_class`;
- its origin word; the index at which it was committed;
- the misses it closed; the protected rows kept;
- its answers on held-out questions against the evaluator's private truth, with the number of certified answers that were wrong;
- the knock-out, sham and restore outcomes; the order-shuffle outcome;
- the C1, C2 and C6 outcomes beside it;
- the own probe proposed, and in the closed-loop variants what it split;
- resources used (time, peak state size, journal size, solver work);
- every failure, preserved.

Then a summary table across scenes, and a **provenance table**: one row per part of the increment (the journal, the class, the solver, the probe set and measure, the found way's list, each committed repair, each own probe, the held-out cases) with its origin word (handed in, found or built) and the evidence for it. Name every reviewer (person, model or session) and what each saw.

## 8. Limits

- Keep every existing V5 obligation: exact support, conditional certificates, refusal when unsupported, atomic persistence, source binding.
- Write the budget in the build plan before code (time per scene, state and journal limits, maximum rivals and candidate changes), and keep to it.
- When a limit is reached, stop that repair, record `resource_stop` in the repair status, keep answers unknown, and report it as a resource stop.
- Edit only the V5 workspace; keep Pinker and V1 to V4 read-only, as now.
- Write these choices of yours in the build plan before code: how the repaired law's value set is carried; the retention tolerance; the probe set and its measure; the found way's grid; the T1 window and velocity bound; the T3 prediction; which exact replay you use (V5's propagation or the independent ledger's method).

## 9. Why this matters

V5 recognises a failure and stops. The owner's aim is a machine that, at that point, works out a repair from its own failure: it holds the law that failed, finds where and how it missed, computes a change that puts every miss right without breaking what was right, checks it against everything it has seen, chooses a test when it cannot yet decide, and then uses the repair. Matching answers alone leave this open, because a list-picker can reach the same answers. So the records must let a reader see, step by step, that the machine did it: the failure, the miss, the part blamed, the value solved, the rivals kept, the commitment, and the controls beside them.
