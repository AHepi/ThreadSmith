# S98 — Grouping and structure, chosen: the line-up by part of the semantics

*Log S98, 26 September 2026, under the owner's instruction of that day (decision S30). This page judges the two proposals for lumping the ledger (`proposal by place.md`, `proposal by idea.md`), gives the choice, and specifies the data files and views that a builder makes by program from it. It was written after reading both proposals, the anchoring summary, the place proposal's `sections.json` and `assignment.jsonl`, the idea proposal's `ideas.py` heading table and assignment file, and a sample of records, and after running measures on them by program. Nothing was changed in any input, and nothing is committed.*

## 1. The choice

**A merge, with the sentence of the latest text as the unit.** The line-up has sixteen groups. Fifteen are parts of the semantics named by the theory's own Part titles (Parts II to XV, plus one group for the document as a whole). The sixteenth holds vocabulary changes that run across the text. Inside a group come the sections of the latest text, and inside a section its sentences in text order. Under each sentence stands every record that touches it, oldest first, with the records of one change kept together.

- **From the place proposal:** the sections (`sections.json`, 134 of them, *not* joined), the placement of each change (`assignment.jsonl`: majority section, section its source names, section lead at 0.5 or more, Part residue), and the whole-text vocabulary group.
- **From the idea proposal:** where a section of Part 0, Part I or Part XVI speaks about the matter of another Part, it is filed with that Part. The idea proposal's heading table (`ideas.py`, `HOME_LABEL`) names that Part for most of these sections; §3 lists every case. Each change also keeps its idea (`group`, `also`, `near_tie`) as a cross-index (`by idea.md`) and as a *form only* tag.
- **Not taken:** placing whole changes by word-list weights as the first level, and joining small sections.

### Why this and not either proposal as it stands

Figures come from programs run on the inputs of §2.

1. **The owner's key is the sentences.** A line-up that files *changes* splits the history of one sentence whenever the changes on it land in different groups.
   - The idea proposal would split the records on **299 of the 540 changed sentences** over two to nine groups: 150 over two, 99 over three, 50 over four or more.
   - The place proposal, filing by change, would split **268 of 540** over two to six groups. This happens because a change that spans sections goes to its majority section, and vocabulary changes go to the whole-text group.
   - Filing by *sentence* splits none: every sentence of the latest text stands in exactly one group, with every record that touches it.
2. **The theory's Parts already name its matters.** The Parts are "Organizations and their changes", "Questions", "Layers, transports, and provenance", "Account", "Work, routes, and interference", "Exact constructions", "Transport results", "Criticism, use, and usable arguments", "Understanding, construction, and origin", "Repair, created explanation, and appraisal", "The physical module", "Recursion and universality", "The class collected" and "What would rule this class out". Nearly all of the idea proposal's twenty ideas are re-cuts of these Parts. Using the Parts' own titles keeps a reader's map of the theory. It also leaves no boundary to Claude's word lists: those lists moved 271 changes under one adjustment, and they leave 302 near ties.
3. **Three Parts speak about the other Parts.** Part 0 (the grievances, "Two words", "What is imported", "Where to attack this"), Part I (the commitments) and Part XVI (the ten arguments) each speak about another Part's matter. A reader of "Questions" should find grievance 4, grievance 10 and argument 7 there, because they change how questions and contracts are stated. The idea proposal's strength is kept here, but at section level: 30 sections are filed, each named in §3, and each section stays whole and keeps its Part label.
4. **The idea proposal remains as a cross-index.** Its per-change ideas, its *also* lists and its *form only* group show where one change carries two ideas. They also show the 77 edits that alter only punctuation, emphasis, pointers or labels. They cost nothing to keep as tags.
5. **Small sections are not joined.** With the sentence as the unit, a section of one or two changes is only a sub-heading, not a group. Joining neighbours would make "neighbour, not matter" groups (all of Part II in one, for example).

What stays weak:

- The 119 changes with no place in the latest text stay in per-Part blocks. Part V's block holds 36 changes, from R2 amendments against file 20.
- The 45 changes placed by named section or section lead (the lead named the right section about 9 times in 10 when tried) are marked as placed that way.
- Records that sit on sentences of several groups are shown in full once, with a pointer line at each other sentence.

## 2. Inputs (read only)

All paths are under `/home/user/ThreadSmith/Semantics/results/S98 Ledger of edits and recommendations/group/`.

| input | md5 | used for |
| --- | --- | --- |
| `anchored.jsonl` | 41752268722000a376a15e7de2bde76e | the 1850 records (1275 changes), all fields |
| `sentence index of the latest text.jsonl` | fdaf069a0c1d71be4e17b38d2f6bce82 | the 756 units of the latest text (id, line, line_end, n, kind, part, heading, label, text) |
| `proposal by place - scripts/sections.json` | c4f53beacd7f699a930191e2cb95f9fe | the 134 sections: `section` [Part key, name], `first_line`, `last_line` |
| `proposal by place - scripts/assignment.jsonl` | 2b57aec91e82dec64aaa9686ca3ca377 | per change: `group`, `section`, `how` |
| `proposal by idea - assignment.jsonl` | 921b4ceb5a918f5fb30425c1068c6ff5 | per change: `group`, `group_name`, `also`, `near_tie` |

The build stops with an error if any md5 differs, or if a round, target version or Part key turns up that §5 or §3 does not name. The latest text itself is not read: the sentence index carries its units.

## 3. The sixteen groups, and where each section goes

| id | group name (the theory's Part title) | file (in `line-up/groups/`) |
| --- | --- | --- |
| G01 | The document as a whole | `01 The document as a whole.md` |
| G02 | Organizations and their changes | `02 Organizations and their changes (Part II).md` |
| G03 | Questions | `03 Questions (Part III).md` |
| G04 | Layers, transports, and provenance | `04 Layers, transports, and provenance (Part IV).md` |
| G05 | Account | `05 Account (Part V).md` |
| G06 | Work, routes, and interference | `06 Work, routes, and interference (Part VI).md` |
| G07 | Exact constructions | `07 Exact constructions (Part VII).md` |
| G08 | Transport results | `08 Transport results (Part VIII).md` |
| G09 | Criticism, use, and usable arguments | `09 Criticism, use, and usable arguments (Part IX).md` |
| G10 | Understanding, construction, and origin | `10 Understanding, construction, and origin (Part X).md` |
| G11 | Repair, created explanation, and appraisal | `11 Repair, created explanation, and appraisal (Part XI).md` |
| G12 | The physical module | `12 The physical module (Part XII).md` |
| G13 | Recursion and universality | `13 Recursion and universality (Part XIII).md` |
| G14 | The class collected | `14 The class collected (Part XIV).md` |
| G15 | What would rule this class out | `15 What would rule this class out (Part XV).md` |
| G16 | Vocabulary across the text | `16 Vocabulary across the text.md` |

The "home Part" of G02–G15 is the Part whose number the group bears (G02 ↔ Part II … G15 ↔ Part XV). G01 and G16 have no home Part.

**Rule for sections.** A section is an entry of `sections.json`. Every unit of the sentence index lies in exactly one section: the section with `first_line ≤ unit.line ≤ last_line`. The build asserts this, and that no two sections overlap.

- A section whose Part key (`section[0]`) is one of II … XV goes to the group of that Part.
- A section whose Part key is `FM`, `0`, `I` or `XVI` goes by the table below, keyed by `first_line`–`last_line`.

The column "idea proposal's home" is for reading only. It gives the idea that `ideas.py` names for the heading; where the two differ, the choice here follows the Part that treats the matter.

| lines | Part | section (name in `sections.json`, abridged) | group | idea proposal's home |
| --- | --- | --- | --- | --- |
| 1–2 | FM | Opening of the Part (title, note) | G01 | frame |
| 3–3 | FM | A structural class of explanatory creativity … | G01 | frame |
| 7–7 | 0 | Opening of the Part | G01 | frame |
| 8–8 | 0 | Two words, as used here | G09 | argument / ruling |
| 9–17 | 0 | What this document claims | G01 | frame |
| 19–27 | 0 | What this document does not claim | G01 | frame |
| 29–31 | 0 | What is imported, what is an index, and what is defined | G14 | inputs |
| 33–35 | 0 | Grievances, anticipated / introduction | G01 | frame |
| 37–37 | 0 | Grievance 1 (declared kinds) | G02 | organization |
| 39–39 | 0 | Grievance 2 (operationalism) | G02 | organization |
| 41–41 | 0 | Grievance 3 (selected correspondences) | G04 | provenance |
| 43–43 | 0 | Grievance 4 (relative to a contract) | G03 | question |
| 45–45 | 0 | Grievance 5 (teleosemantics …) | G04 | provenance |
| 47–47 | 0 | Grievance 6 (explanation replaced with evolution) | G04 | provenance |
| 49–49 | 0 | Grievance 7 (mathematics has no interventions) | G07 | constructions |
| 51–51 | 0 | Grievance 8 (where is aesthetics) | G11 | appraisal |
| 53–53 | 0 | Grievance 9 ('selected' as stipulation) | G04 | provenance |
| 55–55 | 0 | Grievance 10 (freezing the question) | G03 | question |
| 57–57 | 0 | Grievance 11 (kinds exist; a rule is not a cause) | G02 | organization |
| 59–61 | 0 | Where to attack this | G15 | ruleout |
| 65–65 | I | Opening of the Part | G01 | frame |
| 67–67 | I | Faithfulness without assessors | G05 | account |
| 69–69 | I | Fallibility without error-as-work | G05 | criticism |
| 71–71 | I | Conjecture, criticism, action | G09 | criticism |
| 73–73 | I | Recursive scrutiny with operative return | G13 | recursion |
| 75–75 | I | Substrate independence with physical conditions | G12 | organization / physical |
| 77–77 | I | Two provenances, not one | G04 | provenance |
| 550–550 | XVI | Opening of the Part | G01 | argument |
| 552–558 | XVI | 1. Kind preservation needs no condition of its own | G02 | organization |
| 560–568 | XVI | 2. Same counterparts, one account | G05 | account |
| 570–576 | XVI | 3. Selected transports are underdetermined … | G04 | provenance |
| 578–584 | XVI | 4. Surprise requires an incomplete history | G04 | surprise |
| 586–592 | XVI | 5. Question-finding is representable | G10 | creativity |
| 594–600 | XVI | 6. There are two imports | G14 | inputs |
| 602–608 | XVI | 7. The frozen assessment and the moving question are consistent | G03 | question |
| 610–612 | XVI | 8. Equivariance under structure-preserving recoding | G08 | layers |
| 614–616 | XVI | 9. Output descriptions do not determine accounts | G05 | account |
| 618–632 | XVI | 10. A two-layer episode, in exact form | G10 | creativity |

Notes on the four cases that differ from, or choose within, the idea proposal's home:

- Line 69 speaks of what cannot count as explanation, which it defines as an account; it goes to G05.
- Line 75 (substrate) goes with the physical module, where "substrate" next stands (line 461).
- Argument 8 goes with Part VIII, which holds *Recoding*.
- "Two words" defines *argument* and tentative acceptance; it goes to G09.

The sections of Part VIII and Part XI keep their Part even where the idea proposal names another idea: *A failed answer stays failed* stays in G08; *Created explanation* and *Appraisal* stay in G11.

Resulting units per group (all 756 units placed once):

| G01 | G02 | G03 | G04 | G05 | G06 | G07 | G08 | G09 | G10 | G11 | G12 | G13 | G14 | G15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 46 | 66 | 56 | 98 | 68 | 67 | 48 | 27 | 51 | 80 | 27 | 35 | 14 | 55 | 18 |

## 4. Placing records and changes

Terms used below:

- **Unit:** a line of the sentence index (sentence, heading, formula or list item), with id `L<line>.s<n>`.
- **Text order of units:** by (`line`, `n`).
- **Section index:** the position of a section in `sections.json`.
- **Vocabulary scope:** a record whose `scope` is `term` or `whole text`.
- **Place of a change:** the entry of `proposal by place - scripts/assignment.jsonl` with its `change_id`, whose fields are `group` (a pair), `section` (a pair) and `how`.

### 4.1 The change's group (used for counting and for records with no sentence)

- If the place entry's `group[0]` is `ALL`: the change's group is **G16**.
- Else if the place entry's `section` equals the `section` of an entry of `sections.json`: the change's group is that section's group (§3), and the change's section is that section.
- Else (the pair is `[<Part>, "Not in the latest text"]`, or `["OUT", "Notes outside the Parts"]`): the change's group is the group of that Part when the Part is II … XV, and **G01** for every other Part key (`0`, `I`, `XVI`, `FM`, `OUT`). The change has no section; it goes to that group's **rest block** for its Part key.

Expected changes per group: G01 86, G02 52, G03 74, G04 118, G05 153, G06 143, G07 42, G08 37, G09 65, G10 105, G11 77, G12 50, G13 22, G14 116, G15 89, G16 46 (sum 1275).

### 4.2 How each record is shown

Each record gets exactly one **display**, plus pointer lines or vocabulary lines as below.

1. **Record with sentences, not vocabulary scope** (`latest_sentences` not empty; `scope` is `sentence`, `span` or `paragraph`).
   - Its **home sentence** is the first of its `latest_sentences` in text order that lies in its change's section (4.1). If its change has no section, or none of its sentences lies there, the home sentence is the first of its sentences in text order.
   - The record is shown **in full** under the home sentence (display `full`).
   - Under each of its other sentences it gets a **pointer line**.
   - If its change is in G16, G16 also lists it as a pointer line.
2. **Record with sentences, vocabulary scope** (`latest_sentences` not empty; `scope` is `term` or `whole text`).
   - The record is shown in full under **every** one of its sentences (display `term line`); the wording of these records is short (median 115 characters).
   - If its change is in G16, it is also shown in full in G16.
3. **Record with no sentence** (`latest_sentences` empty).
   - If its change is in G16, it is shown in full in G16 only (display `vocabulary only`).
   - Else, if its change has a section, it is shown in full in that section's **not-in-the-latest-text block**, at the end of the section (display `block`).
   - Else it is shown in the change group's **rest block** for the change's Part key, at the end of the group file (display `block`).
   - If the record has `latest_nearest`, its record line names that sentence as "nearest latest-text sentence (a lead, not a place)", with a link.

Expected figures:

| group | changes placed here | units | units touched | records in full (display `full`) | pointer lines | vocabulary lines | records in blocks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | 86 | 46 | 29 | 62 | 2 | 37 | 52 |
| G02 | 52 | 66 | 27 | 51 | 28 | 24 | 7 |
| G03 | 74 | 56 | 39 | 80 | 1 | 50 | 25 |
| G04 | 118 | 98 | 68 | 139 | 17 | 85 | 34 |
| G05 | 153 | 68 | 52 | 130 | 15 | 81 | 42 |
| G06 | 143 | 67 | 61 | 157 | 107 | 157 | 23 |
| G07 | 42 | 48 | 32 | 55 | 4 | 25 | 2 |
| G08 | 37 | 27 | 21 | 44 | 9 | 37 | 4 |
| G09 | 65 | 51 | 40 | 70 | 9 | 48 | 1 |
| G10 | 105 | 80 | 49 | 119 | 9 | 59 | 34 |
| G11 | 77 | 27 | 26 | 81 | 6 | 46 | 29 |
| G12 | 50 | 35 | 23 | 49 | 6 | 16 | 12 |
| G13 | 22 | 14 | 7 | 16 | 0 | 11 | 22 |
| G14 | 116 | 55 | 50 | 141 | 24 | 144 | 19 |
| G15 | 89 | 18 | 16 | 115 | 12 | 43 | 3 |
| G16 | 46 | 0 | 0 | — | 1 | — | — |

Totals:

- display `full` 1309;
- pointer lines 249 in G01–G15, plus 1 in G16;
- vocabulary lines 863 (224 records);
- blocks 309 records: 96 in section blocks, 213 in rest blocks;
- G16 shows 88 records in full: 80 vocabulary-scope records with sentences and 8 with none.

Check: 1309 + 224 + 309 + 8 = 1850.

## 5. Order: oldest first

Each record gets `lineup_order`, its position (1 … 1850) when records are sorted by this key:

1. **Round index**, in this order:
   1. `file 20 (before log 25)`
   2. `R2 (log 25)`
   3. `round 4 (log 28)`
   4. `round 5 and Stage C (logs 29, 30)`
   5. `Stage B (logs 41, 55)`
   6. `S62 (log S63)`
   7. `S64 (log S65)`
   8. `S65 (log S70)`
   9. `S70 (log S71)`
   10. `S72 (log S75)`
   11. `S75`
   12. `S76`
   13. `S81`
   14. `S88`
   15. `S89`
   16. `S90`
   17. `S91`
   18. `S93`
   19. `S94`
   20. `S95`
   21. `S96`
   22. `S97`
2. **Target version index**, in this order:
   1. `f10`
   2. `f11`
   3. `f12`
   4. `d2`
   5. `d3`
   6. `d4`
   7. `d5`
   8. `note`
   9. `scrubbed`
   10. `stage1`
   11. `repaired`
3. **Collector letter:** the part of `rid` before the hyphen (A–E).
4. **Record number:** the part after the hyphen, as an integer.

Order everywhere else:

- **Groups:** G01 … G16.
- **Sections within a group:** first the sections of the group's home Part, in text order; then the sections filed from other Parts, in text order. G01 has no home Part and takes all its sections in text order.
- **Rest blocks:** at the end of the group file, one per Part key, in this order: `FM`, `0`, `I`, `II` … `XVI`, `OUT`.
- **Units within a section:** text order. *Every* unit is shown, including those no record touches, so each section reads as the text does.
- **Changes under a unit, or in a block:** by the smallest `lineup_order` among the change's records shown there (in any display), then by `change_id`.
- **Records within a change:** by `lineup_order`.

## 6. Duplicates and links

- **One change, one entry.** Records with the same `change_id` shown at the same unit (or in the same block) form one entry under the change id. The entry header gives the number of records, and lists the other units where records of this change are shown, as links in text order. For a change in G16, the header gives one link to its entry in G16 instead.
- **Same wording shown once.** Inside an entry, records are bucketed by exact equality (byte for byte) of the four fields `old`, `new`, `old_sentence` and `new_sentence`. Buckets are ordered by their smallest `lineup_order`.
  - A bucket of one record is shown as a record line followed by its wording.
  - A bucket of several is shown as a line "Records X, Y, Z (same wording):", then one record line each, then the wording once.
- **Links that were not joined.** Where a record's `same_as` names an id that is not in its `change_members`, the record line ends "linked (not joined): <ids>". These are the 78 pointers into files no collector recorded entry by entry.
- **Long chains are not split.** A change's records are shown by their own sentences when they have them, so a chain of restatements (CH-0152, CH-1018 …) spreads over its sentences, and the entry header lists where the rest are. A chain with no sentence stays together in its block, with each distinct wording shown.

## 7. Data files

The output root is `/home/user/ThreadSmith/Semantics/results/S98 Ledger of edits and recommendations/line-up/`. The builder writes nothing outside it.

### 7.1 `data/records.jsonl` — every record once

- One JSON object per line, 1850 lines, in the order of `anchored.jsonl`.
- Every field of `anchored.jsonl` comes first, in its order, byte for byte (`json.dumps(obj, ensure_ascii=False)`).
- These fields follow, in this order:

| field | value |
| --- | --- |
| `lineup_order` | integer, §5 |
| `lineup_display` | `full`, `term line`, `block` or `vocabulary only` (§4.2) |
| `lineup_group` | the group of the record's full display: its home sentence's group (`full`), its change's group (`term line`, `block`, `vocabulary only`) |
| `lineup_group_name` | the group's name (§3) |
| `lineup_section` | section id of the full display: `sec-L<first>-<last>`, or `rest-<Part key>` for a rest block, or `null` for `vocabulary only` |
| `lineup_home_sentence` | unit id for `full`, else `null` |
| `lineup_pointer_sentences` | list of unit ids (text order) that carry a pointer line to this record; empty unless `full` |
| `lineup_term_sentences` | list of unit ids (text order) where a vocabulary line shows it; empty unless `term line` |
| `lineup_groups_touched` | sorted list of every group in which the record is shown in any way, G16 included |
| `lineup_change_group` | the change's group (§4.1) |
| `lineup_change_placed_by` | the place entry's `how`, verbatim |
| `lineup_idea` | the idea assignment's `group` (key) |
| `lineup_idea_name` | the idea assignment's `group_name` |
| `lineup_idea_also` | the idea assignment's `also` |
| `lineup_idea_near_tie` | the idea assignment's `near_tie` |
| `lineup_form_only` | `"yes"` when `lineup_idea` is `form`, else `"no"` |

### 7.2 `data/tree.json` — the structure, by reference

`json.dump(…, ensure_ascii=False, indent=1)`, keys in the order given:

```
{"about": {"log": "S98", "inputs": {<path>: <md5>, …}, "records": 1850, "changes": 1275, "units": 756},
 "groups": [
  {"id": "G05", "name": "Account", "file": "groups/05 Account (Part V).md", "home_part": "V",
   "sections": [
    {"id": "sec-L229-231", "part_key": "V", "part": "<unit.part of its first unit>", "name": "<sections.json name>",
     "first_line": 229, "last_line": 231, "filed_from_other_part": "no",
     "units": [
      {"id": "L229.s1", "kind": "heading", "line": 229, "line_end": 229, "text": "<verbatim>",
       "entries": [
        {"change_id": "CH-…", "records": [{"rid": "…", "display": "full" | "pointer" | "term line"}, …]}]}],
     "block": [{"change_id": "CH-…", "placed_by": "<how>", "records": ["<rid>", …]}]}],
   "rest": [{"part_key": "V", "changes": [{"change_id": "CH-…", "placed_by": "<how>", "records": ["<rid>", …]}]}]},
  {"id": "G16", "name": "Vocabulary across the text", "file": "groups/16 Vocabulary across the text.md",
   "changes": [{"change_id": "CH-…", "records": [{"rid": "…", "display": "full" | "pointer"}],
                "places": ["<unit id>", …]}]}]}
```

- `entries`, `block` and `rest` are in the order of §5; they are empty lists when nothing is there.
- `filed_from_other_part` is `"yes"` when the section's Part key differs from the group's home Part; in G01, which has no home Part, it is always `"no"`. The view's "filed here from Part <key>" appears exactly when it is `"yes"`.
- `home_part` is the Part key (`"II"` … `"XV"`), or `null` for G01.
- `places` lists, in text order, every unit where a record of the G16 change is shown.

### 7.3 `data/by sentence.csv` — flat, one row per showing

UTF-8, header row, `csv.writer(…, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)`.

**Rows:**

- one per (unit, record) showing in G01–G15 (display `full`, `pointer` or `term line`);
- one per record shown in a block (unit columns empty);
- one per record shown in G16 (group `G16`, unit columns empty, display as in G16).

Rows are ordered as the views are.

**Columns:**

1. `group`
2. `group_name`
3. `section_id`
4. `part`
5. `section_name`
6. `unit_id`
7. `unit_line`
8. `unit_kind`
9. `display`
10. `change_id`
11. `rid`
12. `lineup_order`
13. `round`
14. `kind`
15. `status`
16. `new_in_latest`
17. `latest_status`
18. `applied_in`
19. `scope`
20. `target_text`
21. `target_line`
22. `old`
23. `new`
24. `old_sentence`
25. `new_sentence`
26. `source_file`
27. `source_ref`
28. `idea`
29. `form_only`

Wording columns are verbatim; for pointer rows they are left empty (the full row carries them).

## 8. Views

All views are markdown in UTF-8, ending with one newline.

- **Links** are relative, with the path percent-encoded (`urllib.parse.quote(path, safe="/")`).
- **Anchors** are explicit, and unique within each file:
  - `<a id="L43-s4"></a>` before each unit (the dot of the unit id becomes a hyphen);
  - `<a id="sec-L43-43"></a>` before each section;
  - `<a id="rest-V"></a>` before each rest block;
  - `<a id="CH-0001"></a>` before each change entry in a block or in G16.

### 8.1 How any wording is shown (one rule for all records)

- `before` = `old_sentence` if not empty, else `old`.
- `after` = `new_sentence` if not empty, else `new`.
- Show **Before:** `before`. If it is empty, show `*(nothing: an addition)*`.
- Show **After:** `after`. If it is empty, show `*(nothing: removed)*`.
- If `old_sentence` and `old` are both non-empty and differ, also show **Old wording:** `old`.
- If `new_sentence` is non-empty and differs from `new`, also show **New wording:** `new`, or `*(nothing: removed)*` when `new` is empty.

Each text is written as a blockquote under its label: every line of the text gets the prefix `> ` (an empty line gets `>`), indented to sit inside the list item. Text is otherwise byte for byte, LaTeX and markdown included. A `new` that begins `[no wording given] ` is shown as it stands.

### 8.2 A record line

One line, with fields joined by ` · `:

```
**<rid>** · <round> · <kind> · <status>[ · wording stands | · wording not in the latest text] · written against: <target_text>[, line <target_line>] · carried by: <applied_in> · source: <source_file> — <source_ref>[ · nearest latest-text sentence (a lead, not a place): [<unit id>](<link>)][ · linked (not joined): <ids>]
```

- "wording stands" appears when `new_in_latest` is `yes`, and "wording not in the latest text" when it is `no`; nothing appears for `n/a`.
- Fields copied from a record are shown verbatim, whatever words they contain.

A **pointer line** is:

```
**<rid>** · <round> · <kind> · <status> · shown in full under [<unit id>](<link>)
```

### 8.3 A group file, G01–G15

```
# <NN> <group name>

*<one line: home Part (or "no home Part"), units shown, units touched, changes placed here, records shown here in full, records in blocks; statuses of the records shown here in full: applied n, not applied n, declined n, superseded n, open for the owner n, unknown n>*

<contents: one bullet per section, "<Part> · <section name> · lines a–b · n records", linked to its anchor; then one bullet per rest block>

<a id="sec-L…"></a>
## <Part heading, e.g. "Part V — Account"> · <section name> · lines a–b[ · filed here from Part <key>]

<a id="L229-s1"></a>
#### L229.s1[ · <kind> when not "sentence"] · line 229 (or "lines a–b") · <n> changes, <m> records   (or "· no change recorded")
> <unit text, verbatim, each line prefixed>

- **CH-…** · <n> record(s) · <distinct statuses, in order of first appearance>[ · vocabulary][ · form only][ · also at: <links>]
  - <record line>
    - Before:
      > …
    - After:
      > …
  - Records X, Y (same wording):
    - <record line X>
    - <record line Y>
    - Before: …
  - <pointer line>

##### Not in the latest text, placed with this section
- <a id="CH-…"></a>**CH-…** · <n> record(s) · <distinct latest_status values> · placed by: <how>
  - <record line> + wording, as above

<a id="rest-V"></a>
## Not in the latest text, with no section: Part <key>
- <a id="CH-…"></a>**CH-…** · … (as in a section block)
```

- The section heading's Part label is the `part` of the section's first unit, as the sentence index gives it. For `OUT` it is "Notes outside the Parts".
- "vocabulary" marks a change with any vocabulary-scope record. "form only" marks a change whose idea is `form`.
- The block heading is written only when the block is not empty.

### 8.4 `16 Vocabulary across the text.md`

- Head line of counts, as in 8.3.
- Then one entry per G16 change, in the order of §5:
  - `<a id="CH-…"></a>` and `## CH-… · <n> record(s) · <distinct statuses>`;
  - its records: in full for vocabulary scope and for records with no sentence, as a pointer line for the one other record;
  - then `Places in the latest text (<n>):`, followed by one line per group, in group order: `<group file name>: <unit links, text order>`.

### 8.5 `index.md`

In this order:

1. **Title.** `# S98 — The line-up of edits and recommendations, by part of the semantics`.
2. **An italic note.** Log S98, the date, decision S30, the inputs with their md5, "made by program, nothing committed".
3. **"How it is lined up."** Five to eight lines, restating §1's structure in plain words.
4. **"How to read an entry."** The record line fields; the displays (in full, pointer, vocabulary line, block); the statuses; "wording stands"; "form only".
5. **"The groups."** A table: group (linked), Parts drawn from, units (touched / all), changes placed here, records shown here in full, pointer lines, vocabulary lines, records in blocks, and the status counts of the records shown here in full.
6. **"The text in order."** The cross-index by Part: one row per section of `sections.json` in text order, with Part, section name, lines, group (linked to the section's anchor in its file), units (touched / all), and records touching it.
7. **"Records open for the owner."** The 26 records whose `status` is `open for the owner`: rid, change, round, group and a link to where each is shown in full.
8. **"Files and rerun."**

### 8.6 `by idea.md` — the cross-index by the idea proposal

- One section per idea, in the idea proposal's order: frame, organization, question, layers, provenance, surprise, account, work, rivals, ruling, constructions, argument, criticism, creativity, appraisal, physical, recursion, inputs, ruleout, form. The title of each is the `group_name` from the idea assignment.
- Each section holds a table of the changes whose idea it is, with columns: change, shown in (group, linked), first place, records, statuses, also.
  - "First place" is the first unit in text order where the change is shown, or the anchor of its block entry or G16 entry.
  - Rows are ordered by group, then by first place, then by change id.
- After the table comes one line, "Also carrying this idea:", listing the linked ids of the changes that name it in `also`.

## 9. What the views never show

- **The reasons.** No field that says why a change was made or proposed is shown. `source_file` and `source_ref` are the only pointers to them.
- **Anchoring fields.** The views do not show `anchor_method`, `anchor_ratio`, `latest_reason`, `terms`, `change_members`, `target_version`, or the idea `shares`. They stay in `data/records.jsonl`, and the idea shares stay in the idea assignment file.
- **Kinds of record.** Removed, never-applied and not-locatable records appear only in blocks, with their `latest_status` in the entry header. Not-applied, declined and superseded records with sentences stand under their sentences like any other record, and their status is on the record line. Nothing is left out.

## 10. The builder's own words

All fixed text of the views lives in one constant (a dict of strings) in `scripts/build.py`. This covers headings, labels, legends and notes. It uses:

- none of the words and stems listed below (the task's hard rules and decision S23 name the families);
- "yes" and "no" for flags.

`scripts/check.py` scans those strings, and the index's prose, for the following list (quoted data, for the check only):

```
"fits", "supports", "supported", "verifies", "verified", "corroborates", "corroborated", "proves", "proved",
"disproves", "disproved", "reason to believe", "reason to reject", "better than", "worse than", "true",
"not true", "more true", "established", "authority", "foundation", "foundational", "derived", "derived from"
(decision S23, the owner's list), and the stems "belie", "justif", "verif", "confirm", "corroborat", "rank",
"authorit", "foundation", "better", "worse", "best", "proof", "support", and the words "prove", "proven", "proving"
```

Match whole words for the list and the three words, and word starts for the stems, ignoring case ("provenance" is not matched). Theory headings and record fields are data and are not scanned.

## 11. Checks the builder runs (`scripts/check.py`)

1. The md5s of the five inputs equal those in §2.
2. `data/records.jsonl` has 1850 lines and 1850 distinct rids. Its first fields equal `anchored.jsonl` line for line.
3. Every one of the 756 units appears exactly once over G01–G15. The per-group unit counts equal §3.
4. Every record's showings match §4.2:
   - `full`: one in full, plus one pointer line per other sentence;
   - `term line`: one per sentence;
   - `block` or `vocabulary only`: once;
   - plus G16 as stated.
   The per-group figures equal the table in §4.2.
5. For every showing in full, each wording text displayed, rendered as its blockquote lines, occurs in the file where it is shown.
6. Every relative link resolves to an existing file, and every `#anchor` exists in its target file.
7. The word scan of §10 finds nothing.
8. A second run gives the same bytes for every output (compare md5s). There are no timestamps, and every sort has an explicit key.

Python 3 standard library only. Run with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py && PYTHONDONTWRITEBYTECODE=1 python3 scripts/check.py` from the `line-up` folder. Nothing is committed.

## 12. Files the builder writes

```
line-up/
  index.md
  by idea.md
  groups/01 The document as a whole.md … groups/16 Vocabulary across the text.md   (16 files)
  data/records.jsonl
  data/tree.json
  data/by sentence.csv
  scripts/build.py
  scripts/check.py
```
