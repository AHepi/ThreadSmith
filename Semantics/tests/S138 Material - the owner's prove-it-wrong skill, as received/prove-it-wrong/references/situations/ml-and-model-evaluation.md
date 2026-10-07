# Machine learning and model evaluation

Use this file for benchmark results, model cards, claims of capability ("understands", "reasons", "generalises"), learned modules inside larger systems, and evaluations run by agents.

## Typical claims

- "Our model understands X: 92% on our benchmark."
- "The learned module beats the old one."
- "It generalises to new tasks."

## Where the falsifiers usually are

- **Q2 Supplied answer: leakage and supplied structure.**
  - Test items close to training items, or written by the same people in the same style.
  - Features that already contain the answer.
  - A hypothesis space or candidate list that leaves only one choice.
- **Q3 Rival: simple baselines.**
  - A keyword or length rule.
  - The majority class.
  - The same pipeline with the learned part replaced by a fixed rule.
  - The previous model on the same data.

  The learned part earns credit only above the best baseline.
- **Q7 Same question: score against capability.** For "understands", build two sets:
  - items that need the capability and lack the surface cues;
  - items with the cues but not needing the capability (innocent neighbours).

  A model that passes the first and is not fooled by the second has shown more than a score.
- **Q8 Unseen changes: distribution shift.** A new source, new authors, a new time period, another language or register. Name the shift the claim must survive, and test it.
- **Q9 Draws and size: seeds, splits and wording.** One training seed, one split, one prompt wording, one order of the answer options. Report the spread across several; a margin smaller than that spread is not a win.
- **Q4 Same by construction: ablations.** A removed part also removes parameters or compute. Compare with a size-matched replacement. Check that two ablation arms are not the same configuration.
- **Q10 Order of events: tuning on the test.** Hyperparameters or prompts chosen while looking at test scores make the test a training set.
- **Q11 Receipts: agent-run evaluations.** An agent's "all tests pass" needs the run output. Rerun a sample independently.
- **Q13 What is counted: the evaluation subset.** Items dropped as "ambiguous" or "malformed", or examples the model refused to answer, are left out of the score. Count them back in, or report them.
- **Q7 Same question: automatic metrics.** An automatic score (exact match, BLEU, COMET, a judge model) is a proxy. Check it against human judgement on a sample.

- **Q11 and Q7: a model grading a model.** A judge model, self-grading, or a judge from the same family may share the system's blind spots. Check it against human judgement on a sample, and on planted wrong answers.

## Mini example

**Claim:** "Removing the attention module dropped accuracy from 81% to 60%, so attention is essential."

**Missing:**
- A size-matched replacement (Q4).
- More than one seed (Q9).
- Was the training schedule retuned for the smaller model (Q6)?

**Next test:** replace attention with a module of the same size, over 3 seeds.
