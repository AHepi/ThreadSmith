# Plan 45 Part B draft coverage: F11-F15

Written by: OpenAI Codex

Authority used: `38 The ledger language - complete definition.md` and `39 Prompt - translate a text into the ledger language.md`, unchanged. Provenance for every ledger is `OpenAI Codex, under plan 45, from the other model's corpus`. The fixture is translated as the actual ledger: CLAIMED and GIVEN are used; no fixture is moved into a TOLD world.

This is a preparation artifact, not a results file. No rig has been run, no predicted verdict is recorded as observed, and no patch is proposed or applied. The raw `text` field from `part_b_inputs.jsonl` is copied exactly into each translation and JSON file. The supplied `question` is kept here as the frozen assessment question, not turned into a source sentence or ledger commitment.

## Translation choices held fixed before runs

The following choices are held in place by the literal cases and their nearest controls.

| Finding | Frozen question | Forcing or primary case | Near control | Translation cut that must not move after a result |
| --- | --- | --- | --- | --- |
| F11 | How many event occurrences does the source identify? | N29-A | N29-B | N29-A has one happening with a repeated mention; N29-B has two happenings. A repeated sentence is not automatically a second event, and a second event is not collapsed merely because its wording repeats. |
| F12 | What is established when an action changes a dependency but its effect is unknown? | N22-A | N22-B | N22-A records a dependency and a change to its setting, but no direction, result, purpose or SO THAT claim. N22-B records the more specific change stated by its supplied rule. Neither case receives a plan line from its question. |
| F13 | Does storage alone perform the promised analysis? / Has the candidate answered the declared question? | T61-B and T76-B | T61-D and T76-D; T61-I and T76-I are invariant restatements | The source's procedural claims are retained as claims. They are not promoted into proof that a physical check ran or that a neighbouring question was answered. These are manual wording/coverage cases, not checker executions. |
| F14 | May an intransitive happening acquire a fictitious patient? | N30-A | N30-B | N30-A remains the Fact `the bell rang`; no doer or patient is invented. N30-B is a Happening because it supplies Ada and the bell. |
| F15 | Can lack of support hide a direct contradiction? | N18-A | N18-B | Positive and negative causal commitments in N18-A point to the same effect and cause. N18-B has only the negative commitment. Neither receives a productive rule merely because the prose uses “produced”. |

The bin is a catch-all only for content for which 38 has no legal line or for a repeated/metatextual sentence already represented without a second commitment. Its gauge is the per-translation count of source sentences that lose material to the bin.

## Artifact coverage

| Finding | ID | Literal text SHA-256 | Role fixed before run | Translation | Ledger pair | Planned semantic use |
| --- | --- | --- | --- | --- | --- | --- |
| F11 | N29-A | `40f6387dc21fe1c6caaf34bb77b086a5e19da7483641f40cd543da9cca311743` | forcing identity case | `translations/N29-A.md` | `ledgers/ledger_N29A.json/.pl` | Translation evidence only; no checker verdict can establish event identity here. |
| F11 | N29-B | `32db4cf49864c688e0a184a305c37db0b612d90cabbd498fb2c8fa526e4a5afc` | opposite control: two stated pushes | `translations/N29-B.md` | `ledgers/ledger_N29B.json/.pl` | Translation evidence only. |
| F12 | N22-A | `a897c836c326f843603e02ab8ad95937810e533d41b2b238f7323a09663c4c14` | forcing/discrepancy case | `translations/N22-A.md` | `ledgers/ledger_N22A.json/.pl` | Patched and frozen rig 1, plus direct diagnostics; no plan verdict may be claimed because there is no SO THAT line. |
| F12 | N22-B | `65bcec1b2e8f3cd47451ca625f5ad1fbdc9c057d206f904ff4dc77f730957978` | directional control | `translations/N22-B.md` | `ledgers/ledger_N22B.json/.pl` | Patched and frozen rig 1, plus the same diagnostics. |
| F13 | T61-B | `a0011041b9e532e17754aa622e2ccde5734a0c8a9107a46af3fc0df7907457cd` | primary opaque-storage case | `translations/T61-B.md` | `ledgers/ledger_T61B.json/.pl` | No run: manual document-rule audit. |
| F13 | T61-D | `bd4b66ceeeb52974da95e00826740903e757b59e3b61cd529f1edf6d5f89ec80` | defended control | `translations/T61-D.md` | `ledgers/ledger_T61D.json/.pl` | No run. |
| F13 | T61-I | `9e5cdbbd6d02c20bcc7b39b2c1e456d2c3ea45b59356827332cedca9898c236b` | invariant restatement | `translations/T61-I.md` | `ledgers/ledger_T61I.json/.pl` | No run. |
| F13 | T76-B | `96de1ceee9c8350baae94f7f11c3056c2cf1f6a47e40d20e1b0763cae9177be2` | primary neighbouring-question case | `translations/T76-B.md` | `ledgers/ledger_T76B.json/.pl` | No run: manual document-rule audit. |
| F13 | T76-D | `71abc4296c2c4c6a9690f0e492a289247635d8c605fdf0efb8e854196f5ac41d` | defended control with a different declared question | `translations/T76-D.md` | `ledgers/ledger_T76D.json/.pl` | No run. |
| F13 | T76-I | `63eb5ef92c83a277d64fa353d3152bea67e347392f47f78ef30b86321d62f9f8` | invariant restatement | `translations/T76-I.md` | `ledgers/ledger_T76I.json/.pl` | No run. |
| F14 | N30-A | `861a15b52442705b2b808739091450e9b92553dff87efd13eccd0fe25c600c7e` | forcing representation-boundary case | `translations/N30-A.md` | `ledgers/ledger_N30A.json/.pl` | Patched and frozen rig 1; Fact only. |
| F14 | N30-B | `9ec056199c092c441f14fb607ef0ad62596a3c5daef88fcb6bfbd6d5016d900d` | explicit-agent-and-patient control | `translations/N30-B.md` | `ledgers/ledger_N30B.json/.pl` | Patched and frozen rig 2; `ring` remains outside the shape book. |
| F15 | N18-A | `a6493a1720258acb4dae71164acbab645941ef85f22640ac0bf1b3dfa91e0a92` | forcing direct-opposition case | `translations/N18-A.md` | `ledgers/ledger_N18A.json/.pl` | Patched and frozen rig 1, plus relational co-reference diagnostics. |
| F15 | N18-B | `c07e72b8bdc99d0d677f5ab81cfceb3120920b57fd7e20abd70814aee5919597` | negative-only control | `translations/N18-B.md` | `ledgers/ledger_N18B.json/.pl` | Patched and frozen rig 1, plus the same diagnostics. |

All fourteen prepared IDs are accounted for. A ledger pair is supplied for each because a legal serialization can be made; that does not turn a no-run case into a run-bearing case.

## Proposed run matrix

This matrix is preregistration only. Preserve the first stdout, stderr, exit code and raw-log byte range from every invocation. A solver error or empty raw segment is not a clean semantic result.

| Finding / ID | Role | Patched rig 1 | Frozen rig 1 | Patched rig 2 | Frozen rig 2 | Direct queries after the full report |
| --- | --- | --- | --- | --- | --- | --- |
| F11 N29-A | forcing | no run | no run | no run | no run | none; event identity is fixed by translation from “same push” and “denies a second push” |
| F11 N29-B | control | no run | no run | no run | no run | none |
| F12 N22-A | forcing/discrepancy | run | run | not applicable | not applicable | both rig-1 copies: `claim_plan(N,A,F)`; `changes(turn(dial),X)`; `depends_on(kept_cool(pear),X)`; `achieves(turn(dial),kept_cool(pear))`; `holds(kept_cool(pear))`. Patched only: `produced(kept_cool(pear))` |
| F12 N22-B | directional control | run | run | not applicable | not applicable | the same five shared queries and one patched-only query |
| F13 all T61/T76 | manual wording cases | no run | no run | no run | no run | none |
| F14 N30-A | forcing boundary | run | run | not applicable: no legal Happening was written | not applicable | `holds(rang(bell))`; do not query or invent `did/5` |
| F14 N30-B | supplied-participants control | not applicable | not applicable | run | run | both copies: `did(E,I,V,T,D)` and `shape(ring,S)`; patched only: `no_shape(E,V,T)` |
| F15 N18-A | forcing | run | run | not applicable | not applicable | both rig-1 copies: `claim_because(N,E,C)`; `denied_because(N,E,C)`; `claim_because(N1,E,C), denied_because(N2,E,C)`; `contradiction(F)`. Patched only: `produced(opening_happened)` |
| F15 N18-B | negative-only control | run | run | not applicable | not applicable | the same four shared queries and one patched-only query |

For F12, an answer to `achieves/2` is only the checker's relevance relation: an action changes a slot on which the goal depends. It is not evidence that the source asserted a plan, that the goal occurred, or that turning produced coolness. The `claim_plan/3`, `holds/1` and `produced/1` queries guard those distinctions.

For F15, the co-reference query asks whether the serialized positive and negative relations have exactly the same `E` and `C`. It does not add a contradiction rule. `contradiction/1` asks what the unmodified rig currently detects.

### Exact driver invocations

Let `D` be the absolute path to this `F11_F15` directory and `R` the absolute path to the copied, never-source-mutating rig bundle. Use copied raw logs in the return staging area.

```text
cd "$R/rigs/rig 1 - arguments"
python3 patched/run_check.py "$D/ledgers/ledger_N22A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 frozen/run_check.py  "$D/ledgers/ledger_N22A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 patched/run_check.py "$D/ledgers/ledger_N22B.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 frozen/run_check.py  "$D/ledgers/ledger_N22B.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 patched/run_check.py "$D/ledgers/ledger_N30A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 frozen/run_check.py  "$D/ledgers/ledger_N30A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 patched/run_check.py "$D/ledgers/ledger_N18A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 frozen/run_check.py  "$D/ledgers/ledger_N18A.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 patched/run_check.py "$D/ledgers/ledger_N18B.pl" "$OUT/raw_logs/rig1/raw_log.txt"
python3 frozen/run_check.py  "$D/ledgers/ledger_N18B.pl" "$OUT/raw_logs/rig1/raw_log.txt"

cd "$R/rigs/rig 2 - causes"
python3 patched/check2.py "$D/ledgers/ledger_N30B.pl" "$OUT/raw_logs/rig2/raw_log.txt"
python3 frozen/check2.py  "$D/ledgers/ledger_N30B.pl" "$OUT/raw_logs/rig2/raw_log.txt"
```

Redirect each invocation's stdout and stderr to unique attempt files while retaining its exit code. Run the direct queries against the same ledger and the exact rules copy named in the corresponding matrix cell. Do not add a temporary `claim_plan`, production rule, participant, response class or movement to make a query fire.

## What this preparation does not establish

It does not adjudicate F11-F15, certify either rig, show that a clean report covers the input, or establish that these serializations are the unique legal translations. It freezes source-faithful cuts so that later outputs cannot retroactively change the input preparation. Any later change to a ledger is a new prepared version and must remain beside this one.
