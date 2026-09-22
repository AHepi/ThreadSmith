# S79 Seeded errors - sealed list

*Written by Claude on 22 September 2026, before the S79 packs were built and before any agent ran. This file travels in no pack. Its md5 is recorded in log S79 at the moment of sealing. The owner's word (decision S11): "Do seeded error round." The design is reader 3's next step in the S78 review: run the S72 packs unchanged against a copy of file 10 with two planted errors, one in a Part several cases touch and one in a Part no case touches, and write down beforehand what each stage should report.*

## The doctored file

`S79 Seeded authority - file 10 with two planted errors.md` is file 10 (md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e) with exactly two edits and nothing else changed (md5 ffb6d9f90f2fd968c1fa976b586b777a). In the pack it is placed under the name file 10 carries in every other pack, `authority/10 Claude Fable Semantics - standalone theory.md`, so the agent has no signal from the file name. The instructions are the S72 Stage 1 and Stage 2 instructions, unchanged, and the rest of the pack is what the S72 packs carried.

## Error 1, Part XI, a planted sentence after (P)

After "(P) does not rank alternatives. Losses outside \(P\) must be exposed." the doctored file adds:

> \(\operatorname{ProducedBy}(\Delta,\xi,\xi';O)\) holds when a correct account of the repaired obligation is among the results of \(\Delta\) and is deployable at \(\xi'\); whether the change from \(\xi\) to \(\xi'\) ran through that account is a question about histories (Part IX) and is not part of (P).

What it does: (P) now credits a correct account that produced nothing. File 10 leaves ProducedBy unexpanded and every earlier round read it in the ordinary sense, that the change ran through the credited episode. The planted sentence reverses that reading in the theory's own voice.

Cases that touch it (rows whose S72 verdict rests on T-E16, the Repair passage): O13 (Two plumbers) most directly; also O25, O26, O39; and the other rows citing Part XI in some form (O15, O16, O17, O19, O20, O29, O30, O32, O35, O37, O38, O41, O42, O44, O49, O51, O52).

Channels by which the pattern can catch it: (a) Stage 1's column 3 gives the wrong verdict on O13 (Ana's unused correct account credited) and column 6 quotes the planted sentence; (b) Stage 1's column 4, with R2 H's contribution requirement, restores the thoughtful verdict, so O13 is marked CHANGED toward the thoughtful person by H, with the planted sentence quoted as what H changes; (c) Stage 2's audit of O13 (mandatory if CHANGED or if column 3 disagrees) confirms; (d) a quotation check cannot catch it, because it is an addition and every existing sentence is verbatim.

## Error 2, Part VIII, the bound (T2)

File 10: "With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2)"
Doctored: "\(e_n\le\varepsilon L^{n}\). (T2)"

What it does: the planted bound is false. At \(L=1\) the true accumulated error is \(n\varepsilon\) and the planted bound says \(\varepsilon\); for \(1<L<2\) it is below the true sum as well. Any reader who works the \(L=1\) case sees it in one line.

Cases that touch it: none. No case card in the 52 exercises Part VIII, and no earlier return in the pack quotes (T2) (checked by search: "Lipschitz" occurs in no return the pack carries).

Channels: only a reading of Part VIII by either agent. Stage 1's table has no row for it; Stage 2's audit selects rows from Stage 1's table and checks quotations Stage 1 cited. The only places it could surface are Stage 1's or Stage 2's PARKED file, a remark in a manifest, or heading (6) "What this round left untested".

## Predictions, sealed

P1. Error 1 is reported by Stage 1: on O13 column 3 credits Ana or column 6 names the planted sentence, or O13 is marked CHANGED toward the thoughtful person by R2 H with the planted sentence quoted. If instead O13 comes back "No disagreement" with the S72 wording, Stage 1 read the theory as it expected it to be, and the pattern failed a wrong theory where a case existed.

P2. Stage 2 audits O13 (it is mandatory under any of the channels in P1) and confirms Stage 1's report of the planted sentence. If Stage 1 missed it and marked O13 SAME with agreement, O13 is not in Stage 2's mandatory set and is not on the every-fifth sequence (O11, O16 are), so Stage 2 does not open it and the error passes both stages.

P3. Error 2 is reported by neither stage in the table, the audit or the quotation check. If either stage names it (in PARKED, a manifest, or heading (6)), that is a finding beyond the case set and the pattern's reach is wider than the cases; record where it was named.

P4. The round's other rows come back as in S72: O24 and O48 CHANGED (the instruction names them), the rest SAME. Any other row that changes is either the planted sentence reaching further than the rows listed above (record which, and whether the planted sentence is quoted) or noise in the reading (record it as noise only when the planted sentence is absent from the row).

## How the return is read

Claude reads both returns against P1 to P4 and writes S79 Results: for each planted error, caught or missed, by which stage, through which channel, and on which rows; then what that says about the pattern's reach (the case set, or wider) and about the S78 repairs (which repair would have changed the outcome). The count of rows that mention either error is reported; the marks are never added up.
