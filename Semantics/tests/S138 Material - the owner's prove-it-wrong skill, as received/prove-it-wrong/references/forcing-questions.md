# The 13 forcing questions

Ask every question against every claim. Answer each with:
- **covered**, and by which evidence;
- **missing**;
- **does not apply**, and why.

Three rules make the answers useful:
- **Think first, then classify.** For each question, write the strongest concrete way the claim could fail under it in this case, before answering covered, missing or does not apply.
- **Quote it, or it is missing.** Facts taken from the source are quoted word for word. A fact the source does not state is unknown.
- **Live risk only.** A *missing* answer must name what in this case makes it a real risk: a number, a word, a step of the method. A worry that would fit any claim word for word does not go in the ledger. Put it in one line headed "Routine checks", or leave it out.
- **One condition per row.** When two conditions differ, give each its own falsifier, even if they look related. Examples: "vary the tremor" and "remove the tremor entirely"; "same team wrote the test" and "held out from training is not independence". The sharper one is usually the one that matters.
- **Every proposed test must be big enough to settle it.** Say whether the test, at its planned size, could tell the claim from its rival. Use the base rate or effect size the case gives. A rerun too small to show a difference is not a falsifier.
- **Cannot tell means missing.** If you cannot find out whether a condition was tested, answer *missing*. The falsifier is then "obtain the dated plan, the raw log, or who ran it".
- **"Does not apply" must use the question's own exemption,** given at the end of each entry below, in terms of this case. Where an exemption says "never", it cannot be used.

Each entry gives:
- **Ask**: the question in a form you can put to yourself or to the claimant;
- **Catches**: what kind of missing condition it finds;
- **Test**: what the falsifying test looks like;
- **Missed in**: a real case where it went unasked, and what that cost;
- **Does not apply when**: when you may answer *does not apply*.

The source of each question in Claude Fable Semantics is given in `semantics-audit.md`.

---

## Q1. Scope

- **Ask:**
  - "Which conditions, operating points and time spans could the world present that were not in the tests: longer use, later effects, other loads, speeds, temperatures, seasons?"
  - "Which of those does the claim still cover?"
  - "Was each exclusion stated before the results, or only now?"
- **Catches:** guarantees that hold only inside a supplied list of models, a training range or a lab setting, stated as if they held everywhere. Also silent narrowing.
- **Also catches:** an audit, scan or review whose scope covered documents or a sample, not the practice itself. Example: a compliance audit that read the written policy, not the actual records.
- **Test:** cases chosen to lie just outside the tested range.
  - For a guarantee: cases where the stated premise fails, to see whether the system notices ("unknown", a refusal, a mismatch) or answers confidently and wrongly.
  - Include cases where the departure is visible in the data the system sees, and cases where it is not.
- **Missed in:** a planner whose exact check "guaranteed" success within its supplied physics models. No scene outside those models was ever tried, so nobody knew whether it would say "yes" and be wrong.
- **Does not apply when:** the claim is explicitly scoped to the tested range and makes no wider promise, including in its title and summary.

## Q2. Supplied answer

- **Ask:**
  - "What did the setup hand in by hand: laws, hypotheses, features, labels, candidate answers, the mapping from words to moments, the test items?"
  - "Could the result follow from what was supplied, with the claimed part doing nothing?"
- **Catches:**
  - a "learned" result whose work was done by supplied structure;
  - a measurement read back from where it was put;
  - an answer already present in the inputs under another name.
- **Test:**
  - Remove or blank the claimed part and keep everything supplied. Does the result survive?
  - Compute what the supplied parts alone predict.
  - Check whether the zero error, or the perfect score, is guaranteed by construction.
- **Missed in:**
  - a "persistent memory" whose two features were exactly momentum and displacement times mass: Newton's law, supplied;
  - a speed estimator scored against the very simulator variable it was computed from.
- **Also catches:**
  - a fix verified by the same instrument that flagged it: a scanner that stops matching a pattern does not show the attack path is closed;
  - look-ahead leakage: a forecast or backtest using data not available at prediction time.
- **Does not apply when:** nothing was supplied beyond raw observations and the claimed part, or the claim credits only the supplied parts.

## Q3. Rivals

- **Ask, first, for rival explanations:**
  - "What else could have produced the same evidence?"
  - "What happened at the same time: a pandemic, a policy, a season, a price change, a launch, a staff change?"
  - "Could the compared groups affect each other? Spillover, shared customers or workers, contamination between arms."
  - "Could the outcome cause the supposed cause (reverse cause), or could both share a cause?"
  - "Were the units selected in a way that produces the result: survivors, volunteers, extremes that drift back?"
- **Ask, second, for rival methods**, when the claim gives credit to a part or method: "What is the simplest rival that uses the same supplied parts but not the claimed one: a plain rule, a fixed formula, no learning, the old version? Was it run under the same conditions?"
- **Catches:**
  - an effect, or a null result, that another cause explains as well;
  - credit given to a learned or new part when a simpler thing would do as well.
- **Write the strongest rival out in full:** two or three sentences on what else happened, by what route it would produce the same evidence, and what it predicts that the claim does not.
- **Test:**
  - For each rival explanation, name the observation that would differ if it were true and the claim false: a group the event did not reach, a period before it, units too far apart to affect each other.
  - Use the untreated units as a control trend: what did comparable units that did not get the change do over the same period?
  - For rival methods, use a ladder, from a "does nothing" rival up to the strongest fair one (see `designing-the-test.md`).
- **Missed in:**
  - a county minimum-wage study with neighbouring counties as controls, over 2019 to 2023. Neither the pandemic nor spillover between neighbours was questioned, because the comparison group and parallel trends were taken to settle it;
  - a benchmark where every rival either learned or used no physics at all, so "learned memory" could not be told from "supplied Newton".
- **Does not apply when:** the claim is a pure measurement with no cause or credit in it (for example, "the archive has 41 million timestamps"). Never for a claim that something caused, improved, prevented or had no effect on something.

## Q4. Same by construction

- **Ask:**
  - "Could any two arms, controls or measures agree simply because of how they were built?"
  - "Is any measure the same as another, counted twice?"
- **Catches:**
  - controls that cannot differ, such as a blanked predictor that reduces to a tie-break rule;
  - two columns that are one measurement, such as total checks and first-try successes when each miss costs exactly one extra check;
  - a null control that is not null.
- **Test:**
  - Work out each arm's behaviour from its definition.
  - Check whether two rows must be identical.
  - Run each detector on its target and on that target's nearest innocent neighbour: a test both pass is measuring something else.
- **Missed in:**
  - five ranking arms where "numbers set to zero" had to order options exactly as "least effort first";
  - a null control in a collision simulation that scored 100%, because collisions amplified a one-micrometre change.
- **Does not apply when:** there is only one arm and one measure.

## Q5. Worst single case

- **Ask:**
  - "Behind 'all', 'never', 'every', 'always', or an average: what is the worst single case, item by item, condition by condition?"
  - "Was the event the claim is about even observed in every case counted?"
- **Catches:**
  - an average that rises while every segment falls, because the mix of segments changed;
  - a minimum taken over summaries instead of items;
  - cases where the event never happened inside the observation window but were counted as support;
  - averages that hide a failing subgroup.
- **Test:**
  - Recompute the claim's statistic per single case.
  - List the cases where the claimed event was not observed (clip ended before it, sensor off, screened). Exclude those from support, and say they are outside the claim.
- **Missed in:** "the pictures never matched in any condition" rested on condition-level summaries. One speed pair met after the last frame at 4 frames per second. There, the two worlds were within the noise floor.
- **Does not apply when:** the claim has no strength word, no average and no rate or score over several cases. Never when any of these is present.

## Q6. Premise match

- **Ask:**
  - "Does the test case meet every premise of the claim it is said to test?"
  - "Besides the factor being compared, what else differs between the two cases: position, timing, load, who wrote what, when?"
- **Catches:**
  - confounds;
  - tests of a nearby but different claim;
  - a fix or removal that changes several things at once.
- **Also catches:** evidence from a different artefact: a different version, build, commit, configuration, seed or data snapshot from the one the claim is about. "Tests pass" on another commit; last version's benchmark quoted in this version's report.
- **Also catches:** expectation effects. The person measuring wants the change to work, and nothing is blinded: a self-experiment, a team scoring its own launch.
- **Test:**
  - Hold everything else equal and vary only the claimed factor. Or vary each other difference on its own and show it does not produce the result.
  - **The knock-out:** remove the proposed mechanism entirely (no tremor, no race, no feature). If the explanation is right, the effect must vanish. Give this its own row.
- **Missed in:**
  - a push-versus-touch test where the learner's own position and press command also differed, which the claim's premise excluded;
  - a cache "root cause" where turning the cache off also changed timing and load.
- **Does not apply when:** the comparison is randomized and nothing but the factor differs by design, and the premise is met as stated.

## Q7. Same question

- **Ask:**
  - "Is the evidence answering the question in the claim?"
  - "Does a good predictor of the outcome also produce it?"
  - "Does matching the outputs show the workings are as claimed?"
- **Catches:**
  - "tells apart" evidence offered for "produces";
  - outputs offered for workings;
  - a score offered for "understands";
  - significance offered for "caused by".
- **Test:**
  - For "produces": change the supposed cause and only it, and watch the effect.
  - For workings: a change that reaches inside, where two routes with the same outputs would come apart.
  - For "understands": cases that need the understanding and lack the surface cues, and cases with the cues but without the understanding.
  - **For a proxy metric** (offline score, automatic metric, surrogate marker): check that it moves with the real outcome it stands for, on the same items.
  - **The mechanism's lever.** If the claim works through an intermediate step, check that the step moved: traffic for an emissions zone, the drug in the blood, emails opened, the cache actually hit. An outcome that moved while its lever did not needs another explanation.
- **Missed in:**
  - a sarcasm score on a team-written set offered as understanding;
  - a before-and-after retention lift with a small p-value offered as caused by an email.
- **Does not apply when:** the claim is only about outputs and says so.

## Q8. Unseen changes

- **Ask:**
  - "For anything fitted, learned, tuned or selected: what kinds of change has it never met?"
  - "What other version would fit the same past equally well but act differently there?"
  - "Was any such change run?"
- **Catches:** a fitted part trusted where its history says nothing:
  - new regimes;
  - a start that is not at rest;
  - contact;
  - real noise instead of simulated;
  - a different population.
- **Test:**
  - Name one alternative that fits the same past and differs on an unseen change.
  - Run that change.
  - If no such alternative exists (the family allows none), say so. Then this question is covered by the family, not by the data.
- **Missed in:** a memory fitted on a start-at-rest world. In a look-alike test it did worse than "stays where it is" once the start was not at rest.
- **Does not apply when:** nothing in the claim was fitted, learned or selected.

## Q9. Draws and size

- **Ask:**
  - "How many independent draws are there: seeds, lesson sets, sites, people, makers?"
  - "Is a repeated run being counted as a replication?"
  - "Could this difference arise by luck at this size?"
- **Catches:**
  - one draw treated as typical;
  - 8 cases with a 3-case difference;
  - non-independent items pooled (672 coordinates from 18 runs);
  - zero events in a sample too small to expect any.
- **Also catches:**
  - a "replication" that reanalyses the same data with the same code;
  - instability under changes that should not matter: the seed, the wording of a prompt, the formatting, the order of items, a retry. A result that moves when these move is smaller than it looks;
  - order effects within a run: warm-up, caching, the first item treated differently.
- **Test:**
  - Rerun across several draws.
  - Count wins and losses case by case.
  - Compute how likely the observed count is by chance.
  - For "zero events", ask how many runs would be needed to expect one.
- **Missed in:**
  - "zero crashes in 20 one-hour runs" for a crash seen about once an hour, where nobody ran the same 20 hours with the cache on;
  - an error figure from one set of five lessons, which varied two-fold across draws in a look-alike test.
- **Does not apply when:** the claim is a proof, or a single worked case with no strength word. Never for a claim of absence or of always (never, none, zero, cannot, always): those need the expected-count calculation.

## Q10. Order of events

- **Ask:**
  - "Were the test, the prediction and the pass mark written down before the results were seen?"
  - "Which analyses were added afterwards?"
  - "Did the metric, the stopping point or the comparison group change along the way?"
- **Catches:**
  - many metrics, subgroups, cut-offs or endpoints examined, with only the winner reported. Ask how many were tried;
  - post-hoc analyses presented as tests;
  - stopping when significant;
  - a metric swapped after a disappointing first look.
- **Test:** repeat the post-hoc analysis as a fresh test, fixed in advance, on new data.
- **Missed in:** a force-wobble analysis that "separated 100%", chosen after the predeclared classifier scored 54%. It was honest only because it was labelled as added afterwards.
- **Does not apply when:** a dated, fingerprinted plan exists and was followed, or the claim is explicitly exploratory.

## Q11. Receipts

- **Ask:**
  - "For every 'checked', 'verified', 'works', 'fixed': what exactly was run, what did it print, and where is the output?"
  - "Who wrote the record?"
  - "Has every check that is claimed actually finished?"
- **Catches:**
  - claims of checks not run, or still running;
  - logs written by the claimant;
  - records rebuilt from the claim;
  - a summary that says "checked" when only part was checked.
- **Test:**
  - Rerun or spot-check from the raw output.
  - Have someone who did not make the claim reproduce one item.
- **Missed in:** a report that said "checked by a third agent: see the note at the end" before that check had run, with no note at the end.
- **Also asks:** has the cited check ever failed on anything? A harness, scorer or scanner that has never caught a planted fault has not shown it can.
- **Does not apply when:** the claim mentions no check, test or verification and asserts no state that needs one. Never when it says works, fixed, passes, safe or verified.

## Q12. Consequences

- **Ask:**
  - "If the claim is true, what else must be true that has not been looked at?"
  - "What does the claimed part decide downstream?"
  - "What does the fix, removal or rollout give up?"
- **Catches:**
  - displacement: the effect pushed elsewhere, such as traffic diverted to roads outside a zone, crime moved to the next district, costs moved to another budget, or failures moved to later;
  - side effects;
  - a ranker said to have no say over answers when it decides which acceptable answer is chosen;
  - a fix that removes a feature;
  - a rollout beyond where the result was observed.
- **Test:**
  - Derive one consequence that rivals do not share, and look for it.
  - List what the change protects and check each still holds.
- **Missed in:**
  - "the memory has no say over any answer", when its ordering decided which workable plan was chosen (88 against 96 total effort);
  - "remove the cache" as a fix, which gives up its speed without showing the cause.
- **Does not apply when:** no action follows from the claim and it implies nothing beyond its own measurement. This is rare; think twice.

## Q13. What is counted

- **Ask:**
  - "Who or what was included in the measurement, and who decided?"
  - "Did the definition, the denominator or the boundary change between the compared cases?"
  - "Would the result survive counting what was left out?"
- **Catches:**
  - **survivors only:** validating a hiring test only on people who were hired; a programme measured only on those who finished;
  - **quiet removal:** hard support tickets passed to humans and dropped from the bot's numbers; dropouts excluded;
  - **a hand-picked sample:** a demo batch for quality control, not the production line;
  - **a narrow boundary:** a carbon figure inside the factory fence only;
  - **a changed definition:** a satisfaction score whose survey wording or audience changed in the same quarter.
- **Test:** recount with the excluded items put back, or with the old definition. Or show the excluded part is too small to matter.
- **Missed in:** a planner benchmark whose error was pooled over 672 coordinates, half of them a still circle that every method predicts perfectly. That made every error look smaller.
- **Does not apply when:** every item in the population was counted, under one fixed definition, and nothing was excluded.

## Reassuring words

Some words in a report sound like validity, and each rules out less than it seems. When the evidence uses one, write what it rules out and what it does not:

| Word | Rules out | Does not rule out |
|---|---|---|
| held out | exact training items in the test | same authors, same style, same period |
| replicated | one lucky run | the same data reanalysed; the same lab's habits |
| randomized | who chose to take part | dropouts that differ by arm; unblinded measurement |
| significant | chance at this sample size | bias in who was compared |
| scanned clean / tests pass | the patterns the tool knows | the paths it does not check |
| audited / QC passed | the items in the audit's scope | practice outside the documents; batches not sampled |
| verified (by an agent) | nothing, until the run and its output are shown | |
| independent | the named overlap | other shared inputs: data, tools, assumptions |

