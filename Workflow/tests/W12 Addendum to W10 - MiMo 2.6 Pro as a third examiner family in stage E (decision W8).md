# W12 Addendum to W10 - MiMo 2.6 Pro as a third examiner family in stage E (decision W8)

*Frozen 22 September 2026, before the client was built and before any request to the service. Read with plan W10 and its first addendum (decision W7). Numbered W12; W11 is the fix-round addendum.*

## 1. What changes
Stage E gains a third examiner family. Beside the five DeepSeek examiners and Atria (one at a time, decision W7), MiMo 2.6 Pro runs as an examiner armed with the skill, over the same marked results and the same sampled half of the reports, under the same instruction: falsify the marks and the reading, re-mark the sample blind, report disagreement by field. Nothing else in W10 changes: MiMo is not a reader under test in stage C, and no arm is run on it. Whether it becomes a third reader is decided after stages C and D, from what the fields and arms show, in a further addendum if at all.

## 2. Why
The marking plan's first named conflict: the reader and both markers are Claude, and DeepSeek is the only reading not by a Claude model. W10.5 carries the cross-reader claim on one stranger family. A second stranger family that agrees on the same fields, or disagrees on the same fields, is what makes that count worth more than an accident of one family's habits. Given up: nothing of W10; the cost is examiner runs and the client.

## 3. How it is built and what is fixed
- One Opus 5 agent at xhigh, armed with the skill, under the W6 addendum's rule for the web (everything read outside the repository is claimed, quoted with address and date, nothing kept): finds the service's documentation (endpoint, model id, authentication, context, output ceiling, rate limits, tool calling, whether a system message and a prefilled assistant message are supported), writes `rigs/W10 harness/code/clients/mimo_client.py` on the shape of the two existing clients (the same four-value `send` seam; retries with backoff; the request and reply returned whole; a `--dry` flag; the output ceiling at the documented maximum as a parameter; the key read from the environment as `MIMO_API_KEY` at call time only and written to no file; base URL and model id overridable), and adds a section to `clients/README.md` with what it found and what it could not.
- No key is in the environment while it builds. One live request of a few tokens, sent by Claude with the key in the command's environment only, checks the client before stage E, as the DeepSeek key was checked.
- Concurrency: the service's own documented limit, and at most five MiMo examiners at a time as for DeepSeek; token spend not limited below the documented maximum.

## 4. Predictions, as counts that could fail
- **W10.11:** the client dry-runs every request shape stage E needs (a system message with the skill, a user message with the marked results, a structured reply) sending nothing, and one live request returns a reply with the model id named in the documentation. Falsified by either failing; then MiMo does not run in stage E and the results file says so.
- **W10.12:** in stage E, W10.5 is read per examiner family and never summed: MiMo's agreement with the Claude markers on the certified within-step fields over the sampled 48 is reported as its own count against the same 40 of 48. Falsified below 40 for the same reading as W10.5; and if DeepSeek passes and MiMo fails, or the reverse, the results file names the fields on which the two families part, which is the finding.

## 5. Not tested
Nothing about MiMo as a reader. Whether MiMo's reading of file 33's tests is the same reading as DeepSeek's is what stage E measures, not what this addendum assumes.

## 6. Traps
Summing families; running an arm on MiMo without an addendum; a key in a file; reading a fast agreement between two stranger families as the instrument travelling when both were handed the Claude marks in the same prompt.
