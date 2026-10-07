# Creative transport: runnable micro-experiment

## Run

Requires Python 3.10 or newer and no external packages.

    python creative_transport_agent.py --out results.json

The script generates candidates from two input terminals and NAND, preserves
behaviorally distinct components, pairs generated components as a sender and
receiver, and tests recovery of messages across a binary channel with unknown
but fixed polarity. It begins with a receiver that sees the current signal
only, and permits one predefined interface change: previous-signal access.

No language model is called by this script. The LLM in the conversation wrote
the experiment; the executed agent is a deterministic symbolic constructor.
The experiment demonstrates synthesis within a small specified language,
not a new-to-the-world protocol or a validated general theory of creativity.

## What was and was not provided

Provided: binary input format; NAND and wiring; previous-state access; clocked
symbols; the message-recovery task; exact finite evaluation; a novelty archive;
and a pilot/reference signal at the start of each transmission.

Not provided to the constructor: XOR, equality, differential coding, a final
sender program, or a final receiver program. NAND composition generated them.
The human experiment designer knew this was a solvable task.

## Actual result

The chosen protocol uses equality at both endpoints. In human-readable form:

    sender(message, previous_sent):
        keep previous_sent when message == 1
        otherwise flip previous_sent

    receiver(previous_received, current_received):
        return 1 if the two levels are equal; otherwise return 0

There are exactly two perfect pairs among all 256 pairs of two-input Boolean
functions. The alternative uses XOR at both endpoints. These are familiar
differential-coding conventions, rediscovered by the bounded constructor.

With the receiver-history input, the best accuracies at composition rounds
0, 1, 2 and 3 were 50%, 62.5%, 62.5%, and 100%. Without history, the best is 50%.
One-endpoint-at-a-time strict improvement stalls at the direct-send/direct-read
pair with 50% accuracy. With no reuse of composite components, the best is 62.5%.

All 4,096 twelve-bit messages, both initial levels, and both fixed polarities
were checked after synthesis: 16,384 transmissions, 196,608 bits, zero errors.
This is exhaustive within that test set, not independent evidence about other
channel models. The local test already covers all eight possible input cases.

Training only on the noninverted channel selects an unmodified direct protocol
that gets 0% on the inverted channel. If polarity is allowed to vary between
adjacent signals, the chosen robust-to-fixed-polarity protocol falls to 50% over
all 16 local cases. Omitting the reference signal gives 50% first-bit accuracy.

## Files

* creative_transport_agent.py: full constructor, task, ablations and tests.
* results.json: exact results, expressions, trajectory and all 256 pair scores.

## Relationship to existing work

This small demonstration is not FunSearch, DreamCoder, or novelty search as
implemented in their papers. Those works supply relevant precedents for
separating generation from evaluation, growing reusable program libraries,
and preserving behavioral diversity, respectively.

FunSearch: https://www.nature.com/articles/s41586-023-06924-6
DreamCoder: https://arxiv.org/abs/2006.08381
Novelty search: https://pubmed.ncbi.nlm.nih.gov/20868264/
Differential encoder: https://www.mathworks.com/help/comm/ref/differentialencoder.html
Differential decoder: https://www.mathworks.com/help/comm/ref/differentialdecoder.html
