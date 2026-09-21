# F04–F05 execution summary

Written by: OpenAI Codex, under frozen plan 45

## Scope and preservation

This execution used the preregistered matrix and the selected-adapter note without editing any source, plan, rig, rule file, translation or ledger. It ran F04 N14-A, N15-A and N15-B on frozen and patched rig 1; F05 N17-A on the selected frozen and patched rig-2 adapter; and F05 N17-B on the selected frozen and patched rig-1 adapter. T21 was not run. No draft rig-2 N17-B output was created.

Every driver invocation has its own directory below this file. Each directory preserves the exact report, raw log, wrapper stderr, exit code, validation result and hashes in `execution.json`. Every wrapper exited 0, every Prolog pair parsed, and no query timed out. The wrapper's automated missing-predicate classifier does **not** recognize s(CASP)'s wording `scasp_predicate ... does not exist`; consequently its `material_error_line_count` field overcounts missing-predicate stack lines as material errors. The inventory below classifies those lines from the preserved raw text and does not turn them into false answers.

## Exact native reports

### F04 N14-A — rig 1 frozen

```text
REPORT for paragraph F04 N14-A movement with no producer

NO FAULT FOUND in the lines that were checked.

GAUGE: 1 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: metalinguistic notice that fixes the absence of a producer; no producer is invented.. Slowest question: 0.05 seconds.
```

### F04 N14-A — rig 1 patched

```text
REPORT for paragraph F04 N14-A movement with no producer

NO FAULT FOUND in the lines that were checked.

GAUGE: 1 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: metalinguistic notice that fixes the absence of a producer; no producer is invented.. Slowest question: 0.07 seconds.
```

### F04 N15-A — rig 1 frozen

```text
REPORT for paragraph F04 N15-A movement with exact causal denial

NO FAULT FOUND in the lines that were checked.

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: source-attribution wording around the exact denied causal relation.. Slowest question: 0.07 seconds.
```

### F04 N15-A — rig 1 patched

```text
REPORT for paragraph F04 N15-A movement with exact causal denial

NO FAULT FOUND in the lines that were checked.

DENIED BECAUSE on line 3: "[CLAIMED] NOT [line 2 BECAUSE line 1]".
Fine. Nothing in the ledger makes pushed(ada,box) produce moved(box). The effect itself still stands; only the cause is denied.

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: source-attribution wording around the exact denied causal relation.. Slowest question: 0.06 seconds.
```

### F04 N15-B — rig 1 frozen

```text
REPORT for paragraph F04 N15-B movement with stated producer

BECAUSE-claim on line 3: "[CLAIMED] line 2 BECAUSE line 1".
JUMP. Leaving aside the line(s) that simply state it (2), nothing in the ledger makes moved(box) follow.

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: source-attribution wording around the asserted causal relation.. Slowest question: 0.07 seconds.
```

### F04 N15-B — rig 1 patched

```text
REPORT for paragraph F04 N15-B movement with stated producer

BECAUSE-claim on line 3: "[CLAIMED] line 2 BECAUSE line 1".
JUMP. Even granting the stated cause, nothing in the ledger produces moved(box).

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 2 sentences went to the leftover bin (not checked): Sentence 2: source-attribution wording around the asserted causal relation.. Slowest question: 0.07 seconds.
```

### F05 N17-A — rig 2 frozen

```text
REPORT for F05 N17-A assistance without achieved opening  [whose case: OpenAI Codex, under frozen plan 45, from the other model's corpus]

You said (line h1): [CLAIMED] the handle adjustment HELPS the gate open.
  FINE, BUT IT RESTS ON SOMETHING NOBODY STATED: 'HELPS' only fits if they were already heading that way.

GAUGE: 2 lines said, 0 filled in, 0 usual case. Left in the bin: The report-framing words are treated as fixture framing under plan 45's actual-ledger convention; no tendency is supplied.. Slowest question 0.08 seconds.
```

### F05 N17-A — rig 2 patched

```text
REPORT for F05 N17-A assistance without achieved opening  [whose case: OpenAI Codex, under frozen plan 45, from the other model's corpus]

You said (line h1): [CLAIMED] the handle adjustment HELPS the gate open.
  FINE, BUT IT RESTS ON SOMETHING NOBODY STATED: 'HELPS' only fits if they were already heading that way.

GAUGE: 2 lines said, 0 filled in, 0 usual case. Verbs with no shape: none. Left in the bin: The report-framing words are treated as fixture framing under plan 45's actual-ledger convention; no tendency is supplied.. Slowest question 0.07 seconds.
```

### F05 N17-B — rig 1 frozen

```text
REPORT for paragraph F05 N17-B stated adjustment-produced opening

BECAUSE-claim on line c1: "[CLAIMED] line o1 BECAUSE line a1".
JUMP. Leaving aside the line(s) that simply state it (o1), nothing in the ledger makes open(gate) follow.

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 1 sentences went to the leftover bin (not checked): The report-framing words are treated as fixture framing under plan 45's actual-ledger convention; no narrow MAKES line or productive general rule is supplied.. Slowest question: 0.07 seconds.
```

### F05 N17-B — rig 1 patched

```text
REPORT for paragraph F05 N17-B stated adjustment-produced opening

BECAUSE-claim on line c1: "[CLAIMED] line o1 BECAUSE line a1".
JUMP. Even granting the stated cause, nothing in the ledger produces open(gate).

GAUGE: 3 lines said, 0 filled in, 0 usual case; 1 of 1 sentences went to the leftover bin (not checked): The report-framing words are treated as fixture framing under plan 45's actual-ledger convention; no narrow MAKES line or productive general rule is supplied.. Slowest question: 0.08 seconds.
```

## Direct-query receipts

The direct queries are assessment machinery, not added source lines. An answer count of zero below means a clean query with no answer only when `error` is `no`; an undefined predicate is recorded as an error and is not read as false.

| Case | Version(s) | Query | Answers | Error | Observation |
| --- | --- | --- | ---: | --- | --- |
| N14-A | frozen, patched | `holds(moved_away_from(box,wall))` | 1 each | no | The source movement Fact is retained. |
| N14-A | frozen, patched | `contradiction(F)` | 0 each | no | No contradiction is derived. |
| N14-A | frozen, patched | `claim_because(N,E,C)` | 0 each | **yes** | `claim_because/3` is undefined in this program. |
| N14-A | frozen, patched | `denied_because(N,E,C)` | 0 each | **yes** | `denied_because/3` is undefined in this program. |
| N14-A | frozen, patched | `produced(moved_away_from(box,wall))` | 0 each | **yes** | `produced/1` is undefined; this is not a negative production result. |
| N15-A | frozen, patched | `holds(moved(box))` | 1 each | no | Movement stands independently of the causal denial. |
| N15-A | frozen, patched | `holds(pushed(ada,box))` | 1 each | no | The proposed cause stands. |
| N15-A | frozen, patched | `denied_because(N,E,C)` | 1 each | no | The exact denied relation is present. |
| N15-A | frozen, patched | `contradiction(F)` | 0 each | no | No generic fact contradiction is derived. |
| N15-A | frozen, patched | `claim_because(N,E,C)` | 0 each | **yes** | The positive claim predicate is undefined because no positive claim occurs. |
| N15-A | frozen, patched | `produced(moved(box))` | 0 each | **yes** | `produced/1` is undefined; the patched report's “Fine” follow-up cannot be treated as a clean semantic negative. |
| N15-B | frozen, patched | `holds(moved(box))` | 1 each | no | Movement stands. |
| N15-B | frozen, patched | `holds(pushed(ada,box))` | 1 each | no | The stated cause stands. |
| N15-B | frozen, patched | `claim_because(N,E,C)` | 1 each | no | The positive BECAUSE commitment is present. |
| N15-B | frozen, patched | `contradiction(F)` | 0 each | no | No contradiction is derived. |
| N15-B | frozen, patched | `denied_because(N,E,C)` | 0 each | **yes** | The denial predicate is undefined because no denial occurs. |
| N15-B | frozen, patched | `produced(moved(box))` | 0 each | **yes** | `produced/1` is undefined; the native JUMP wording is not a clean negative production proof. |
| N17-A | frozen, patched | `social(E,W,I,T,R)` | 1 each | no | The source-faithful HELPS tuple is present. |
| N17-A | frozen, patched | `word_misfit(n17a,helps)` | 0 each | no | The rig does not establish a slot contradiction. |
| N17-A | frozen, patched | `tendency_stated(n17a)` | 0 each | no | No tendency was supplied or inferred. |
| N17-A | frozen, patched | `holds(stayed_shut(gate))` | 1 each | no | The explicit outcome remains held. |
| N17-A | frozen, patched | `holds(open(gate))` | 0 each | no | Assistance does not derive the goal. |
| N17-B | frozen, patched | `claim_because(N,E,C)` | 1 each | no | The ordinary production claim is retained as BECAUSE. |
| N17-B | frozen, patched | `holds(open(gate))` | 1 each | no | The source-stated opening stands as its own Fact. |

The per-query directories preserve `query.json`, solver stdout, solver stderr and exit code. All F04 undefined-predicate queries exited nonzero with an explicit s(CASP) existence error. All F05 direct queries exited 0 without errors.

## Native-driver error inventory

| Case / driver | Missing-predicate query failures in raw log | Distinct undefined predicates |
| --- | ---: | --- |
| N14-A rig 1 frozen | 3 | `claim_because/3`, `claim_plan/3`, `exception/2` |
| N14-A rig 1 patched | 9 | `claim_because/3`, `claim_since/3`, `claim_plan/3`, `claim_like/3`, `denied/1`, `denied_because/3`, `exempt/2` |
| N15-A rig 1 frozen | 3 | `claim_because/3`, `claim_plan/3`, `exception/2` |
| N15-A rig 1 patched | 10 | `claim_because/3`, `claim_since/3`, `claim_plan/3`, `claim_like/3`, `denied/1`, `exempt/2`, `produced/1` |
| N15-B rig 1 frozen | 2 | `claim_plan/3`, `exception/2` |
| N15-B rig 1 patched | 11 | `claim_since/3`, `claim_plan/3`, `claim_like/3`, `denied/1`, `denied_because/3`, `exempt/2`, `produced/1` |
| N17-A rig 2 frozen | 2 | `said_moves/3`, `said_stays/2` |
| N17-A rig 2 patched | 2 | `said_moves/3`, `said_stays/2` |
| N17-B rig 1 frozen | 2 | `claim_plan/3`, `exception/2` |
| N17-B rig 1 patched | 11 | `claim_since/3`, `claim_plan/3`, `claim_like/3`, `denied/1`, `denied_because/3`, `exempt/2`, `produced/1` |

These are stack-producing existence errors from unconditionally issued driver queries. For N17-A the discriminating `social`, `word_misfit`, `tendency_stated` and outcome queries are clean, so the optional movement/staying predicate errors do not erase that observation. For N15-A, N15-B and N17-B, by contrast, the native causal verdict calls `produced/1`; that relevant query errors, so the displayed “Fine” or “JUMP” prose cannot be promoted to a clean semantic verdict.

## Hard-to-vary interpretation

The explanatory question, the source wording, the selected standing convention and the two rig versions were held fixed. No producer, movement direction, tendency, LETS line, MAKES line or productive general rule was added.

F04's core survives this stress test in a qualified form. N14-A can retain the movement only as a free Fact: the movement has one clean `holds` answer, but the source supplies no happening that would make the typed Result form legal. The native rig-1 report finds no fault and never checks the movement against rig 2's laws. Changing this outcome requires inventing a producer/event and a direction, which changes the forcing case. That supports the claimed representation/coverage gap. The N15 diagnostics establish that positive movement can coexist with an exact denied-BECAUSE commitment and that a positive BECAUSE commitment can be stored, but they do **not** establish clean production negatives: `produced/1` is undefined in both programs. N15-B is therefore only the preregistered documentary control, not a successful executable Result control.

F05's source-faithful result is cleaner than the frozen prose prediction. N17-A contains HELPS, not LETS; it contains no tendency; it explicitly retains `stayed_shut(gate)`; and `holds(open(gate))` has no answer. Thus assistance alone does not establish the goal, which is the conservative boundary F05 is about. The exact frozen expectation “LETS reported against a stated tendency” is not confirmed because neither element occurs in the source. Replacing HELPS with LETS or adding a tendency would make the prediction easier to satisfy only by changing the case. N17-B shows that the stated opening and its ordinary BECAUSE commitment are retained, but its JUMP prose is production-error-contaminated and is not needed for the N17-A conclusion.

The robust parts are therefore: N14-A exposes a source-to-typed-Result representation gap; N17-A confirms that source-faithful assistance does not infer achievement. The loose parts are any claim that an undefined `produced/1` query returned false, and the frozen F05 wording that assumes LETS and a stated tendency. No rig patch is proposed or made here.
