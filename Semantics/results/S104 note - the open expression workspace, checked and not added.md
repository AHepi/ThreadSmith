# S104 note: the open expression workspace, checked and not added

**Log:** S104 (round 2), 27 September 2026.
**The owner's question** (decision S37): "Do these help? Or did the coding rounds already test this?"
**Material:** `tests/S104 Material - open expression workspace, supplied by the owner, checked and not added/`. It holds the zip (md5 99f7f6df74bbb39666d5309d19c5b21e) and `results1.json` (md5 38e5c603e2b637742445c4a9b0a766ea).
**Who checked:** one Opus 5.5 agent (decision S22: one agent for questions like this). It worked in a copy in the scratchpad with the network cut off. It did not open any round-2 reply and wrote nothing to Semantics/. Claude wrote this note from the agent's report. The text checked against is `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd). Line numbers below are that file's.

## Verdict

**No new case, counterexample or sharper finding.** Everything in the uploads that bears on the theory had already been tested by:
- the creative transport case card (items C01–C14);
- the S104 maths (formal claims FC01–FC110 and the model);
- the external cross-examination items (E01–E22).

So the workspace is not a case in the round-2 reading, and no addendum to the reading rule was written.

## The rerun

- **Tests:** all 35 of the zip's tests pass, in 0.2 seconds. The experiments take 0.5 seconds. The rerun used Python 3.11.15; the bundle was made on 3.13.5.
- **Results files:** the rerun's `results.json`, the zip's `results.json` and `results1.json` are the same bytes.
- **Examples and logs:**
  - All 7 example files match the rerun. The brief had said 6.
  - `experiment_log.txt` matches.
  - `test_log.txt` differs only in elapsed times.
  - All 18 hashes in the manifest match.
- **Earlier rounds' code, rerun for comparison:**
  - FC02, FC07, FC57, FC80 and FC101 hold.
  - FC23, FC77, FC78, FC83 and FC102 give counterexamples.
  - Both results are as committed.
  - `s104_creative_transport.py` gives output md5 62cac6e6…, as committed.

## Section by section

For each section: which sentences of the text it bears on, whether an earlier round already tested it and where, and what it adds.

- **storage.** Bears on L169. Two nodes with equal labels stay two nodes: this is Argument 10's swap (L630, FC103). Adds nothing. Sure.
- **computation.** Bears on L469 and L509. A finite record does not show universality, and the zip's README says so itself. Adds nothing. Sure.
- **interpretation.** Bears on L151 and L253 (two readings of one expression are two questions), and on L21 and L409.
  - A bare expression has nothing in it that could stand for the adder. So the occurrence that represents must include the installed interpreter, and the text allows that.
  - Roles (L109) do not change.
  - Putting direction into the data is the second repair in E04, not a case against FC07.
  - Adds nothing. Fairly sure.
- **construction.** Bears on L195–L201, L405, L427, L574 and L616. This is the same shape as the creative transport case (CT8, C01–C06, inventions I112–I115).
  - The two survivors, "add 1 then ×3" and "×3 then add 3", agree on every integer checked from −1000 to 1000. That is L574, as in C13.
  - The tie is broken by list order, as the creative transport card found.
  - The workspace's "constructor" only fills in the operation-and-constant details the host script supplies. The search and the choice run in the host script. That is I112, C06 and C14 again.
  - Adds nothing. Sure.
- **perception.** Bears on (I1) and (I2) at L329.
  - Images with two lit pixels have 1 or 2 components, so no reader of the count alone meets (A) on both. FC57 already holds on 11,132 models, and (F1) is not needed to catch this.
  - The grayscale input breaks the matched-scope conditions of L353 and L361 (FC64, FC65) and makes a new question (L335), as CT6 did.
  - The zip's "port contract" is a type check, not the text's contract (L141).
  - Adds nothing. Sure.
- **topology.** Bears on L105 (cyclic constraints admitted) and L375 (histories acyclic). Non-circular dependence (L255) is not about cycles in a graph. Adds nothing. Sure.
- **adversarial.** There is no sentence of the text for it to test. Adds nothing.
- **prior_protocol.** `previous_constructor.py` is byte-identical to the creative transport experiment's `creative_transport_agent.py` (md5 777a5078…), so the reuse is confirmed. It picks the same pair. Its 640 bits are a subset of the creative transport card's 196,608. Certain.
- **replaceable_evaluators.** Bears on L119, L39 and L466–L469.
  - Strict and lazy evaluators are one kind until the contract includes a program that does not finish.
  - Not finishing is covered by CT1.
  - The interpreters are written by hand, which is what L199 describes.
  - Whether their provenance is declared, or inherits a constructed one, depends on the author's history, which is not supplied (C01, C03, I114, I118).
  - Adds nothing. Fairly sure.
- **scope.** Adds nothing.
- **README and SOURCES.** Its "transport" is a program stage, not the text's transport. It illustrates E20's "repairable" but does not test it.

## Not tested, and not sure

- The agent encoded nothing on the S104 model. Its readings of interpretation and of the evaluators were done by hand, not computed.
- Take a content with no components, on a contract with only one pair. There, any mapping counts as faithful, so representation rests on provenance alone. That is FC77's shape, and the agent judged it not new.
- The README's design goal, "open expression", has no counterpart in the text.
