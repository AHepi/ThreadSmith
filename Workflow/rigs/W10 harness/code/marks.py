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
from rig import CRITERIA, read_json

COMPARABLE = {"enum", "map_enum", "set", "int", "bool"}


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


def fields(c, sort=None, comparable_only=False):
    out = c["fields"]
    if sort:
        out = [f for f in out if f["sort"] == sort]
    if comparable_only:
        out = [f for f in out if f["kind"] in COMPARABLE]
    return out


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
