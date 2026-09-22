# The criteria file the markers read

A1 wrote the marker programs before A4 wrote the instrument. This is the shape they read, so
that A4 can write the instrument and nothing in the code needs changing. An example of the shape
is `fixtures/criteria.example.json`; it is an example and not the instrument.

Path: `<W10 harness>/instrument/criteria.json`. The markers read that path with no flag, and
stop if it is not there. `--criteria PATH` points them elsewhere.

```
{
  "version":  a string, so a mark can be traced to the criteria it was made under
  "frozen":   when, in words; the instrument is frozen before any report is read
  "agreement": { "tolerance_documents": 2,
                 "k_rule": ..., "baseline_rule": ..., "uninformative_rule": ... }
  "fields": [ one object per field:
    { "name":      a short id, used as the key in a marks file
      "title":     what a marker sees
      "kind":      enum | map_enum | set | int | bool | text
      "values":    the closed list, for enum and map_enum
      "per":       report | part
      "sort":      within-step | cross-step        (W8 part B4; the markers refuse anything else)
      "layer":     the document | the thing under test | the reader     (plan 52's three layers)
      "criterion": the rule in words a stranger could apply
      "example":   { "report": which report of the record, "value": ..., "quote": the sentence }
      "source":    the report | the run record
      "certified_candidate": true | false
    } ]
  "corpus_affordance": optional; W11 decision D4's table (see below)
}
```

Two keys the counts turn on, both added after the stage-A review.

**`source`.** "the report" means a marker reads it. "the run record" means a program fills it and
the marker never sees it: `first_marker.py` leaves such a field out of the marking prompt and
fills it at `collect` from `<rig>/runs/<reader>/<run>.json`. Asked of a marker who has only the
report, those fields come back null or guessed, and P4.6 then has no field and arm (e) never
names its ports. A field with no `source` is read as the report's.

**`certified_candidate`.** True when stage B can certify the field on the 96 reports in hand.
`agreement.py` reads P4.1, P4.2, P4.3, P4.4, P4.5 and PA.3 over fields with it true — and over
stage B's own certified list when one is passed with `--certified` — and prints the read-outs
and the gauges beside every count, never inside one. A field with no `certified_candidate` is
not certified, so a criteria file that omits the key carries no arm difference anywhere and the
counts file says so.

**The corpus-affordance table** (W11 decision D4) names, for every cross-step field the corpus
records, which of the eight arms documents afford it; P4.2 and P4.3 are read over the fields at
least one affords, and over every cross-step field the table does not name. A field the corpus
records neither way is not named in the table at all (fault 28 of the fix round's review), so
the rule two paragraphs below reaches it: found nowhere means unknown.
`marks.affordance()` looks for it in the criteria file's `corpus_affordance`,
`cross_step_affordance`, `affordance` or `what_the_corpus_affords` key, then at
`<rig>/instrument/affordance.json`, `corpus_affordance.json`, `cross_step_affordance.json`.
Either shape is read:

```
{"fields": {"test_flip": ["W8","W9"], "test_patches": []}}
{"fields": [ {"field": "test_flip", "affords": ["W8","W9"]}, ... ]}
```

A field the table does not name is read, not excluded: "found nowhere means unknown". A field
the table names with no arms document is left out of P4.2 and P4.3, and the counts file says
which and why.

What each kind means for agreement is in `marks.py`: enum, int and bool agree when equal; a set
agrees when the sets are equal; a map_enum agrees when the whole map is equal; text is never
compared and is kept so a disagreement can be traced. A field where either marker left no value
is reported unreadable, never as agreement.

A marks file, which is what a marker returns and what `agreement.py` reads:

```
{ "marker": "first" | "second" | a name, "criteria_version": ..., "reader": "deepseek" | "sonnet",
  "marks": { "<run id>": { "<field name>": value, ... }, ... } }
```
