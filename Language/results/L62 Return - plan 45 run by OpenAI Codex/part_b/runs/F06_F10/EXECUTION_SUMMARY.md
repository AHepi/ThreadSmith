# Part B execution summary: F06-F10

Written by: OpenAI Codex, under plan 45, from the other model's corpus.

## Scope and frozen boundaries

This execution follows `PART_B_PREREGISTERED_RUN_MATRIX.md`. It ran the selected F06-F10 slice without changing a source record, translation, ledger, rig, driver, or rules file. F06 `N16-A` was run on both selected projections: rig 2 for the narrow MAKES/tendency check and rig 1 for the separately stated ordinary production attribution. F06 `N16-B`, all selected F07-F09 records, and F10 `T27-B`, `T27-D`, and `T27-I` were run on rig 1. The three T26 records remain `NR` exactly as preregistered.

There are 28 native executions: fourteen distinct ledger/rig selections, each against frozen and patched copies. There are also 54 separately labelled direct-query executions against the exact frozen or patched rule file. Every native execution has its own `execution.json`, `report.stdout.txt`, `wrapper.stderr.txt`, `exit_code.txt`, and `raw_log.txt`. Every direct query has its own `query.json`, solver stdout/stderr, and exit record.

No post-output repair, adapter change, rig patch, or source reinterpretation was made.

## Execution integrity and error boundary

All 28 native wrappers exited 0, parsed their ledger with SWI-Prolog, used distinct raw-log paths, and recorded no timeout. All 54 direct queries exited 0 with no timeout and no solver error: 50 returned at least one answer and four cleanly returned no model. The four no-model results are the frozen and patched `N23-A` queries after removal of `s1`, and the frozen and patched `T27-B` contradiction queries. s(CASP) writes the expected `No models` warning to stderr for those four; the exit code remains 0 and no `ERROR` appears.

Every native raw log contains at least one s(CASP) predicate-existence error because the historical drivers unconditionally ask optional predicates absent from these small ledgers. The wrapper exits remain 0 because those drivers suppress the child-query exit codes. Consequently, `NO FAULT FOUND`, `FINE`, a gauge-only report, or wrapper exit 0 is not treated as a semantic success. Only the raw block for the bearing query, corroborated where preregistered by a clean direct query, is interpreted below.

The slice draft's matrix says any solver error invalidates an invocation, while the later governing addendum expressly permits missing optional predicates to be preserved and requires the bearing query to be interpretable. Because the task designates the addendum as governing, this summary makes no claim that any native invocation is globally clean; it salvages only the separately identified clean bearing blocks. Readers applying the earlier global rule instead must mark all 28 native invocations blocked and use the 54 direct-query receipts only as supplemental observations.

The native wrapper's `--rules` argument is receipt metadata rather than an argument passed to the historical driver. For this run, a static cross-check confirmed that each driver loaded its colocated file (`checker_rules.pl` for rig 1, `laws.pl` for rig 2) and that its hash equals the rules hash in the receipt. All current ledger, driver, rules, report, stderr, raw-log, and solver hashes match their receipts. The direct-query runner does not preserve the exact temporary combined program by hash. For the N23 removal probe, the inspected ledger has the declaration `line(s1).` before any guarded use, so the runner's first-match removal removed the intended declaration; the receipt still records this as an assessment transform, not a source edit.

One selected-input attribution difference is preserved rather than repaired: `selected/rig1/ledger_F06_N16A.json` says `OpenAI Codex, under frozen plan 45, from the other model's corpus`, whereas the draft adapters use the requested `OpenAI Codex, under plan 45, from the other model's corpus`. The governing matrix explicitly selected that rig-1 adapter, so its two receipts retain the differing string. It must not be silently treated as byte-identical authorship metadata.

Runtime identity for this execution: s(CASP) executable SHA-256 `2110e60890a766b1a630dba595f4e9752f01662ebd5301d61af1fba685fa2ad7`, repository commit `2dfbdb9cb41f8b9198f19289bab73dd72efad46a`, SWI-Prolog 9.0.4, Python 3.12.14. The runner hashes are `793ac081244f39cb79b2e7ccdca60c3d75f97a94ac7ce8d416b10fa0bbd580c8` for `run_pair.py` and `58b642c93d5b661f2ae6cf6c9ea168a49701ca0ea4a3e153e5a8d77710b24cd9` for `run_direct_query.py`.

## Native and bearing-query observations

| Finding / record | Patched adjudicative observation | Frozen diagnostic | Attribution limit |
| --- | --- | --- | --- |
| F06 `N16-A`, rig 2 | The native report says `THE WORD DOES NOT FIT THE SLOTS` for MAKES. Clean direct queries return the exact `social(n16a,makes,moving_walkway,nora,continue_toward(exit))`, `tendency_stated(n16a)`, and `word_misfit(n16a,makes)` answers. | The same three bearing answers and the same word-misfit report. | This is a verdict on the stipulated MAKES slots only. It does not refute the separately stated ordinary production attribution. |
| F06 `N16-A`, rig 1; `N16-B`, rig 1 | Each production-attribution query returns one answer. The native reports say `NO FAULT FOUND`, but their logs contain unrelated existence errors and the rig has no semantic rule for the free production fact. | Same fact-preservation result; no ordinary-production assessment. | These runs establish serialization, not a same-measurement control for MAKES. F06 therefore retains the preregistered owner-decision boundary. |
| F07 `N19-A` | The patched driver reports the press-to-ringing SINCE step and ringing-to-flag step as holding, the offered flag-to-ringing step as `NO CONNECTION`, and the ringing endpoint as standing through the independent press route. Clean direct queries expose all three SINCE claims and both endpoints. | The frozen driver does not inspect SINCE; its `NO FAULT FOUND` is not a verdict. Direct frozen queries nevertheless confirm the same serialized claims and endpoints. | The core endpoint/route separation is observed. The plan's predicted `CIRCLE` label is not: exact-text `supports`/`inferred` was preserved as SINCE/SHOWS, while the circle routine is BECAUSE-specific. |
| F07 `N19-B` | The one independent flag-to-ringing SINCE route holds and the final ringing conclusion stands. | The frozen driver does not inspect SINCE; direct queries confirm the stored route. | The source's denial of reverse provenance remains binned because file 38 supplies no NOT-SINCE form. |
| F07 `N20-A` | The press-to-ringing BECAUSE claim `FOLLOWS`; the one SINCE step supports `opened(gate)`; the printed final conclusion is `opened(gate)`. | The frozen driver calls the BECAUSE claim a `JUMP` and does not inspect SINCE. | The exact run does not reproduce the plan's predicted miss of the first-stated conclusion. That is not evidence of a general target mechanism: the explicit target designation remains in the bin, and the later relation is BECAUSE rather than a second SINCE step. The alleged page-order defect is not forced by this adapter. |
| F07 `N20-B` | Both SINCE steps hold and the final conclusion is `opened(gate)`. | The frozen driver does not inspect SINCE; direct queries confirm both serialized steps and opening. | This is the conventional-order control only. |
| F08 `N23-A` | The native driver emits no added-lines warning. Direct `holds(open(gate))` has one answer with all lines and no model after removing said line `s1`, in both rule copies. | Same structural direct-query result; the frozen native driver has no added-lines diagnostic. | The added bridge parasitises the source fact. No conclusion claim was invented merely to activate patch 10. |
| F08 `N23-B` | The native driver again emits no added-lines warning. Direct `holds(open(gate))` has one answer using only filled-in lines `f1` and `f2`, in both rule copies. | Same structural direct-query result. | This exposes a broader silence than the plan predicted: patch 10 iterates explicit BECAUSE/SINCE claims, and this exact source supplies no separate claim object. The structural query is supplemental evidence, not a native warning. |
| F09 `N25-A` | The native patched what-if removes direct push line `p1`, asks `holds(moved(box))`, receives an answer from actual movement line `m1`, and prints `Your what-if HOLDS` relative to the proposed assessment's `claims:true`. | The frozen driver has no JSON what-if executor and prints `NO FAULT FOUND`; that string is not a counterfactual result. | This reproduces the plan's predicted actual-to-counterfactual carryover. `HOLDS` means the driver matches the described proposed assessment, not that the assessment is warranted. |
| F09 `N25-B` | The patched what-if receives an answer for actual movement and therefore prints `Your what-if FAILS` against the source-supplied `claims:false`. Its named-case pass also reports a `moved(box)` contradiction between actual line `m1` and supposed line `c2`. | The frozen driver, which lacks case isolation, reports the same pair as an undifferentiated contradiction. | Conditional on the disclosed anaphoric resolution that the old photograph records actual movement. The sentence does not restate the photograph's content, so this control cannot bear an unconditional verdict. F09's forcing result does not depend on this control because `N25-A` already reproduces the carryover. |
| F10 `T27-B` | Clean direct queries return both open-gate facts and no model for `contradiction(F)`. | Identical direct-query results. | This confirms that the inclusive alternative requirement does not conflict with both alternatives being open. It does not test selection from an uninstantiated alternative set; T26 remains unrun by design. |
| F10 `T27-D` | Both open-gate facts return answers. | Identical direct-query results. | The exact-one/may rule is in the bin, so the native `NO FAULT FOUND` cannot adjudicate it. |
| F10 `T27-I` | Both open-gate facts return answers. | Identical direct-query results. | The at-least-one modal/quantity clause has no named dependent content and remains in the bin. As preregistered, this DX cannot determine the pile. |

## Exact direct-query counts

The following counts are answer-block counts, not truth scores. All listed queries exited 0 without timeout or `ERROR`.

| Record | Queries, frozen then patched |
| --- | --- |
| `N16-A` rig 2 | `social/5`: 1/1; `word_misfit(n16a,makes)`: 1/1; `tendency_stated(n16a)`: 1/1 |
| `N16-A` rig 1 | ordinary production attribution: 1/1 |
| `N16-B` rig 1 | ordinary production attribution: 1/1 |
| `N19-A` | `holds(rang(bell))`: 2/2; `holds(rose(flag))`: 3/3; `claim_since/3`: 3/3 |
| `N19-B` | `holds(rang(bell))`: 2/2; `holds(rose(flag))`: 1/1; `claim_since/3`: 1/1 |
| `N20-A` | `claim_since/3`: 1/1; `claim_because/3`: 1/1; `holds(opened(gate))`: 2/3; `holds(rang(bell))`: 1/2 |
| `N20-B` | `claim_since/3`: 2/2; `holds(opened(gate))`: 3/3 |
| `N23-A` | `holds(open(gate))`, all lines: 1/1; after removing `s1`: 0/0 |
| `N23-B` | `holds(open(gate))`, unchanged: 1/1 |
| `T27-B` | `contradiction(F)`: 0/0; side gate: 1/1; front gate: 1/1 |
| `T27-D` | side gate: 1/1; front gate: 1/1 |
| `T27-I` | side gate: 1/1; front gate: 1/1 |

## Held, loose, and blocked

- Held by clean bearing queries: F06's narrow MAKES/tendency mismatch; F07's serialized routes and patched endpoint/route treatment; F08's two distinct dependency patterns; and F10's explicit gate facts plus the absence of a T27-B contradiction.
- Held by a clean native bearing block: F09 `N25-A` carries actual movement into the no-push query. This is the forcing evidence for the planned pile-2 defect. `N25-B` points the same way but remains conditional on its disclosed anaphoric reading.
- Loose: every native `NO FAULT FOUND`, `FINE`, or gauge-only phrase in a log containing unrelated existence errors; F07's general target-order claim, which `N20-A` does not force; and any inference from a free production-attribution fact to the rig-2 MAKES verdict.
- Blocked or outside the run: a semantic check of ordinary “produced” in F06; a NOT-SINCE check for `N19-B`; a native patch-10 warning without an explicit claim object; the binned exact-one and modal clauses in `T27-D/I`; and every T26 non-selection case.

No result above licenses changing a ledger or rig after seeing the output.
