"""Collector D, part 2: the S95 vocabulary as term records.

tests/S95 Scrub - vocabulary, as used.md      -> kind edit, scope term (the words the scrubbed copy uses)
tests/S95 Scrub - vocabulary, proposed.md     -> kind recommendation, scope term
tests/S95 Scrub - vocabulary, sceptic's rulings.md -> kind recommendation (CHANGE / OWNER rows, and
                                                   section 3's occurrences), scope term
Cells are copied verbatim; the 'why' columns are not copied.
"""
import re
from lib import *

USED = "tests/S95 Scrub - vocabulary, as used.md"
PROP = "tests/S95 Scrub - vocabulary, proposed.md"
SCEP = "tests/S95 Scrub - vocabulary, sceptic's rulings.md"

# proposal row (file line) -> sceptic row number (section 2), read by hand from both tables
P2S = {29: 1, 30: 2, 31: 3, 32: 4, 33: 4, 34: 5, 35: 6, 36: 7, 37: 8, 38: 9, 39: 10, 40: 11, 41: 12,
       47: 13, 48: 14, 49: 15, 50: 16, 51: 16, 52: 17, 53: 18, 54: 19, 55: 20, 56: 20, 57: 21, 58: 22,
       59: 23, 60: 24, 66: 25, 67: 26, 68: 27, 69: 28, 70: 27, 71: 52, 72: 52, 73: 29, 74: 29, 75: 30,
       76: 29, 77: 29, 83: 31, 84: 31, 85: 32, 86: 32, 87: 32, 88: 32, 89: 32, 90: 33, 91: 33, 92: 33,
       93: 33, 94: 34, 95: 35, 96: 36, 97: 36, 98: 36, 104: 37, 105: 37, 106: 37, 107: 37, 108: 37,
       109: 38, 110: 38, 111: 38, 112: 37, 113: 38, 114: 39, 115: 40, 116: 40, 117: 40, 118: 40,
       119: 40, 120: 40, 121: 40, 122: 40, 123: 40, 124: 40, 130: 41, 131: 42, 132: 43, 133: 43,
       134: 44, 135: 45, 136: 45, 137: 46, 143: 47, 144: 47, 145: 48, 146: 49, 147: 49, 148: 49,
       149: 49, 150: 49, 151: 49, 152: 50, 153: 51, 154: None}
# as-used marks "differs from the sceptic" / "differs from the proposal" on these
PROP_STATUS_OVERRIDE = {149: "declined"}          # as used differs from proposal and sceptic (elegance)
SCEP_STATUS_OVERRIDE = {8: "declined"}            # as used differs from the sceptic at l. 317
# section 3 rows whose quoted words are in the scrubbed copy with other markup or adapted (read by eye)
SCEP3_STATUS_OVERRIDE = {101: "applied", 116: "applied", 118: "applied"}


def table_rows(path):
    out = []
    sec = ""
    for i, l in enumerate(open(SEM + path, encoding="utf-8").read().split("\n"), 1):
        if l.startswith("#"):
            sec = l.lstrip("#").strip()
        if l.startswith("|") and not re.match(r"^\|[-| ]+\|$", l):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", l.strip())[1:-1]]
            out.append((i, sec, cells))
    return out


def line_refs(s):
    """Line numbers named in a cell: 'l. 13, 598', 'l. 285–313' (range ends only), or a bare list."""
    nums = []
    for m in re.finditer(r"\bl\.\s*([\d,\s–-]+)", s):
        for part in re.split(r",\s*", m.group(1)):
            part = part.strip()
            mm = re.match(r"^(\d+)(?:[–-](\d+))?$", part)
            if mm:
                nums.append(int(mm.group(1)))
                if mm.group(2):
                    nums.append(int(mm.group(2)))
    return sorted(set(n for n in nums if 1 <= n <= 632))


def place(H, nums):
    if len(nums) == 1:
        return nums[0], H[nums[0]]
    if not nums:
        return None, "whole text (term; no line named)"
    parts = []
    for n in nums:
        p = H[n].split(" / ")[0]
        if p not in parts:
            parts.append(p)
    return None, "several places: " + "; ".join(parts) + " (l. " + ", ".join(map(str, nums)) + ")"


def base(rid, src, ref, kind, status, applied_in, tline, tpart, old, new, os_="", ns_=""):
    return {"rid": rid, "round": "S95", "source_file": src, "source_ref": ref, "kind": kind,
            "status": status, "applied_in": applied_in, "target_text": "draft 5", "target_line": tline,
            "target_part": tpart, "old": old, "new": new, "old_sentence": os_, "new_sentence": ns_,
            "scope": "term", "same_as": []}


def norm(s):
    s = re.sub(r"\\[()\[\]]", "", s)
    s = re.sub(r"\\(operatorname|mathsf|mathcal|mathfrak|mathrm)\{([^}]*)\}", r"\2", s)
    s = s.replace("\\", "").replace("*", "").replace("{", "").replace("}", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def quoted(s):
    out = []
    for q in re.findall(r"\"([^\"]{4,})\"", s):
        out += [norm(x) for x in re.split(r"\u2026|\.\.\.", q) if len(norm(x)) >= 4]
    return out


def build(next_rid, prior, texts):
    d5 = texts["draft 5"]
    sc = texts["scrubbed copy"]
    H = headings(d5)
    recs = []
    # as used
    for i, sec, c in table_rows(USED):
        if c[0] == "draft 5":
            continue
        nums = line_refs(c[0] + " " + c[1])
        tl, tp = place(H, nums)
        st = "not applied" if re.match(r"^kept(, BORDERLINE| BORDERLINE)", c[1]) else "applied"
        os_ = ns_ = ""
        if tl:
            os_, ns_ = d5[tl - 1].strip(), sc[tl - 1].strip()
            if len(os_) > 600:         # a long line: leave the sentence to the per-occurrence edits
                os_ = ns_ = ""
        r = base(next_rid(), USED, "table row at file line %d (section: %s)" % (i, sec), "edit", st,
                 "scrubbed copy" if st == "applied" else "none (word kept)", tl, tp, c[0], c[1], os_, ns_)
        r["_key"] = ("used", i)
        recs.append(r)
    # sceptic section 2 and 3
    scep_rid = {}
    for i, sec, c in table_rows(SCEP):
        if len(c) == 5 and c[0] not in ("#",):
            n, pair, ruling, words = c[0], c[1], c[2], c[3]
            if ruling == "KEEP" and not words:
                continue
            if ruling == "KEEP":
                # a KEEP with an added note: the note's wording is its own recommendation
                old, new = pair, words
            else:
                old = pair.split(" → ")[0] if " → " in pair else pair
                new = words
            st = {"CHANGE": "applied", "OWNER": "open for the owner", "KEEP": "applied"}[ruling]
            st = SCEP_STATUS_OVERRIDE.get(int(n), st)
            nums = line_refs(pair + " " + words)
            tl, tp = place(H, nums)
            r = base(next_rid(), SCEP, "section 2, row %s (%s), file line %d" % (n, ruling, i), "recommendation",
                     st, "scrubbed copy" if st == "applied" else ("scrubbed copy (provisional name)" if ruling == "OWNER" else "none"),
                     tl, tp, old, new)
            r["_key"] = ("scep", int(n))
            scep_rid[int(n)] = r["rid"]
            recs.append(r)
        elif len(c) == 3 and c[0] not in ("line",) and re.match(r"^[\d, –-]+$", c[0]):
            nums = [int(x) for x in re.findall(r"\d+", c[0]) if 1 <= int(x) <= 632]
            tl, tp = place(H, nums)
            qs = quoted(c[2])
            hits = [q for q in qs if any(q in norm(sc[n - 1]) for n in (nums or range(1, 633)))]
            if qs and not hits:
                st = "declined"
            else:
                st = "applied"
            st = SCEP3_STATUS_OVERRIDE.get(i, st)
            os_ = ns_ = ""
            if tl and len(d5[tl - 1]) <= 600:
                os_, ns_ = d5[tl - 1].strip(), sc[tl - 1].strip()
            r = base(next_rid(), SCEP, "section 3 (%s), row at file line %d" % (sec, i), "recommendation", st,
                     "scrubbed copy" if st == "applied" else "none", tl, tp, c[1], c[2], os_, ns_)
            r["_key"] = ("scep3", i)
            recs.append(r)
    # proposal
    for i, sec, c in table_rows(PROP):
        if c[0] == "draft 5" or len(c) != 3:
            continue
        s = P2S.get(i)
        ruling = None
        for r0 in recs:
            if r0.get("_key") == ("scep", s):
                ruling = r0["source_ref"].split("(")[1].split(")")[0]
        if s is None:
            st = "applied"            # 'advanceable challenges': kept, as proposed
        elif ruling is None:
            st = "applied"            # sceptic KEEP with no added words
        elif ruling == "CHANGE":
            st = "superseded"
        elif ruling == "OWNER":
            st = "open for the owner"
        else:
            st = "applied"
        st = PROP_STATUS_OVERRIDE.get(i, st)
        nums = line_refs(c[0] + " " + c[1])
        tl, tp = place(H, nums)
        r = base(next_rid(), PROP, "section %s, table row at file line %d%s" % (
            sec.split(" ")[0], i, "; sceptic's row %s" % s if s else ""), "recommendation", st,
            "scrubbed copy" if st == "applied" else ("scrubbed copy (provisional name)" if st == "open for the owner" else "none"),
            tl, tp, c[0], c[1])
        if s in scep_rid:
            r["same_as"].append(scep_rid[s])
        r["_key"] = ("prop", i)
        recs.append(r)
    return recs
