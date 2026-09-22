"""The criteria file, read; and what counts as agreement on a field.

A RULE, shared by first_marker.py, second_marker.py and agreement.py.

The criteria file is A4's, frozen before any report is read, at <rig>/instrument/criteria.json.
A1 wrote code against a schema before that file existed; the schema is set out in
CRITERIA-SCHEMA.md and an example of it is fixtures/criteria.example.json. If A4's file has a
different shape, this file is where it is changed, and nothing else changes.

Field kinds, and what agreement means for each:
  enum      one value from `values`      agree: the same value
  map_enum  {part number: value}         agree: the same map (same keys, same values)
  set       a list, read as a set        agree: the same set
  int       a whole number               agree: the same number
  bool      true or false                agree: the same
  text      free text                    never compared; kept so a disagreement can be traced
"""
import os, json
import rig
from rig import CRITERIA, read_json

COMPARABLE = {"enum", "map_enum", "set", "int", "bool"}

# W11 decision D4 (fault 18 of the stage-A review): the cross-step set is read over the fields
# at least one of the eight arms documents affords. A4 writes the table before stage B. This
# rig reads it from, in order: a key of the criteria file, then a file of its own beside it.
# Where none is there, the affordance is unknown, every certified cross-step field is read, and
# the counts file says so by name rather than passing silently.
AFFORDANCE_KEYS = ["corpus_affordance", "cross_step_affordance", "affordance",
                   "what_the_corpus_affords"]
AFFORDANCE_FILES = [os.path.join(rig.RIG, "instrument", "affordance.json"),
                    os.path.join(rig.RIG, "instrument", "corpus_affordance.json"),
                    os.path.join(rig.RIG, "instrument", "cross_step_affordance.json")]


def load(path=None):
    p = path or CRITERIA
    if not os.path.exists(p):
        raise SystemExit(f"no criteria file at {p}. A4 of stage A writes it, frozen before any "
                         f"report is read. Pass --criteria to point somewhere else. Nothing marked.")
    c = read_json(p)
    for f in c.get("fields", []):
        for k in ("name", "kind", "per", "sort", "criterion"):
            if k not in f:
                raise SystemExit(f"criteria field {f.get('name')!r} has no {k!r}")
        if f["kind"] in ("enum", "map_enum") and not f.get("values"):
            raise SystemExit(f"criteria field {f['name']!r} is {f['kind']} with no values")
        if f["sort"] not in ("within-step", "cross-step"):
            raise SystemExit(f"criteria field {f['name']!r}: sort must be within-step or cross-step "
                             f"(W8 part B4); got {f['sort']!r}")
    return c


def fields(c, sort=None, comparable_only=False, certified_only=False, certified=None):
    """The criteria's fields, filtered.

    certified_only is the filter fault 1 of the stage-A review forced. criteria.json's own
    words: "certified_candidate: true when stage B can certify the field on the 96 reports in
    hand. P4.1 to P4.5 are read over certified fields only. false fields are read-outs and
    gauges and carry no arm difference." Without it P4.4 could be carried by
    marks_outside_closed_list alone, which goes to zero under arm (e) by construction.

    `certified` is stage B's own list of the fields that agreed there, where one has been
    supplied: W10 stage B, "No field carries an arm difference in stage C unless it agreed
    here." With none supplied the filter is certified_candidate alone, and the caller says so."""
    out = c["fields"]
    if sort:
        out = [f for f in out if f["sort"] == sort]
    if comparable_only:
        out = [f for f in out if f["kind"] in COMPARABLE]
    if certified_only:
        out = [f for f in out if f.get("certified_candidate") is True]
        if certified is not None:
            keep = set(certified)
            out = [f for f in out if f["name"] in keep]
    return out


def read_outs(c, comparable_only=True):
    """The fields a count is never read over: the read-outs and the gauges. They are printed
    beside every count and never inside one."""
    out = [f for f in c["fields"] if f.get("certified_candidate") is not True]
    if comparable_only:
        out = [f for f in out if f["kind"] in COMPARABLE]
    return out


AFFORDS_KEYS = ["affords", "documents", "arms_documents", "afforded_by"]

# Fault 28 of the stage-A review (round 3): a cross-step field the corpus records NEITHER WAY
# must be read, not excluded, and the counts file must say which of the two moves the instrument
# made - the table stopped naming such a field, or this reader learned to read a row's status.
# A4's table carries one sentence saying which. It is passed through to `where`, which the counts
# file already prints beside every exclusion. It is data, not a rule: no count, no exclusion and
# no field list depends on it.
NOTE_KEYS = ["note_to_the_counts_file", "counts_file_note"]


def _table_note(d):
    """The table's own one sentence to the counts file, or None."""
    if isinstance(d, dict):
        for k in NOTE_KEYS:
            v = d.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
    return None


def _where(src, note):
    return src if not note else f"{src} | the table's own note: {note}"


def _affordance_table(d):
    """Normalise A4's table to {field name: [arms document ids]}. Two shapes are read: an
    object of field name to a list of ids, and a list of rows carrying a field name and a list
    of ids. A field the table does not name is not in the returned map, and is read: A4's own
    rule, "'Found nowhere means unknown': a gap in the corpus's record is not a finding that the
    documents afford nothing.\""""
    got = d.get("fields") if isinstance(d, dict) and "fields" in d else d
    out = {}
    if isinstance(got, dict):
        for k, v in got.items():
            if isinstance(v, (list, tuple)):
                out[k] = list(v)
            elif isinstance(v, dict):
                for kk in AFFORDS_KEYS:
                    if isinstance(v.get(kk), (list, tuple)):
                        out[k] = list(v[kk])
                        break
    elif isinstance(got, list):
        for row in got:
            if not isinstance(row, dict):
                continue
            name = row.get("field") or row.get("name")
            for kk in AFFORDS_KEYS:
                if name and isinstance(row.get(kk), (list, tuple)):
                    out[name] = list(row[kk])
                    break
    return out or None


def affordance(c, path=None):
    """W11 D4's table: {field name: [arms document ids that afford it]}, and where it came from.

    Returns (table_or_None, where). `where` is the path or key it was read from, or, when there
    is none, the sentence naming every place looked at, which the counts file prints. Where the
    table carries a note to the counts file, it is appended to `where` word for word (fault 28)."""
    for k in AFFORDANCE_KEYS:
        src = c.get(k)
        got = _affordance_table(src) if isinstance(src, (dict, list)) else None
        if got:
            return got, _where(f"the criteria file's {k!r} key", _table_note(src))
    for p in ([path] if path else []) + AFFORDANCE_FILES:
        if p and os.path.exists(p):
            src = read_json(p, "the corpus-affordance table (A4 writes it, W11 D4)")
            got = _affordance_table(src)
            if got:
                return got, _where(p, _table_note(src))
    looked = ", ".join([f"the criteria file's keys {AFFORDANCE_KEYS}"] + AFFORDANCE_FILES)
    return None, ("no corpus-affordance table found; looked at " + looked)


def normalise(field, value):
    k = field["kind"]
    if value is None:
        return None
    if k == "set":
        return tuple(sorted(str(x) for x in value))
    if k == "map_enum":
        return tuple(sorted((str(a), str(b)) for a, b in dict(value).items()))
    if k == "int":
        return int(value)
    if k == "bool":
        return bool(value)
    return str(value)


def same(field, a, b):
    """Agreement on one field between two marks. Two missing values do not agree:
    'found nowhere means unknown' (testing-against-cases.md), so a pair with a missing
    value is reported as unreadable, never as agreement."""
    na, nb = normalise(field, a), normalise(field, b)
    if na is None or nb is None:
        return None
    return na == nb


def check_value(field, value):
    """Return a complaint, or None. The closed list is closed."""
    k = field["kind"]
    if value is None:
        return "missing"
    if k == "enum" and str(value) not in field["values"]:
        return f"{value!r} is not one of {field['values']}"
    if k == "map_enum":
        if not isinstance(value, dict):
            return "should be an object of part number to value"
        bad = [f"{p}={v}" for p, v in value.items() if str(v) not in field["values"]]
        if bad:
            return f"outside the closed list: {bad}"
    if k == "set" and not isinstance(value, list):
        return "should be a list"
    if k == "int" and not isinstance(value, int):
        return "should be a whole number"
    return None
