# Part B execution summary: F11-F15

Written by: OpenAI Codex

## Scope and frozen boundaries

This execution follows `PART_B_PREREGISTERED_RUN_MATRIX.md`. F11 (`N29-A`, `N29-B`) and F13 (all `T61` and `T76` records) remain translation/manual-audit cases and were not run. The twelve preregistered native runs for F12, F14 and F15 were executed against separate frozen and patched rig copies. Forty-seven preregistered direct queries were then executed as transparent assessment machinery. No source, translation, ledger, driver or rules file was edited, and no rig patch was made.

Every native run has its own `execution.json`, `report.stdout.txt`, `wrapper.stderr.txt`, `exit_code.txt`, and `raw_log.txt`. Every direct query has its own `query.json`, solver stdout/stderr, and exit record. Those JSON records preserve the query or exact driver command and SHA-256 hashes of the ledger, driver/rules and s(CASP) executable as applicable.

All twelve native wrappers exited 0 and none timed out. That is execution evidence only. Every native raw log contains s(CASP) predicate-existence errors which the historical driver suppresses while still printing a report. The wrapper's automatic missing-predicate heuristic recognizes “unknown procedure” and “no rules for” but not s(CASP)'s wording, `scasp_predicate ... does not exist`; consequently, `execution.json` labels those lines “material” rather than “missing predicate.” The raw text is authoritative. Relevance to the assessed question is distinguished below.

## Native-run observations

| Finding / record | Frozen report | Patched report | Raw-output limit |
| --- | --- | --- | --- |
| F12 `N22-A` | Prints `NO FAULT FOUND` | Prints `NO FAULT FOUND` | The native plan-related query is an existence error because the source-faithful ledger has no `claim_plan/3`; many other unconditionally issued predicates are absent. Neither report is a clean plan verdict. |
| F12 `N22-B` | Prints `NO FAULT FOUND` | Prints `NO FAULT FOUND` | Same adapter limit as `N22-A`. |
| F14 `N30-A` | Prints `NO FAULT FOUND` | Prints `NO FAULT FOUND` | The source is represented only as `holds(rang(bell))`; the native reports contain unrelated absent-predicate errors and do not test an invented `did/5`. |
| F14 `N30-B` | Prints gauge only | Prints `Verbs with no shape: ring` | Both raw logs contain existence errors for unrelated `said_moves/3` and `said_stays/2` checks. The patched `no_shape/3` result is separately confirmed by a clean direct query. |
| F15 `N18-A` | Reports the positive BECAUSE line as `JUMP` | Reports the positive line as `JUMP` and the exact denial as `Fine` | The production-support query in the patched raw log errors because `produced/1` has no clause in this combined program. Thus `Fine` is not treated as proof of a clean support check. The relational opposition is assessed directly below. |
| F15 `N18-B` | Prints `NO FAULT FOUND` | Reports the denial as `Fine` | The patched production-support path has the same absent-predicate confound. The control's negative relation is confirmed directly; no positive relation was serialized. |

## Direct-query observations

### F12 — dependency relevance is not goal success

For both records and both rig-1 copies, `changes/2`, `depends_on/2`, and `achieves/2` returned an answer with no solver error:

| Record | Changed/dependency slot | `achieves(turn(dial),kept_cool(pear))` |
| --- | --- | --- |
| `N22-A` | `setting(dial)` | Answer 1 in frozen and patched rules |
| `N22-B` | `set_to_cool(dial)` | Answer 1 in frozen and patched rules |

The answer is exactly what the rig defines: the action changes a slot on which the goal depends. It does not establish that the pear was kept cool. `claim_plan/3` produced a predicate-existence error in both copies rather than a clean negative answer. `holds(kept_cool(pear))` is absent in the source: the frozen query errors because `holds/1` is undefined there, while the patched query is defined but has no model. Patched `produced(kept_cool(pear))` also raises a predicate-existence error because no `produced/1` clause is present. The held result is therefore relevance, not a source plan, occurrence or successful production.

Hard-to-vary mark: changing the setting atom distinguishes the forcing case from the directional control but leaves the result unchanged because each action and goal share the same corresponding slot. The result depends on that structural match; it does not depend on treating the corpus question as a ledger assertion.

### F14 — retain the representational boundary

For `N30-A`, `holds(rang(bell))` returned Answer 1 in both rig-1 copies. No `did/5` query was issued and no doer or patient was invented.

For `N30-B`, `did(E,I,V,T,D)` returned `p1, ada, ring, bell, none` in both rig-2 copies. `shape(ring,S)` had no model in both. The patched-only `no_shape(E,V,T)` returned `p1, ring, bell`, matching the patched native report. This isolates the result: the event is stored with its supplied participants, while the unknown verb remains outside the shape book.

Hard-to-vary mark: the two records differ at the exact feature that licenses the Happening form—explicit doer and thing. Replacing `ring` with a known shape verb or adding a participant to `N30-A` would change the source, so neither move is available to rescue coverage.

### F15 — exact relational opposition is invisible to generic contradiction

For `N18-A`, both rig-1 copies returned answers for:

- `claim_because(N,E,C)` as line 3, `opening_happened`, `fleaming_happened`;
- `denied_because(N,E,C)` as line 4 with the same effect and cause; and
- the joint co-reference query, proving that the two relations share exactly the same `E` and `C`.

Nevertheless, `contradiction(F)` had no model in both copies. That predicate only checks `holds(F)` together with `denied(F)` and has no rule connecting an exact `claim_because/3` / `denied_because/3` pair to contradiction. The patched `produced(opening_happened)` query is an existence error, not a clean no-production answer.

For negative-only control `N18-B`, `denied_because/3` returned line 3 with the same effect/cause atoms, and `contradiction(F)` had no model. Queries for the absent positive `claim_because/3` fail with a predicate-existence error rather than a clean negative answer; the ledger itself contains no positive clause. The joint co-reference query therefore errors for the same absence.

Hard-to-vary mark: `N18-A` already preserves both opposing commitments and their co-reference. Varying the translation into generic positive/negative facts would test a different representation. The failure point is the checker's generic contradiction definition, while the control shows that a denial alone should not be called a contradiction.

## What is held, loose, and blocked

- Held: the source-faithful F12 structural relevance results, F14 Fact/Happening boundary and unknown-verb diagnostic, and F15 exact relational opposition are reproduced by direct, interpretable queries.
- Loose: native `NO FAULT`, `Fine`, or gauge-only prose wherever the bearing query or another report-generating query encountered an existence error. Those strings are not promoted to semantic success.
- Blocked: a clean native plan verdict for F12 and a clean native productive-support verdict for F15. The absent predicates are preserved as runtime evidence rather than repaired after seeing output.
- Not tested by design: F11 event identity and F13 report/question fidelity; those remain manual translation/document-rule adjudications.

No post-result translation change, adapter change, rig patch, or pile-2 repair was made.
