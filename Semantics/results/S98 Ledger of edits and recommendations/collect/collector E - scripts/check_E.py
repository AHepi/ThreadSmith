"""Checks of collector E.jsonl (log S98). Reads only; prints a report.

1. Shape: 16 fields in order, rids unique, every same_as names an existing rid (in E or in collectors A-D).
2. Every non-empty "old" is found verbatim in its target text (all records; "applied" ones are reported apart).
3. Every non-empty old_sentence is found verbatim in its target text.
4. For each record with wording, whether its new wording (or the words it adds) is in the latest text, the
   repaired copy or the scrubbed copy, and whether another collector holds a record with the same "new".
"""
import difflib, glob, json, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *  # noqa

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = ["rid", "round", "source_file", "source_ref", "kind", "status", "applied_in", "target_text",
          "target_line", "target_part", "old", "new", "old_sentence", "new_sentence", "scope", "same_as"]
recs = [json.loads(l) for l in open(os.path.join(HERE, "collector E.jsonl"), encoding="utf-8")]
other = {}
for fn in sorted(glob.glob(os.path.join(HERE, "collector [A-D].jsonl"))):
    for l in open(fn, encoding="utf-8"):
        r = json.loads(l)
        other[r["rid"]] = r

texts = {}
for n in TEXTS:
    try:
        texts[TEXTS[n][2]] = "\n".join(load(n))
    except SystemExit as e:
        print("TEXT NOT LOADED", n, e)
later = {n: "\n".join(load(n)) for n in ["latest text", "repaired copy", "scrubbed copy"]}

# 1
bad = [r["rid"] for r in recs if list(r.keys()) != FIELDS]
rids = [r["rid"] for r in recs]
dup = sorted({x for x in rids if rids.count(x) > 1})
known = set(rids) | set(other)
dangling = [(r["rid"], s) for r in recs for s in r["same_as"] if s not in known]
print("1. records %d; field-order misses %s; duplicate rids %s; dangling same_as %s" % (len(recs), bad, dup, dangling))

# 2 and 3
miss_old, miss_os, checked_old, checked_os, applied_checked = [], [], 0, 0, 0
for r in recs:
    t = texts.get(r["target_text"])
    if t is None:
        continue  # declarations: the note of file 13 (no such text on disk)
    if r["old"]:
        checked_old += 1
        if r["status"] == "applied":
            applied_checked += 1
        if r["old"] not in t:
            miss_old.append(r["rid"])
    if r["old_sentence"]:
        checked_os += 1
        if r["old_sentence"] not in t:
            miss_os.append(r["rid"])
print("2. 'old' checked in its target text: %d (of them recorded as applied: %d); misses: %s" % (checked_old, applied_checked, miss_old))
print("3. 'old_sentence' checked in its target text: %d; misses: %s" % (checked_os, miss_os))
nodisk = [r["rid"] for r in recs if r["target_text"] not in texts]
print("   records whose target text is not a file on disk (declarations for the note of file 13):", nodisk)


def added_part(old, new):
    """The longest run of words new adds to old (for a span change), or new itself."""
    if not old:
        return new
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    best = ""
    for tag, a1, a2, b1, b2 in sm.get_opcodes():
        if tag in ("insert", "replace") and b2 - b1 > len(best):
            best = new[b1:b2]
    return best.strip()


# 4
print("4. the new wording in the later texts, and identical 'new' in collectors A-D:")
for r in recs:
    new = r["new"]
    if not new or new.startswith("[no wording given]"):
        continue
    hits = [n for n, t in later.items() if new in t]
    add = added_part(r["old"], new)
    hits_add = [n for n, t in later.items() if len(add) >= 12 and add in t]
    same_new = sorted(k for k, o in other.items() if o["new"] == new)
    if hits or hits_add or same_new:
        print("   %s: whole new in %s; added words %r in %s; same 'new' in %s" % (r["rid"], hits, add[:60], hits_add, same_new))
print("   (records not listed: no hit)")

# 5
miss_src = []
for r in recs:
    if not r["new"] or r["new"].startswith("[no wording given]"):
        continue
    raw, _ = read(r["source_file"])
    if r["new"] not in raw and r["new"] not in unquote_block(raw):
        miss_src.append(r["rid"])
print("5. every 'new' with wording found verbatim in its source file (after removing blockquote markers where the source quotes it): misses %s" % miss_src)
import collections
print("6. counts by kind and status:", dict(collections.Counter((r["kind"], r["status"]) for r in recs)))
print("   by round:", dict(collections.Counter(r["round"] for r in recs)), " by scope:", dict(collections.Counter(r["scope"] for r in recs)))
print("   [no wording given]:", [r["rid"] for r in recs if r["new"].startswith("[no wording given]")])
