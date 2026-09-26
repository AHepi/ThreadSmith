# S98 — Ledger of edits and recommendations

*Log S98, 26 September 2026, under decision S30. Made by program (`build/build_ledger.py`).*

This ledger holds every edit made to the theory texts and every recommendation for one, from the making of file 10 to the S97 cross-examination (1894 records of 1293 changes), each lined up under the sentence of the latest text it touches, and the sentences grouped by the part of the semantics they belong to. It leaves out the reasons given for each change: only the sentences and wordings are copied, byte for byte, and each record's source file and source reference are the only pointer to why it was made or proposed.

## The groups

| group | units (touched / all) | changes placed here | records shown in the group | records in full under their home sentence | pointer lines | vocabulary lines | records in blocks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [G01 The document as a whole](line-up/groups/01%20The%20document%20as%20a%20whole.md) | 28 / 46 | 86 | 142 | 62 | 2 | 38 | 54 |
| [G02 Organizations and their changes](line-up/groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md) | 27 / 66 | 52 | 74 | 52 | 35 | 24 | 7 |
| [G03 Questions](line-up/groups/03%20Questions%20%28Part%20III%29.md) | 42 / 56 | 75 | 135 | 83 | 1 | 61 | 24 |
| [G04 Layers, transports, and provenance](line-up/groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md) | 68 / 98 | 120 | 208 | 142 | 17 | 87 | 34 |
| [G05 Account](line-up/groups/05%20Account%20%28Part%20V%29.md) | 51 / 68 | 157 | 213 | 137 | 15 | 82 | 42 |
| [G06 Work, routes, and interference](line-up/groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md) | 62 / 67 | 143 | 231 | 160 | 109 | 159 | 23 |
| [G07 Exact constructions](line-up/groups/07%20Exact%20constructions%20%28Part%20VII%29.md) | 34 / 48 | 43 | 77 | 57 | 8 | 25 | 2 |
| [G08 Transport results](line-up/groups/08%20Transport%20results%20%28Part%20VIII%29.md) | 21 / 27 | 38 | 65 | 45 | 9 | 37 | 4 |
| [G09 Criticism, use, and usable arguments](line-up/groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md) | 41 / 51 | 69 | 114 | 76 | 11 | 48 | 1 |
| [G10 Understanding, construction, and origin](line-up/groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md) | 49 / 80 | 105 | 191 | 122 | 17 | 60 | 34 |
| [G11 Repair, created explanation, and appraisal](line-up/groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md) | 26 / 27 | 77 | 137 | 82 | 7 | 48 | 29 |
| [G12 The physical module](line-up/groups/12%20The%20physical%20module%20%28Part%20XII%29.md) | 23 / 35 | 51 | 81 | 52 | 9 | 20 | 12 |
| [G13 Recursion and universality](line-up/groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md) | 7 / 14 | 22 | 47 | 16 | 0 | 11 | 22 |
| [G14 The class collected](line-up/groups/14%20The%20class%20collected%20%28Part%20XIV%29.md) | 50 / 55 | 118 | 204 | 144 | 30 | 151 | 19 |
| [G15 What would rule this class out](line-up/groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md) | 16 / 18 | 89 | 148 | 116 | 14 | 45 | 2 |
| [G16 Vocabulary across the text](line-up/groups/16%20Vocabulary%20across%20the%20text.md) | — | 48 | 93 | — | — | — | — |

G16 holds vocabulary changes that run across the text; its records also stand, as vocabulary lines, under the sentences of G01 to G15 they touch. A record on sentences of several groups is counted in each group where it is shown.

## Where things are

- [`line-up/index.md`](line-up/index.md): how the line-up is made, how to read an entry, every section of the text in order with its group, and the 26 records open for the owner.
- `line-up/groups/`: the sixteen group files; `line-up/by idea.md`: the idea proposal's twenty ideas as a cross-index.
- `line-up/data/`: `records.jsonl` (every record once), `tree.json` (the structure), `by sentence.csv` (one row per showing).
- What the ledger does not hold, and why: the section "What is not here" of `line-up/index.md`. What was corrected and added after the ledger's two checks: `build/fixes after the checks.md`.
- `collect/`: the five collectors' records and coverage notes, and `collector F.jsonl`, the records added after the two checks; `group/`: the anchoring to the latest text, the two proposals, and the chosen structure (`grouping and structure, chosen.md`).
- Rerun: `PYTHONDONTWRITEBYTECODE=1 python3 build/build_ledger.py` (runs `line-up/scripts/build.py`, then `line-up/scripts/check.py`, then writes this page).
