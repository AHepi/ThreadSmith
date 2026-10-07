C1. "Learned persistent memory makes planning more efficient: 9 exact checks against 12 for fixed order, on our 8-case benchmark."
C2. "The exact check **guarantees** every chosen program reaches the goal."
Source: the engineer's viability report, "Verdict" section.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C2 | In at least one of three scenes whose physics lies outside the supplied model list, the planner answers a confident yes that turns out wrong | missing | none | C2 held only while the world obeys a supplied model |
| F2 | C1 | A ranker using the same two force totals with no learning (plain Newton) also needs 9 or fewer checks on the 8 cases | blocked | the engineer can add it as a sixth arm on the existing benchmark; C1's credit stands if it needs 11 or more | credit to "learned" unmeasured; C1 holds for "the supplied totals", held if F2 loses |
| F3 | C1 | The zero-numbers arm and the least-effort arm order options differently on at least one case | survived | worked out from the stated ranking rule: a zero readout predicts no motion everywhere, so ordering falls to effort then input order; the report's rows are identical | five arms counted as four |
| F4 | C1 | Across 5 fresh draws of the five training lessons, the gain over fixed order falls to 1 check or less | missing | none | C1 held for one lesson draw only |
| F5 | C1 | Case by case, memory beats fixed order in no more cases than chance would give | survived | counted from the report's table: 4 wins, 1 loss, 3 ties; two-sided sign test p = 0.375 | C1 reported as "on these 8 cases", not as general |
| F6 | C2 | Planner forecasts differ from an independent enumeration by the checker on at least one candidate | reported | report: "Every attempted planner forecast exactly matched its independent enumeration"; not rerun by us | none, as reported |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | missing | F4: one benchmark, one lesson draw |
| Q1 | C2 | missing | F1 |
| Q2 | C1 | missing | F2: the totals are momentum and displacement times mass, supplied |
| Q2 | C2 | covered | F6: the checker's family is declared as supplied, and the guarantee is stated as conditional on it |
| Q3 | C1 | missing | F2 |
| Q3 | C2 | does not apply | C2 makes no comparative or credit statement about a rival |
| Q4 | C1 | covered | F3: two arms identical by construction; checks and first-try are one measurement |
| Q4 | C2 | covered | F6: forecasts compared with a separate enumeration, as reported |
| Q5 | C1 | covered | F5: counted case by case; 4 wins, 1 loss, 3 ties, so reported as "on these 8 cases" |
| Q5 | C2 | covered | report: "40/40 supported selections", case by case |
| Q6 | all | covered | all arms ran on identical lessons, goals and programs, as reported |
| Q7 | C1 | covered | worked out: the claim is about ordering efficiency, and the evidence counts checks, so it is the same question |
| Q7 | C2 | missing | F1: "guarantees" is shown only inside the family |
| Q8 | C1 | missing | F4: never met a start not at rest, contact, or varying weight |
| Q8 | C2 | missing | F1 |
| Q9 | C1 | missing | F4, F5: one lesson draw; 8 cases |
| Q9 | C2 | covered | report: "complete physical witnesses for 18/18 trajectories" |
| Q10 | all | covered | report: "The prospective contract was written before the V2 experiment" |
| Q11 | C1 | covered | F3, F5: worked out and counted by us from the report's tables |
| Q11 | C2 | covered | F6: reported, not rerun by us |
| Q12 | C1 | covered | the ordering also decides which workable program is chosen; report table, "Total selected force effort": 88 against 96 |
| Q12 | C2 | missing | F1: a wrong yes would be acted on |
| Q13 | all | covered | all 8 cases counted; error pooled over 672 coordinates, half from a still circle every method gets right, noted |

**Claim as it stands:** on these 8 cases, with one lesson draw, the supplied force totals with 16 learned numbers ordered candidates so that 3 fewer exact checks were needed than fixed order. Every chosen program reaches the goal *held if* the world obeys a supplied model.

**Next test:** run the existing benchmark on three new scenes whose physics lies outside the supplied model list (F1). It needs only new scenes.
