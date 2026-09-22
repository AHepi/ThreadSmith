# L72 Test plan - two translators on the eight texts of plan 37

Written before Astra Ultra's bundle is sent. Not edited afterwards. Handoff: "L72 Handoff - Astra Ultra translates the eight texts of plan 37.md". Worker: Astra Ultra, fresh, no repository, one zip back. The eight texts and their questions come from the other model's corpus (`45 Audit package .../corpus/inputs.jsonl`), the same eight plan 37 sampled: T05-B, T05-D, T07-B, T07-D, T10-B, T10-D, T11-B, T11-D.

## Why this test
Plan 45 compared six translations of texts the other model had already worked on (not blind). L66 compared nothing: it had one translator and a sealed key. This is the first comparison between two translators who never saw each other's work on the same texts: mine of 20 September (log 37, ledgers `ledger_T05B` to `ledger_T11D` in rig 1) and Astra Ultra's, from a bundle with those eight ledgers and the rig's raw log removed. What it measures is the second of the four error sources in decision L4: how much of a ledger is the translator rather than the text. The instrument is `tools/sameness.py`, which compares wording, not meaning, so its "near" and "only one side" buckets are read by hand afterwards.

## What I expect
| | Expectation | Would count against |
| --- | --- | --- |
| E1 shared content | On every one of the eight, at least one line matches in content (the "both" bucket, standing set aside). Over the eight together, at least half of my 21 lines are matched | Any text with no matched line: the two translators read it as different texts |
| E2 standing | Standing differs on at least half of the matched lines, as in L62 (Astra Ultra writes GIVEN where I wrote CLAIMED, or the reverse) | Standing the same on every matched line |
| E3 line counts | Astra Ultra's line count equals mine on at least four of the eight; where they differ, Astra Ultra has the extra line on at least two, and no text differs by more than two lines | Any text differing by three or more lines |
| E4 the bin | On both sides: T05-B's and T05-D's quoted command; T07-D's "with no difference of context or respect"; T11-B's "reason for concluding" phrasing appears as a SINCE line on Astra Ultra's side too, not in the bin | The command written as a line about the gate; T11-B's inference written as BECAUSE |
| E5 the checker | The same kind of report on at least six of eight: T05-B, T05-D, T07-B nothing found; T07-D a contradiction; T10-B cannot tell (the plan's route unstated); T10-D and T11-D a BECAUSE with nothing that makes it (a jump); T11-B a SINCE with no connecting line. Most likely to differ: T10-B (whether the purpose is written as a PLAN line at all) and T11-B (how the denied BECAUSE is written) | Fewer than five the same; or a contradiction on T07-B (the told world not used) |
| E6 consequences | Derived facts 0 on at least six of eight; never more than 2 on any; the T10-D and T11-D BECAUSE lines yield no `produced` fact, because no MAKES or ALWAYS line supports them | A `produced` fact on T10-D or T11-D, which would mean a supporting line was filled in |
| E7 the worker | Astra Ultra returns one zip with all the pieces the handoff lists, a manifest whose hashes match, no file edited after the fact, nothing written about records or repositories, and the eight earlier ledgers not mentioned | A draft that discusses the project's status; any sign it saw the earlier ledgers (Lesson L5's family) |
| E8 the reading by hand | After the program, at most three "near" pairs across the eight need a hand decision, and each is a wording difference with the same meaning (my "the gate is NOT open" against, say, "the gate remained shut") | A near pair where the two lines mean different things and the program called them near |

## Known exposure
The scope file L64, which the handoff asks Astra Ultra to read, names four of the eight texts as examples of kinds of finding (section 3: Nora's story and the note as told worlds; section 4: T07-D beside a contradiction, T10-D beside a jump). So the worker can learn that a told world, a contradiction and a jump are among the kinds the checker reports, and which texts they were seen on, but not a single line of the earlier ledgers. L64 goes in whole rather than cut, because it is the contract the translation is made under. E5 is read with this in mind: agreement on T07-B, T07-D and T10-D counts for less than agreement on the other five.

## What the comparison cannot show
Which translation is right. Two translators agreeing may both be wrong in the same way; the texts' answer keys (plan 37) say what the corpus author intended, not what the text says. Sameness measures spread between translators, not fidelity to the text (L64, section 5 keeps those apart).

## Order of work when the zip returns
1. Manifest hashes; source identity (the texts unchanged); runtime provenance; E7.
2. Reruns of every returned ledger on this machine's rig; reports must match the returned ones.
3. `sameness.py` on each of the eight pairs; then the near and only-one-side buckets read by hand.
4. E1 to E8 marked; "L72 Test results" written; decisions the owner must make listed under PARKED.

## Not tested
Rig 2. Any reader. The other 72 families of the corpus.

## Traps
- Editing this file after the zip is sent.
- Letting the results read Astra Ultra's translation through mine. The program runs first; the hand reads only what it leaves.
- Treating a difference in standing as a difference in content.
