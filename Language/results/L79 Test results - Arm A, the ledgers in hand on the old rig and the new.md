# L79 Test results - Arm A, the ledgers in hand on the old rig and the new

Plan: "L79 Test plan - Arm A ..., third version.md", frozen at SHA-256 2e97300690dc39f7 after three premise checks (log L77 to L79); instrument `tools/L79_normalise.py` at ca62f449cef91a3b; not edited since. Built and run 22 September under decision L10 ("pick something and see what happens"). Outputs, all 76 ledgers on both drivers with the instrument's verdict on each pair, in "L79 Arm A outputs" (390 files, manifest inside). Two markings: mine below, and "L79 Second marking - by a fresh agent from the plan and outputs alone.md", made by an agent that saw neither this file nor the record. They agree on every mark.

## What was built (new files beside the old; the old untouched, at their recorded hashes)
| File | From | SHA-256 | Reviewed against its spec |
| --- | --- | --- | --- |
| `rigs/rig 1 - arguments/patched/run_check_2.py` | run_check.py (eff1dee15bebc977) | 9a4b21cf771b1208 | built, reviewed (five deviations), fixed, re-reviewed (four remain, below) |
| `tools/consequences_2.py` | consequences.py (782047f829cf6b39) | d04f6dfd08268ce7 | reviewed clean |
| `tools/sameness_2.py` | sameness.py (9bb0534553397401) | e66a9d314a0227b6 | reviewed clean |
| `authority/L80 The ledger language - complete definition, second version.md` | 38 (5f0f54c2f6af60e5) | ec16e220a433e24a | reviewed (two deviations), fixed, re-reviewed clean |
Each file's header names its source, the D-numbers of its changes and the give-up line for each. Builders and reviewers were fresh Opus agents in a workflow of thirteen; the runner was a fourteenth, and its script is kept with its outputs' summary.

## The marks
| | Expectation, in short | Found | Mark (mine) | Second marker |
| --- | --- | --- | --- | --- |
| A1 regression | every old finding in the new report, same kind, lines, verdict, world; additions of listed kinds only | 76 of 76 "A1 HOLDS"; the second marker re-ran the instrument on all 76 and injected four faults to show it is not vacuous | met | MET |
| A2 sentences | the eight JUMP, NO CONNECTION and CANNOT TELL findings carry a Claim or Plan line with a sentence number equal to the ledger's field | eight of eight; every number equals the ledger's `sentence` field (g 5, s 10; g 5, s 10; p 6, q 6; h 8; b 3) | met | MET |
| A3 the tie | P14: HOLDS, g set aside, tied by h, h's verdict JUMP, NOTE h; P11 and P13 unchanged with no tie block | as predicted, lines 14 to 17 of P14's new report; P11 HOLDS and P13 FAILS with nothing added | met | MET |
| A4 worlds in consequences | no contradiction in T07-B's actual section, a world section under the case's own name; ledger A exactly eight derived | 0 derived on both T07-Bs, sections `nora_story` and `Nora's story`; ledger A 8 derived, the two `depends_on` twins gone | met | MET |
| A5 inside worlds | T10-D a JUMP inside `account_world`; T11-B a NO CONNECTION inside `inspector_world`, DENIED BECAUSE unchanged; T07-B's world empty; T07-D's contradiction in told-world wording, same two lines; outside counts 0 | all as predicted | met | MET |
| A6 F15 and F09 | N18-A gains YOU CLAIM AND DENY THE SAME CAUSE naming lines 3 and 4, keeps Fine.; N18-B nothing; N25-A HOLDS, no tie; N25-B FAILS | all as predicted | met | MET |
| A7 outcomes and gauge | six numbers and two outcome lines | all six numbers right (1, 1, 0, 0, 0; T10-D `not asked, no line of that kind` in the actual block, `asked, 1 found` in the world's); the second marker checked all 1033 outcome values conform | met | MET |
| A8 time | both passes under 10 minutes | 97 s old, 110 s new, 207 s; self-reported by the runner, no independent clock | met | MET |
Eight of eight met. The "against" column fired nowhere.

## What the marks do not say, and the plan did not predict
1. **The plan's spec and its instrument disagreed at two points, and the builder chose the instrument.** D4 orders `  - (none)` under an empty Effect's or Expected's direct lines; the frozen normaliser's pattern does not accept that string outside a world, so a build that printed it would have failed A1. The builder left the label with nothing under it, in nine places across five ledgers (the second marker lists them). D2 orders every finding inside a supposed case indented two spaces; on N25-B the old contradiction's verdict line must reappear unindented for A1, so the builder left it at the margin and the instrument closes that world early, booking its count line and outcomes block outside it. Both were reported by the driver's reviewer and left unresolved because resolving them would have failed A1. A fault of the plan: the mock suite the premise checker built did not contain an empty Effect's list or a supposed world with a contradiction, so the instrument was never tested on those wordings. Lesson L12.
2. **A7 was met by a mechanism D5 does not describe.** D5 says "no line of that kind" is decided by the s(CASP) missing-predicate message. On Ultra's T10-D the actual ledger has no BECAUSE line, but the `.pl` still holds the world's `claim_because` clause (only the `line(because).` fact is removed), so the predicate exists and the query answers "asked, nothing found". The builder reported this, then implemented the reading from the ledger's clauses instead, so that the printed line matches A7. The line is right; the rule in D5 was wrong, and the premise checker had confirmed it on a ledger with no such clause at all. The expectation was met by fitting the mechanism to it, which is the hazard the skill names; it is recorded here rather than hidden.
3. **Two builders each ran one `git status`** by reflex, read-only, and said so. No file outside the named new files and the outputs folder was written; the old hashes were re-verified by the runner.
4. **The two copies of ledger A are not byte-identical**: the gauge's timing figure differs. P14's "must agree with itself" was written without that figure in mind; the instrument ignores it.
5. **consequences_2's header on ledger A does not add up** (9 stated + 8 derived, 19 found): a fact under both `depends` and `depends_on` is counted twice in "found" and once in "derived". And its `depends_on(reading(thermometer), ...) <- lines 11` is a derived fact cited to one line, against the tool's own rule; inherited from the old ten, as P15 records, and untouched by the merge because it has no `depends` twin. Both for the tool's next version.
6. **The count "N findings inside 'x' would not stand if the actual ledger's general lines were available" read 0 on all eleven world sections.** On the four Ultra ledgers 0 was the right answer (P16). On ledger H and P18, the only two with both a world and general lines, it also read 0; nothing in the plan predicted those two, so the count's nonzero case is still unexercised.

## What this run shows
The three picks of L78 are built and do what the plan says on every ledger in hand, without changing any old finding. A reported argument is now tested inside its told world (T10-D's cause claim is a jump on the account's own lines; T11-B's inference does not connect on the inspector's). A what-if says what it leaned on. Findings that name no lines now name their claim line with its sentence. NO FAULT FOUND is gone. The consequences tool respects worlds. None of this says the new reports are better for a reader; that is Arm B's question and the read-back test's.

## Not tested
Arm B: new texts nobody in the loop has seen, two translators, the reader on old and new reports shuffled. Rig 2. The world half of the split. The outside-line count at a nonzero value. Any reader.

## Held for the owner
- Whether to keep the picks (L78) now that they run: all three reversible as new versions.
- The two spec-against-instrument conflicts (item 1): fix D4's empty form and D2's supposed-case layout in the driver's next version, or accept the built readings and amend the plan's successor.
- D5's rule (item 2): the next plan states the mechanism the driver uses.

## Traps
- Reading eight of eight as the language working. Arm A held the translator constant and tested only that the rig change did what it said.
- Reading item 2 as the driver being wrong. The printed line is what the plan meant; the plan's description of how to get it was wrong.
