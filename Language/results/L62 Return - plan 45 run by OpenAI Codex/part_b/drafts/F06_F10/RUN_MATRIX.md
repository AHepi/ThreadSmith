# F06-F10 proposed exact run matrix

Written by: OpenAI Codex

This matrix was written before any ledger in this folder was run. It proposes commands and queries; it records no observed output. Every invocation must use its own new raw log and captured report. Any solver error, timeout, malformed answer, or nonzero wrapper exit invalidates that invocation. No joined driver and no rig patch is authorised here.

`Patched` means the current `patched` driver and its colocated rules or laws. `Frozen` means the current `frozen` driver and its colocated rules or laws. Patched output is adjudicative where the table says so. Frozen output is a historical diagnostic and cannot override patched output.

| Finding / ID | Role | Ledger | Patched run | Frozen run | Preregistered queries and interpretation |
| --- | --- | --- | --- | --- | --- |
| F06 N16-A | Forcing | `rig2/ledger_N16A` | Rig 2; adjudicative for the stipulated word-slot behaviour | Rig 2; diagnostic | Standard driver plus `social(E,W,I,T,R)`, `word_misfit(n16a,makes)`, and `tendency_stated(n16a)`. The source-derived tendency and MAKES line must remain present. This run cannot decide whether ordinary “produced” has the same stipulated sense. |
| F06 N16-B | Lexical control | `rig1/ledger_N16B` | Rig 1; coverage diagnostic only | Rig 1; coverage diagnostic only | Standard report plus `holds(production_attribution(moving_walkway,nora,continued_toward(exit)))`. No `social/5` query is licensed because the literal text uses no listed causal word. Do not compare a rig-2 word verdict against this rig-1 fact as though both adapters asked one question. |
| F07 N19-A | Forcing | `rig1/ledger_N19A` | Rig 1; adjudicative for route-report behaviour | Rig 1; diagnostic | Standard report plus `holds(rang(bell))`, `holds(rose(flag))`, and `claim_since(N,E,C)`. Record endpoint support separately from the offered flag-to-ringing route. A missing BECAUSE-circle report is expected to be a coverage distinction unless the text-derived SINCE route itself is mishandled. |
| F07 N19-B | Independent control | `rig1/ledger_N19B` | Rig 1; adjudicative control | Rig 1; diagnostic | Standard report plus `holds(rose(flag))`, `holds(rang(bell))`, and `claim_since(N,E,C)`. The binned denial of reverse provenance is untested. |
| F07 N20-A | Target-order forcing case | `rig1/ledger_N20A` | Rig 1; adjudicative only for the exact mixed SINCE/BECAUSE translation | Rig 1; diagnostic | Standard report plus `claim_since(N,E,C)`, `claim_because(N,E,C)`, `holds(opened(gate))`, and `holds(rang(bell))`. The source-designated target is `opened(gate)`. Do not recode the final BECAUSE as SINCE to make the chain routine choose a different terminal item. |
| F07 N20-B | Conventional-order control | `rig1/ledger_N20B` | Rig 1; adjudicative control | Rig 1; diagnostic | Standard report plus `claim_since(N,E,C)` and `holds(opened(gate))`. The last SINCE target and the explicitly named final conclusion are both `opened(gate)`. |
| F08 N23-A | Negative diagnostic | `rig1/ledger_N23A` | Rig 1; adjudicative for silence of the standard diagnostic; supplemental structural queries required | Rig 1; diagnostic | Standard report; then `holds(open(gate))` with all lines, and the same query with said line `s1` removed. The first should have a route and the second should not. No claim line may be added merely to trigger patch 10. |
| F08 N23-B | Structural positive control | `rig1/ledger_N23B` | Rig 1; supplemental structural query, not a standard-warning test | Rig 1; diagnostic | Standard report; then `holds(open(gate))`. There are no said object-level lines to remove, so the query is unchanged by delete-all-said. If no standard warning prints, record the driver's claim-domain limit instead of adding a claim. |
| F09 N25-A | Forcing | `rig1/ledger_N25A` | Rig 1; adjudicative | Rig 1; diagnostic coverage only because frozen has no JSON what-if executor | Standard patched report executes MAKE NOT SO `pushed(box)`, asks `holds(moved(box))`, and compares it with the proposed assessment's `claims: true`. If the report says HOLDS, that confirms carryover by the proposed assessment; it does not validate the assessment. |
| F09 N25-B | Source-supplied control | `rig1/ledger_N25B` | Rig 1; adjudicative | Rig 1; diagnostic coverage only | Standard patched report executes MAKE NOT SO `pushed(box)`, asks `holds(moved(box))`, and compares it with source-supplied `claims: false`. Also inspect the named `no_push` case. An inherited actual movement that clashes with the case is the target failure mode. |
| F10 T26-B | Non-selection forcing case | `rig1/ledger_T26B` | Rig 1; adjudicative with supplemental queries | Rig 1; diagnostic | Standard report plus `holds(entry)`, `holds(open(side_gate))`, and `holds(open(front_gate))`. Entry should be held; neither gate may be selected from the Only-ways constraint. |
| F10 T26-D | Specified-side control | `rig1/ledger_T26D` | Rig 1; adjudicative control | Rig 1; diagnostic | Standard report plus `holds(entered(cart))`, `holds(open(side_gate))`, and `holds(open(front_gate))`. The side-gate query is source-supported; the front-gate query is not. Exclusivity is not tested. |
| F10 T26-I | Paraphrase forcing case | `rig1/ledger_T26I` | Rig 1; adjudicative with supplemental queries | Rig 1; diagnostic | Standard report plus `holds(entered(cart))`, `holds(open(side_gate))`, and `holds(open(front_gate))`. Neither gate may be selected. |
| F10 T27-B | Inclusive-alternatives forcing case | `rig1/ledger_T27B` | Rig 1; adjudicative | Rig 1; diagnostic | Standard report plus `contradiction(F)`, `holds(open(side_gate))`, and `holds(open(front_gate))`. Both gate facts should stand and the inclusive requirement should not create a contradiction. |
| F10 T27-D | Out-of-scope exact-one contrast | `rig1/ledger_T27D` | Rig 1; coverage diagnostic only | Rig 1; coverage diagnostic only | Standard report plus both open-gate queries. No verdict on “exactly one may” is admissible because that clause is in the bin. |
| F10 T27-I | Unnamed-target paraphrase | `rig1/ledger_T27I` | Rig 1; coverage diagnostic only | Rig 1; coverage diagnostic only | Standard report plus both open-gate queries. Do not introduce `entry` or an Only-ways head from the family question.

For standard runs, use these command forms from the relevant rig directory, substituting an invocation-specific empty log path:

```text
python3 patched/run_check.py LEDGER.pl UNIQUE_RAW_LOG
python3 frozen/run_check.py LEDGER.pl UNIQUE_RAW_LOG
python3 patched/check2.py LEDGER.pl UNIQUE_RAW_LOG
python3 frozen/check2.py LEDGER.pl UNIQUE_RAW_LOG
```

Supplemental queries are read-only probes against the same exact ledger and rules hash. Their raw solver output must be stored separately and labelled supplemental; they do not become standard-driver findings. Removed-line probes must name the removed line in their receipt. No output may be sorted into a pile until every adjudicative row above is either successfully run or explicitly marked untested.
