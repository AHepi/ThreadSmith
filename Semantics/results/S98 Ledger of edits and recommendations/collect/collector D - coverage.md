# Collector D — coverage (logs S95, S96, S97)

*Log S98, 26 September 2026. Collector D's stretch: the scrub (S95), the repairs (S96, stages 1 and 2) and the last cross-examination with its reading and stage 3 (S97). Not committed.*

## Output

- `collector D.jsonl` — 952 records, one JSON object per line, in the shared shape (16 fields, in the given order). md5 9f6808fd7fcc875d5a6ddea82f0312e2.
- `collector D - scripts/` — the programs that made and tested it: `lib.py` (texts, headings, sentence bounds, span application), `edits.py` (the replacement files), `vocab.py` (the three vocabulary tables), `reclib.py`, `recs_s95.py`, `recs_s96.py` (the proposals), `build_D.py` (writes the jsonl), `check.py` (the tests below). Rerun: `PYTHONDONTWRITEBYTECODE=1 python3 build_D.py`, then `python3 check.py`.
- `collector D - build report.json` — the rebuild md5s and the part counts.

No reason is copied into any record: `source_ref` is the only pointer to the reasons. Wording is copied byte for byte from its source (LaTeX included). Seventeen table cells of the vocabulary files carried a reason in brackets beside the wording; the bracket was cut and nothing else (list at the end).

## Record ranges

| rids | source | kind | records |
|---|---|---|---|
| D-1 – D-300 | `tests/S95 Scrub - scripts/replacements.json` (298 entries, 74 of them made by the AUTO rules of `replacements_source.py`, plus the 2 added paragraphs of `fill_blank_lines`) | edit, applied in the scrubbed copy | 300 |
| D-301 – D-378 | `tests/S96 Repair - scripts/replacements.json` (stage 1: 77 entries and the whole-line replacement of l. 2) | edit, applied in the repaired copy | 78 |
| D-379 – D-406 | `tests/S96 Repair - scripts/replacements_stage2.json` (stage 2) | edit, applied in the repaired copy | 28 |
| D-407 – D-491 | `tests/S96 Repair - scripts/replacements_stage3.json` (stage 3, log S97) | edit, applied in the latest text | 85 |
| D-492 – D-567 | `tests/S95 Scrub - vocabulary, as used.md` | edit, scope term | 76 |
| D-568 – D-621 | `tests/S95 Scrub - vocabulary, sceptic's rulings.md` (section 2 rows with new words, section 3 rows) | recommendation, scope term | 54 |
| D-622 – D-717 | `tests/S95 Scrub - vocabulary, proposed.md` (every row of section 2) | recommendation, scope term | 96 |
| D-718 – D-778 | `results/S95 Does the semantics hold without verificationist words.md`, sections 7–9 | recommendation | 61 |
| D-779 – D-808 | `results/S95 Scrub - check of the opening note, …, and Parts 0 to VIII.md`, "Repairs" (R1–R19, the two optional clarity wordings) | recommendation | 30 |
| D-809 – D-841 | `results/S95 Scrub - check of Parts IX to XV and every derivation, proof or argument after them.md`, section 6 (repairs 1–23) | recommendation | 33 |
| D-842 – D-873 | `results/S96 Check of the repaired copy - whole text.md`, section 5 (R-1 … O-7) | recommendation | 32 |
| D-874 – D-875 | `results/S96 Check of the repaired copy - cases.md`, "Repairs proposed" | recommendation | 2 |
| D-876 – D-952 | the six replies in `results/S96 Cross-examination - repaired copy - returns/` (Atria A 7, GLM A 4, Mimo 1 22, Mimo 2 13, Mimo 3 13, Mimo 4 18), with the rulings of `results/S96 Reading of the replies.md` | recommendation | 77 |

## Counts

By kind and status:

| kind | applied | superseded | declined | not applied | open for the owner | all |
|---|---|---|---|---|---|---|
| edit | 566 | 0 | 0 | 1 | 0 | 567 |
| recommendation | 267 | 79 | 23 | 2 | 14 | 385 |
| all | 833 | 79 | 23 | 3 | 14 | 952 |

By round: S95 650, S96 217, S97 85 (the stage-3 edits; the replies' own proposals carry S96, the round of the calls, and their rulings are the S97 reading's). By scope: span 426, sentence 269, paragraph 26, term 231.

By source and status:

| source | applied | superseded | declined | not applied | open for the owner |
|---|---|---|---|---|---|
| S95 replacements.json | 300 | | | | |
| S96 replacements.json (stage 1) | 78 | | | | |
| S96 replacements_stage2.json | 28 | | | | |
| S96 replacements_stage3.json | 85 | | | | |
| S95 vocabulary, as used | 75 | | | 1 | |
| S95 vocabulary, proposed | 50 | 44 | 1 | | 1 |
| S95 vocabulary, sceptic's rulings | 49 | | 4 | | 1 |
| S95 results file, sections 7–9 | 51 | 4 | | 1 | 5 |
| S95 range 1 reading (Parts 0–VIII) | 23 | 3 | | | 4 |
| S95 range 2 reading (Parts IX–XV and after) | 28 | 3 | | 1 | 1 |
| S96 Check file, whole text | 30 | | 1 | | 1 |
| S96 Check file, cases | 1 | | | | 1 |
| reply Atria A | 3 | 3 | 1 | | |
| reply GLM A | 3 | 1 | | | |
| reply Mimo 1 | 3 | 7 | 12 | | |
| reply Mimo 2 | 7 | 5 | 1 | | |
| reply Mimo 3 | 8 | 3 | 2 | | |
| reply Mimo 4 | 11 | 6 | 1 | | |

## How the statuses were set

- **Edits** (the four replacement files): applied, each in the text its stage wrote. The one edit "not applied" is the as-used row "advanceable challenges | kept, BORDERLINE" (the word was kept).
- **S95 proposals** (results file and the two range readings): applied where an S96 stage-1 entry names them in its `ref` (R1…R19, B1…B15, "range 2 repair N", "range 1 optional clarity"); superseded or not applied or open for the owner as the stage-1 `not_applied` list says (R2 and R7 superseded; range 2 repairs 4, 13 and 14's "tentatively accepts" superseded; B12's marker superseded by F; R6 option A, the optional l. 455 wording and hard case 1 the owner's; the optional l. 403 not applied). Each is linked by `same_as` to the stage-1 edit that carries it and to the same proposal in the other S95 file.
- **The two S96 Check files**: applied where a stage-2 entry names the item in its `ref` (W R-1 … O-6, K O37); declined for W P-1's first part; open for the owner for W O-7 and K's l. 317 question. Linked to the stage-2 edits.
- **The replies**: from the rulings in the reading's section 3. FIX taken as worded or near it ("as proposed", "close to the reply's wording", "the reply's split", "the reply's first sentence") → applied. FIX in other words ("in a third wording", "with other words", "by a pointer, not the formula", "with a gloss instead", "minimal", or the reading's own wording) → superseded: the place was changed, not with the reply's words; `same_as` points at the stage-3 edits whose `ruling` carries the same id, and those hold the words used. KEEP, and parts of a FIX not taken up (Mimo 1's (P1)–(P5) labels, Mimo 1 3's L31 wording, Mimo 1 5's L141 sentence, Mimo 3 6 at L347, Mimo 4 F4's claim) → declined. Every stage-3 edit of group X is linked from at least one reply record.
- **Vocabulary**: proposal rows follow the sceptic's ruling on the row that covers them (KEEP → applied; CHANGE → superseded, the sceptic's words being the ones used, sometimes keeping part of the proposal; OWNER → open for the owner, applied as a provisional name); the proposal to have "does not separate an elegant account from an inelegant one" is declined (the as-used table differs from both). Sceptic rows are applied, except section 2 row 8 (the as-used table differs from the sceptic at l. 317) and four section 3 rows whose words are not in the scrubbed copy (l. 57, l. 159, l. 277, l. 317), which are declined. The map from proposal rows to sceptic rows was made by hand (`P2S` in `vocab.py`).

## Sources read

md5 of each file as read (HEAD at the end of the work: 4a857f814f71ee5add0e100e1a151fa9bc2336e7).

| file | md5 | what was read |
|---|---|---|
| tests/Revision 2 - file 13 draft 5, theory text.md | 7f1d8ad02adf96e27622593bd263252e | by program: lines, headings, sentences |
| tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md | 2517ef4ec1f274e8de2bfb7e6661ef94 | by program |
| tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md | 8bb4d19d5aad53de2492b2193fd23ff1 | by program; a few lines by eye |
| tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md | ebca15a047f686b15d5f5766b69825c9 | by program |
| tests/S95 Scrub - scripts/replacements.json | bd2b5bc3f9339287c0670575d901c301 | all, by program |
| tests/S95 Scrub - scripts/scrub_apply.py | cb52f1f1778f098f76a3ec9401434ce7 | the apply rules |
| tests/S95 Scrub - scripts/replacements_source.py | 22c3e66d3dd5e0b5a4a337678df62f7c | the AUTO rule lines only (their entries are in the JSON, marked "generated") |
| tests/S95 Scrub - vocabulary, as used.md | 035455701472f44811abb617babb7f3c | all tables |
| tests/S95 Scrub - vocabulary, proposed.md | bb1cecd5036b25fa74f7951178f7b4a7 | the section 2 tables, by program |
| tests/S95 Scrub - vocabulary, sceptic's rulings.md | e82b440128148d21c6c062708338e716 | the section 2 and 3 tables, by program |
| results/S95 Does the semantics hold without verificationist words.md | 5bbb207285cb2f3a6a252a3e2d2aef23 | sections 7–13 |
| results/S95 Scrub - check of the opening note, the note of sources and departures, and Parts 0 to VIII.md | 89040474615883d586db41aadc8dfca7 | headings; the "Repairs" section |
| results/S95 Scrub - check of Parts IX to XV and every derivation, proof or argument after them.md | c5d13de327148d93c89eaaa09562c183 | headings; section 6 |
| results/S95 Scrub - cases re-read on the scrubbed text.md | cfd7f5e96a9bf26f7799535ebebbdd15 | headings and the closing section: it proposes no wording (it points to the two range readings) |
| tests/S96 Repair - scripts/replacements.json | 210adcf921e679374ae144df92fe778d | all, by program |
| tests/S96 Repair - scripts/replacements_stage2.json | c6feec2d56a851cfef8e64686a064540 | all, by program |
| tests/S96 Repair - scripts/replacements_stage3.json | 49e0f42423858dc57347298153304a62 | all, by program |
| tests/S96 Repair - scripts/replacements_stage3_extra.json | 94fadf328cce25429860c479d42029eb | by program: no entries; its `not_applied` is the same list as stage 3's |
| tests/S96 Repair - scripts/repair_apply.py | 27b6be13823767897a660ead8b98c0d9 | the docstring and the apply rules |
| results/S96 Check of the repaired copy - whole text.md | 3b06dd9fa2ba9a52d5506cf19dd793df | headings; section 5, parsed by program |
| results/S96 Check of the repaired copy - cases.md | 3ab6bf93a5f7df386a726c631e550123 | "In brief"; "Repairs proposed" |
| results/S96 Reading of the replies.md | b75fdd9350f454946abdcb8cc3f737cc | sections 0–10 (Appendix A not read: it prints `replacements_stage3.json`) |
| results/S96 Cross-examination - repaired copy - returns/s96_xexam_atria_A.response.txt | e8c70f7c58f89a876f021acaaeeb1402 | all |
| …/s96_xexam_glm_A.response.txt | aa5fb89dbf9ae96b0875246b114702f0 | the findings |
| …/s96_xexam_mimo_1.response.txt | a64710a4be05a0e43ee7ae7a5c8750b3 | the findings |
| …/s96_xexam_mimo_2.response.txt | 5b21c78534c5fd83d70bf0bd891b97db | the findings |
| …/s96_xexam_mimo_3.response.txt | ba4e1b5f876d234fc01e04875218e241 | the findings |
| …/s96_xexam_mimo_4.response.txt | e867023ae29a4fbddd56744d0e56811a | the findings |
| tests/S96 Repair of the scrubbed copy - plan.md | a050cf0fe2c700b4b531d2481f9569ed | headings, section 10 (open points) and the stage-2 "Not applied" list: no wording beyond what the JSON files hold |
| results/S96 The scrubbed copy repaired - physical possibility, conflict by argument, premises taken as given.md | 82ee665fbb7db748522df644c1f38d0c | searched only, for "not applied": it lists the same items as the JSON files |

## Sources skipped, and why

- `tests/S95 Scrub - register of words in draft 5.json` / `.md` and `tests/S95 Scrub - scripts/register.py`: a register of words found in draft 5, not a change or a proposal.
- `tests/S96 Repair - scripts/replacements_source.py`, `replacements_stage2_source.py`, `replacements_stage3_source.py`, `plan_build.py`: they write the JSON files and the plan. The JSON files were used, and rebuilding the texts from them gives each text's md5 exactly (below); the source files add the reasons, which the ledger leaves out.
- The `borderline` and `physical_mentions` notes of the four JSON files: words kept, each with a reason; not changes.
- `tests/S96 Cross-examination - repaired copy - part 1 … part 4, part A, part B`: the excerpts sent to the readers; no proposals.
- `results/S96 How the cross-examination of the repaired copy will be read - written before sending.md`, `results/S96 GLM 5.3 pilot - written before sending.md`, `results/S96 note - GLM 5.3 as an outside reader, quick research.md`: rules and notes; no wording for the theory.
- The replies' `.reasoning.txt`, `.request.json` and `.receipt.json` files, and Atria's part B (`s96_xexam_atria_B.pass1.*`): no reply came back from part B; the reading used only the `.response.txt` files, and so does this ledger.
- `records/Semantics - Decisions.md` (S28): the owner's words of S28 enter the text through stage 3's group O, recorded as edits D-407 onward with `ruling` "S28 (i)" or "S28 (ii)"; the decisions file was not needed for the wording.

## Tests run by program (`check.py`)

1. **Rebuilds.** Draft 5 plus the S95 entries and the two added paragraphs gives the scrubbed copy (md5 2517ef4e…, equal line for line). The scrubbed copy plus stage 1 gives the stage-1 text (md5 c1eecbd1587e5aec91fd0ba7d46e1469, the md5 `repair_apply.py` asks for; this text is not on disk and is rebuilt in memory). Stage 2 on it gives the repaired copy (equal); stage 3 on the repaired copy gives the latest text (equal).
2. **Every `old` recorded as applied is found verbatim in its target text**: 634 applied records with a span as `old` were compared (all 491 edits of the replacement files and 143 applied recommendations); **1 miss**: D-736, the S95 results file's R12 at l. 307, which quotes "Here a route of the candidate is a member of S" without the text's markup (`\(\mathsf S\)`); the range 1 reading's copy of the same proposal (D-798) quotes it with the markup and is found. Recommendations whose source gives no old wording and whose `old` was left empty are not in the 634.
3. **Term records** (vocabulary cells): a cell names draft 5's words in a description, so each of its words and quoted phrases was looked for in draft 5 (markup and case ignored). 35 of the applied term records have a word not found as written, in each case a description ("Part IX title", "where no assessor is meant"), notation written without markup (`Lic_j`, `O_ep`), the "draft 5 → proposed" pair as the sceptic restates it, or an S95-reading term written against the scrubbed copy (`R_j`).
4. **Every `old_sentence` is verbatim in its target text**: 0 misses. **Every edit's `new_sentence` is verbatim in the text its stage wrote**: 0 misses.
5. Shape: 952 records, all 16 fields in order, no rid twice, every `same_as` names an existing rid, no empty `target_part`.

## How the sentences were built

- The four texts keep the same 632 lines, so `target_line` is one key across all of them. `target_part` is the Part heading and section heading in force at that line **of the target text**, so the same line may carry a different Part title in different texts (Part VI is "Work, support, and interference" in draft 5 and "Work, routes, and interference" from the scrubbed copy on; Parts IX, XI, XV and XVI change titles too). Group on `target_line` first.
- For each edit, all the edits of its stage on that line were applied together (as the apply scripts do), and `old_sentence` / `new_sentence` are the whole sentence(s) around the span in the line before and after. A sentence ends at ".", "?" or "!" (with any closing quote, bracket or `*`) followed by a space and a capital, a quote, `*`, a bracket or a backslash; nothing inside `\( \)` or `\[ \]` ends a sentence; "l.", "e.g.", "i.e.", "cf." and the like, single initials and list numbers do not end one. Where a change runs across sentences, or another change on the line does, both fields cover all of them. Headings, list items and display lines are their own "sentence".
- Stage-2 edits and the proposals of the two S96 Check files are written against the **stage-1 text**, named in `target_text` as "stage-1 text (S96; scrubbed copy with stage 1 applied, rebuilt in memory)".
- S95 proposals are written against the scrubbed copy. Where the source quotes the old words, those are `old`. Where it gives only a line and the new words (78 of the 124), `old` is the old span of the stage-1 edit that carries the proposal, when that edit is on the same line; this is marked here and not in the records. Where the source says "the last two sentences", "the first sentence", "from … to the end of the item", `old` was cut from the scrubbed copy by program. Where the proposal's words replace the whole sentence, `new_sentence` is the proposal itself; where they contain "…", no `new_sentence` was built.
- Reply proposals: a reply mostly gives a whole replacement line or sentence in a code block and names the line. The sentence(s) it replaces were found in the repaired copy by similarity (difflib) within four lines of the named line, and recorded as `old` and `old_sentence`; ratios run from 0.42 to 1.00, and the lowest (D-898 0.42, D-944 0.47, D-945 0.49, D-886 0.52, D-889 0.54) were each read by eye and name the sentence meant. Two reply lines were off: Mimo 1's "L141" for ρ_p is l. 147 of the repaired copy, and Mimo 4 F9 (ii)'s premise is on l. 562; the records carry the repaired copy's lines. Insertions (Mimo 2's two abbreviation clauses) have an empty `old` and the sentence they follow as `old_sentence`.

## What could not be recovered, or is given only as a description

- Proposals with no wording (`new` begins "[no wording given]"): W O-7 (D-873), K's l. 317 question (D-875), Mimo 1 finding 3's "the same words … at L257" (D-893), Mimo 1 finding 4's "Part XV must carry the same labels (P1)–(P5)" (D-895), Mimo 2's note on "(Part VIII)" (D-911).
- No `old_sentence` for 21 recommendations (and for the 2 added paragraphs of S95, which fill blank lines): an insertion whose place the source does not give (D-718); words written without markup (D-736); a sentence added after one that another proposal first writes (D-861, after B-3's); markers and options with no place in the old text (D-743, D-768, D-786, D-790); new sentences added with no anchor (D-770, D-772, D-775, D-792, D-836, D-841); inline wordings with no single place (D-904, D-907, D-934); and the five with no wording above (D-873, D-875, D-893, D-895, D-911).
- The S95 results file's "l. 8" borderline item and hard case 1, the S96 reading's "S28 (i), places considered and left", GLM's account of the missing (I3), Atria's remark on L195 and Mimo 3's remark on L369's header: no wording proposed; not recorded.
- `same_as` between a vocabulary term record and the per-occurrence edits it covers was not made: a term row is a rule, the edits are its occurrences, and matching them by word would join unrelated edits. Group them by the term's words.

## Reason brackets cut from vocabulary cells

D-541, D-544, D-555 (as used: the "differs from …" brackets); D-598, D-599, D-601, D-602, D-603, D-604, D-610, D-613, D-614, D-615, D-616, D-619, D-621 (sceptic's section 3); D-682 (proposal). In each, one bracketed clause giving why was removed from the cell; the words around it are unchanged.
