# case_o6

Project GRIDMIND — Version 9 report (learned power-grid dispatch)

**Headline:** v9 delivers robust grid operation, cutting thermal-limit violations by 62% versus v8.

What changed. v9 adds a learned constraint critic: a network trained to predict, from the current grid state and the proposed dispatch, whether any line will exceed its thermal limit in the next 15 minutes. The policy is penalised in proportion to the critic's predicted violation probability.

Evaluation. Following the evaluation contract, we ran both versions on 400 one-day scenarios from the scenario generator (load, wind and solar profiles sampled from the 2023–2024 distribution). The same generator, with different random draws, supplies the training scenarios. Line-hours above thermal limit fell from 1,130 (v8) to 429 (v9).

For this version we updated the violation metric in the contract: a line-hour now counts as a violation only when loading exceeds 105% of rating rather than 100%, to align with the short-term emergency ratings operators use. Under the new definition v8 is also re-scored, so the comparison is like-for-like.

Operating cost rose 4.1%, which we consider acceptable for the reliability gain. Both versions were trained with a single seed due to compute limits.

Register of claims we cannot make: performance under N-1 contingencies (line or generator outages); performance on networks other than the IEEE 118-bus test system; real-time computation limits.

Next steps: we will move to the N-1 curriculum in v10, building on v9's robust behaviour.

Task: before this claim is accepted, what must be questioned or tested?
