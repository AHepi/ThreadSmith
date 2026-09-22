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
    } ]
}
```

What each kind means for agreement is in `marks.py`: enum, int and bool agree when equal; a set
agrees when the sets are equal; a map_enum agrees when the whole map is equal; text is never
compared and is kept so a disagreement can be traced. A field where either marker left no value
is reported unreadable, never as agreement.

A marks file, which is what a marker returns and what `agreement.py` reads:

```
{ "marker": "first" | "second" | a name, "criteria_version": ..., "reader": "deepseek" | "sonnet",
  "marks": { "<run id>": { "<field name>": value, ... }, ... } }
```
