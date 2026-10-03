#!/usr/bin/env python3
"""Tabulation helpers: the mechanical half of tabulating the replies (extraction, never ruling).

Subcommands (each prints one JSON object):
  items   --brief BRIEF                         the items of a part, from its brief, in order
  blocks  --reply REPLY --prefix G12            the fenced proposal blocks of a reply, numbered in order
                                                (G12-B1, G12-B2, ...), with their reply lines (fence to fence), their
                                                text byte for byte, and the text lines their first line names
  quote   --text TEXT --q "..." [--q ...]       where each quotation stands in the text (normalized; " … " joins
                                                fragments that must stand in one line)
  sheet   --brief B --reply R:PREFIX:READER ... the work sheet a Sonnet agent fills: items, blocks, empty rows;
                                                with --prefill, the rows the program can fill from the replies'
                                                bold headers (passages, blocks, 'nothing to add'), 'said' left empty
  check   --extraction X.json --brief B --text T --reply R:PREFIX:READER ...
                                                checks a filled sheet: every (item, reader) row once, known ids,
                                                reply lines inside the reply, block ids real, lines named by the
                                                block, copied wordings equal to the block byte for byte
  fill    --extraction X.json --reply R:PREFIX:READER ... --out Y.json
                                                writes each row's wordings from the blocks by program (the copy
                                                Sonnet is never trusted with), and each quotation's lines
  opus    --tabulation TAB.md --part 12         reads a tabulation written by Opus (round 2's form) into rows
  compare --extraction X.json --tabulation TAB.md --part 12 --reply R:PREFIX:READER ...
                                                compares a filled sheet with Opus's rows: items found and missed,
                                                challenge marks, blocks, lines, reply passages, wordings exact or not

"said" takes one of: challenges | does not challenge | nothing to add | no point. Whether a point challenges is
marked by the list of rule 5 of the round's reading rule; in doubt, "challenges". That mark is the one part of the
job that is not pure copying; Opus checks every row not marked "challenges" (README).
"""
import argparse
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402

SAID = ("challenges", "does not challenge", "nothing to add", "no point")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


# ------------------------------------------------------------------ items of a part, from its brief
ITEM_RX = [
    (re.compile(r"^\*\*(D\d+\.\d+)[ .*]"), "definition"),
    (re.compile(r"^\*\*(E\d+)[ .*]"), "encoding"),
    (re.compile(r"^### (FC[\w.]+) ·"), "claim"),
    (re.compile(r"^### (I\d+) ·"), "invention"),
    (re.compile(r"^### (H\d+) ·"), "H-entry"),
    (re.compile(r"^### (U\d+) ·"), "U-entry"),
    (re.compile(r"^\*\*(NF\d+)\*\*"), "NF entry"),
    (re.compile(r"^\*\*Round-1 matter (\d+)\.\*\*"), "round-1 matter"),
    (re.compile(r"^\*\*The round-1 change at (L\d+)\.\*\*"), "round-1 change"),
]


def items_of(brief_text):
    out, seen = [], set()
    for n, l in enumerate(brief_text.split("\n"), 1):
        for rx, kind in ITEM_RX:
            m = rx.match(l)
            if m:
                iid = ("matter " + m.group(1)) if kind == "round-1 matter" else m.group(1)
                if iid not in seen:
                    seen.add(iid)
                    out.append(dict(id=iid, kind=kind, brief_line=n))
                break
    return out


# ------------------------------------------------------------------ fenced blocks of a reply
def blocks_of(reply_text, prefix):
    lines = reply_text.split("\n")
    out, open_at, n = [], None, 0
    for i, l in enumerate(lines, 1):
        if FENCE.match(l):
            if open_at is None:
                open_at = i
            else:
                n += 1
                body = lines[open_at:i - 1]
                first = body[0] if body else ""
                out.append(dict(id="%s-B%d" % (prefix, n), reply_lines=[open_at, i], text="\n".join(body),
                                lines_named_first_line=[int(x) for x in re.findall(r"\bL(\d{1,4})\b", first)]))
                open_at = None
    return out, (open_at is not None)


# ------------------------------------------------------------------ quotations
GREEK = {"alpha": "α", "beta": "β", "gamma": "γ", "Gamma": "Γ", "delta": "δ", "Delta": "Δ", "epsilon": "ε",
         "varepsilon": "ε", "zeta": "ζ", "eta": "η", "theta": "θ", "Theta": "Θ", "kappa": "κ", "lambda": "λ",
         "Lambda": "Λ", "mu": "μ", "nu": "ν", "xi": "ξ", "Xi": "Ξ", "pi": "π", "Pi": "Π", "rho": "ρ", "sigma": "σ",
         "Sigma": "Σ", "tau": "τ", "phi": "φ", "varphi": "φ", "Phi": "Φ", "chi": "χ", "psi": "ψ", "Psi": "Ψ",
         "omega": "ω", "Omega": "Ω", "land": "∧", "wedge": "∧", "lor": "∨", "vee": "∨", "neg": "¬", "lnot": "¬",
         "Rightarrow": "⇒", "rightarrow": "→", "to": "→", "Leftrightarrow": "⇔", "iff": "⇔", "neq": "≠", "ne": "≠",
         "in": "∈", "notin": "∉", "subseteq": "⊆", "subset": "⊂", "supseteq": "⊇", "emptyset": "∅",
         "varnothing": "∅", "bot": "⊥", "top": "⊤", "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "times": "×",
         "cup": "∪", "cap": "∩", "forall": "∀", "exists": "∃", "circ": "∘", "prime": "′", "ldots": "…",
         "dots": "…", "cdots": "…", "mid": "|"}
MATHCAL = {"E": "ℰ", "T": "𝒯", "N": "𝒩", "V": "𝒱", "C": "𝒞", "A": "𝒜", "R": "ℛ", "S": "𝒮", "P": "𝒫"}


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\\mathcal\s*\{?\s*([A-Za-z])\s*\}?", lambda m: MATHCAL.get(m.group(1), m.group(1)), s)
    s = re.sub(r"\\(operatorname|mathrm|mathbf|mathit|text|textit|textbf|mathsf)\s*\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\\([A-Za-z]+)", lambda m: GREEK.get(m.group(1), ""), s)
    s = s.replace("\\(", " ").replace("\\)", " ").replace("\\[", " ").replace("\\]", " ")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("...", "…"),
                 ("𝓔", "ℰ")):
        s = s.replace(a, b)
    s = re.sub(r"[{}\\*_^`$]", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([(),;:.|'\"∧∨¬⇒→=≠∈⊆])\s*", r"\1", s)
    return s.strip().lower()


def quote_lines(q, text_lines, normed=None):
    normed = normed or [norm(l) for l in text_lines]
    frags = [f for f in (x.strip(" .,;:") for x in norm(q).split("…")) if f]
    if not frags:
        return []
    return [i for i, l in enumerate(normed, 1) if all(f in l for f in frags)]


# ------------------------------------------------------------------ replies given as PATH:PREFIX:READER
def parse_replies(specs):
    out = []
    for s in specs:
        parts = s.rsplit(":", 2)
        if len(parts) != 3:
            H.refuse("a reply is given as PATH:PREFIX:READER, e.g. '<file>:G12:GLM'")
        path, prefix, reader = parts
        text = H.read_text(path)
        blocks, unclosed = blocks_of(text, prefix)
        out.append(dict(path=path, prefix=prefix, reader=reader, text=text, n_lines=len(text.split("\n")),
                        blocks=blocks, unclosed_fence=unclosed))
    return out


def ranges(x):
    """[[a,b], ...] or [a, b] or 'a-b' -> list of (a, b)."""
    if isinstance(x, str):
        return [tuple(int(v) for v in (p.split("-") * 2)[:2]) for p in re.findall(r"\d+(?:-\d+)?", x.replace("–", "-"))]
    if x and all(isinstance(v, int) for v in x):
        return [(x[0], x[-1])]
    return [(int(r[0]), int(r[-1])) for r in (x or [])]


def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


# ------------------------------------------------------------------ the sheet Sonnet fills
def sheet(brief, replies, with_blocks=True):
    """with_blocks=False gives the bare sheet (no block table): the agent must find, number and copy the blocks
    itself; used to measure what the block table fixes."""
    items = items_of(H.read_text(brief))
    readers = []
    for r in replies:
        d = dict(reader=r["reader"], block_prefix=r["prefix"], reply=H.rel(r["path"]), reply_lines=r["n_lines"])
        if with_blocks:
            d["blocks"] = [dict(id=b["id"], reply_lines=b["reply_lines"], lines_named=b["lines_named_first_line"],
                                first_words=b["text"][:90]) for b in r["blocks"]]
        readers.append(d)
    row = lambda it, r: dict(item=it["id"], reader=r["reader"], said=None, reply_lines=[], blocks=[], lines_to_change=[],
                             **({} if with_blocks else dict(wordings=[])))
    return dict(
        what="Fill 'rows': one row for every item and every reader, in this order. Copy; do not rule.",
        said_values=list(SAID), items=items, readers=readers, rows=[row(it, r) for it in items for r in replies])


# ------------------------------------------------------------------ the program's first pass over the rows
ID_RX = re.compile(r"\b(D\d+\.\d+|E\d+|FC[\w]+(?:\.new\d+)?|I\d+|H\d+|U\d+|NF\d+|[Mm]atter \d+|L\d+)\b")
HEADER = re.compile(r"^\*\*(.+?)\*\*")
NOTHING = re.compile(r"^\*?nothing to add:?\*?:?\s*(.*)$", re.I)
SECTION = re.compile(r"^#{1,3} ")


def _ids(txt, order):
    """Item ids named in txt, with ranges such as D9.1–D9.4 expanded by the brief's order."""
    out = []
    for m in re.finditer(r"(D\d+\.\d+)\s*[–-]\s*(D\d+\.\d+)", txt):
        a, b = m.group(1), m.group(2)
        if a in order and b in order:
            out += order[order.index(a):order.index(b) + 1]
    for m in ID_RX.finditer(txt):
        t = m.group(1)
        t = "matter " + t.split()[1] if t.lower().startswith("matter") else t
        if t in order and t not in out:
            out.append(t)
    return out


def passages(reply, order):
    """Split a reply into passages: a bold header naming items, to the last non-blank line before the next header,
    'nothing to add' line or section heading. Returns [{items, lines: [a, b], nothing_to_add, text}]."""
    lines = reply["text"].split("\n")
    starts = []
    for i, l in enumerate(lines, 1):
        h = HEADER.match(l)
        n = NOTHING.match(l.strip())
        if SECTION.match(l):
            starts.append((i, None, False))
        elif n:
            starts.append((i, _ids(n.group(1), order), True))
        elif h and _ids(h.group(1), order):
            starts.append((i, _ids(h.group(1), order), False))
    out = []
    for k, (i, ids, nothing) in enumerate(starts):
        if ids is None:
            continue
        end = (starts[k + 1][0] - 1) if k + 1 < len(starts) else len(lines)
        if nothing:
            end = i
        while end > i and not lines[end - 1].strip():
            end -= 1
        out.append(dict(items=ids, lines=[i, end], nothing_to_add=nothing, text="\n".join(lines[i - 1:end])))
    return out


def prefill(sh, replies):
    """Fill what a program can: each row's passages (from the headers that name the item), the blocks inside them,
    the blocks a passage points to with 'under <item>', and 'nothing to add' where the item is only listed so.
    Leaves 'said' empty (null) wherever the reader says something: that mark is the agent's."""
    order = [it["id"] for it in sh["items"]]
    by = {}
    for r in replies:
        ps = passages(r, order)
        for p in ps:
            p["blocks"] = [b["id"] for b in r["blocks"] if p["lines"][0] <= b["reply_lines"][0] <= p["lines"][1]]
        for it in order:
            mine = [p for p in ps if it in p["items"]]
            rl = [p["lines"] for p in mine]
            blocks = [b for p in mine for b in p["blocks"]]
            for p in mine:
                for m in re.finditer(r"\bunder (?:the )?(?:wording under )?(D\d+\.\d+|FC\w+|I\d+|H\d+|U\d+|[Mm]atter \d+)", p["text"]):
                    tgt = m.group(1)
                    tgt = "matter " + tgt.split()[1] if tgt.lower().startswith("matter") else tgt
                    blocks += [b for q in ps if tgt in q["items"] for b in q["blocks"]]
            blocks = list(dict.fromkeys(blocks))
            said = None
            if not mine:
                said = "no point"
            elif all(p["nothing_to_add"] for p in mine):
                said = "nothing to add"
            named = sorted({ln for b in r["blocks"] if b["id"] in blocks for ln in b["lines_named_first_line"]})
            by[(it, r["reader"])] = dict(said=said, reply_lines=rl, blocks=blocks, lines_to_change=named, prefilled=True)
    for row in sh["rows"]:
        row.update(by.get((row["item"], row["reader"]), {}))
    return sh


# ------------------------------------------------------------------ checking a filled sheet
def check(ext, brief, text_path, replies, lines_by_program=False):
    items = [x["id"] for x in items_of(H.read_text(brief))]
    text_lines = H.read_text(text_path).split("\n")
    rd = {r["reader"]: r for r in replies}
    bl = {b["id"]: (r, b) for r in replies for b in r["blocks"]}
    probs, seen = [], {}
    for k, row in enumerate(ext.get("rows", [])):
        key = (row.get("item"), row.get("reader"))
        where = "row %d (%s, %s)" % (k + 1, key[0], key[1])
        if key[0] not in items:
            probs.append(where + ": item not in the part's brief")
        if key[1] not in rd:
            probs.append(where + ": reader unknown")
            continue
        if key in seen:
            probs.append(where + ": a second row for this item and reader")
        seen[key] = row
        if row.get("said") not in SAID:
            probs.append(where + ": 'said' is %r" % row.get("said"))
        rr = ranges(row.get("reply_lines"))
        if row.get("said") in ("challenges", "does not challenge", "nothing to add") and not rr:
            probs.append(where + ": no reply lines for a point")
        if row.get("said") == "no point" and (rr or row.get("blocks")):
            probs.append(where + ": 'no point' with reply lines or blocks")
        for a, b in rr:
            if not (1 <= a <= b <= rd[key[1]]["n_lines"]):
                probs.append(where + ": reply lines %d-%d outside the reply (1-%d)" % (a, b, rd[key[1]]["n_lines"]))
        for bid in row.get("blocks", []):
            if bid not in bl:
                probs.append(where + ": block %s does not exist" % bid)
            elif bl[bid][0]["reader"] != key[1]:
                probs.append(where + ": block %s is another reader's" % bid)
        named = sorted({ln for bid in row.get("blocks", []) if bid in bl for ln in bl[bid][1]["lines_named_first_line"]})
        ltc = sorted(set(row.get("lines_to_change", [])))
        for ln in ltc:
            if not (1 <= ln <= len(text_lines)):
                probs.append(where + ": L%d is not a line of the text" % ln)
        if named and ltc != named and not lines_by_program:
            probs.append(where + ": lines_to_change %s, but its blocks name %s" % (ltc, named))
        for w in row.get("wordings", []):
            if w.get("block") not in bl:
                probs.append(where + ": wording for unknown block %s" % w.get("block"))
            elif w.get("text", "").encode("utf-8") != bl[w["block"]][1]["text"].encode("utf-8"):
                probs.append(where + ": wording of %s differs from the block byte for byte" % w["block"])
    missing = [dict(item=i, reader=r) for i in items for r in rd if (i, r) not in seen]
    cited = {bid for row in ext.get("rows", []) for bid in row.get("blocks", [])}
    orphans = sorted(set(bl) - cited)
    return dict(ok=not probs and not missing and not orphans, rows=len(ext.get("rows", [])),
                rows_expected=len(items) * len(rd), missing_rows=missing, blocks_not_cited=orphans, problems=probs)


# ------------------------------------------------------------------ Opus's tabulation (round 2's form)
P_POINT = re.compile(r"^- \*\*(Mimo|GLM)\*\* \((reply lines? [^;]+); (challenges|does not challenge)\): (.*)$")
P_NONE = re.compile(r"^- \*\*(Mimo|GLM):\*\* no point on this item")
P_PROP = re.compile(r"^  - Proposal `([A-Z]\d+-B\d+)` \((reply lines? [^;)]+)(;[^)]*)?\), would change (.*?)([:.])$")
P_QUOTE = re.compile(r"^  - Quotations: (.*)$")


def opus_rows(tab_path, part):
    t = H.read_text(tab_path)
    m = re.search(r"(?ms)^### Part %d: .*?(?=^### Part \d+: |^## \d)" % part, t)
    if not m:
        H.refuse("no section '### Part %d:' in the tabulation" % part)
    sec = m.group(0)
    rows, wordings, decisions, order = {}, {}, {}, []
    item = cur = cur_reader = None
    lines = sec.split("\n")
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("#### "):
            item = l[5:].split(" · ")[0].strip()
            if item.startswith("Part "):
                item = None
            else:
                order.append(item)
            cur = None
        elif item and P_POINT.match(l):
            mm = P_POINT.match(l)
            r = rows.setdefault((item, mm.group(1)), dict(points=[], blocks=[], lines=[]))
            said = mm.group(3)
            if said == "does not challenge" and mm.group(4).startswith("Named among the items with nothing to add"):
                said = "nothing to add"
            cur = dict(reply_lines=ranges(mm.group(2)), said=said, digest=mm.group(4), quotes=[])
            cur_reader = mm.group(1)
            r["points"].append(cur)
        elif item and P_NONE.match(l):
            rows.setdefault((item, P_NONE.match(l).group(1)), dict(points=[], blocks=[], lines=[]))
            cur = None
        elif item and cur is not None and P_PROP.match(l):
            mm = P_PROP.match(l)
            r = rows[(item, cur_reader)]
            bid = mm.group(1)
            if bid not in r["blocks"]:
                r["blocks"].append(bid)
            r["lines"] += [int(x) for x in re.findall(r"L(\d+)", mm.group(4))]
            if mm.group(5) == ":":
                j = i + 1
                while j < len(lines) and not lines[j].startswith("````"):
                    j += 1
                k = j + 1
                while k < len(lines) and not lines[k].startswith("````"):
                    k += 1
                wordings.setdefault(bid, "\n".join(lines[j + 1:k]))
                i = k
        elif item and cur is not None and P_QUOTE.match(l):
            cur["quotes"] = re.findall(r"“(.*?)” — (found at [^;]*|not found in the text[^;]*)", P_QUOTE.match(l).group(1))
        elif item and l.startswith("- **Goes to a checker**"):
            decisions[item] = True
        elif item and l.startswith("- **Goes to no checker**"):
            decisions[item] = False
        i += 1
    out = []
    for it in order:
        for rdr in ("Mimo", "GLM"):
            r = rows.get((it, rdr), dict(points=[], blocks=[], lines=[]))
            saids = [p["said"] for p in r["points"]]
            said = ("challenges" if "challenges" in saids else "does not challenge" if "does not challenge" in saids
                    else "nothing to add" if "nothing to add" in saids else "no point")
            out.append(dict(item=it, reader=rdr, said=said, reply_lines=[list(x) for p in r["points"] for x in p["reply_lines"]],
                            blocks=r["blocks"], lines_to_change=sorted(set(r["lines"])),
                            quotes=[q for p in r["points"] for q in p["quotes"]]))
    return dict(part=part, items=order, rows=out, wordings=wordings, goes_to_checker=decisions)


# ------------------------------------------------------------------ comparing a filled sheet with Opus's rows
def compare(ext, tab_path, part, replies):
    op = opus_rows(tab_path, part)
    bl = {b["id"]: b for r in replies for b in r["blocks"]}
    orow = {(r["item"], r["reader"]): r for r in op["rows"]}
    srow = {(r.get("item"), r.get("reader")): r for r in ext.get("rows", [])}
    addressed = lambda s: s in ("challenges", "does not challenge")
    res = dict(pairs=len(orow), found=0, missed=[], extra=[], said_equal=0, said_diff=[], blocks_equal=0,
               blocks_diff=[], lines_equal=0, lines_diff=[], passages_covered=0, passages_missed=[])
    for key, o in orow.items():
        s = srow.get(key)
        if s is None:
            res["missed"].append(dict(item=key[0], reader=key[1], opus=o["said"], sonnet="(no row)"))
            continue
        if addressed(o["said"]) and not addressed(s.get("said")):
            res["missed"].append(dict(item=key[0], reader=key[1], opus=o["said"], sonnet=s.get("said")))
        elif addressed(s.get("said")) and not addressed(o["said"]):
            res["extra"].append(dict(item=key[0], reader=key[1], opus=o["said"], sonnet=s.get("said")))
        elif addressed(o["said"]):
            res["found"] += 1
        if o["said"] == s.get("said"):
            res["said_equal"] += 1
        else:
            res["said_diff"].append(dict(item=key[0], reader=key[1], opus=o["said"], sonnet=s.get("said")))
        if sorted(o["blocks"]) == sorted(s.get("blocks", [])):
            res["blocks_equal"] += 1
        else:
            res["blocks_diff"].append(dict(item=key[0], reader=key[1], opus=o["blocks"], sonnet=s.get("blocks", [])))
        if o["lines_to_change"] == sorted(set(s.get("lines_to_change", []))):
            res["lines_equal"] += 1
        else:
            res["lines_diff"].append(dict(item=key[0], reader=key[1], opus=o["lines_to_change"],
                                          sonnet=sorted(set(s.get("lines_to_change", [])))))
        sr = ranges(s.get("reply_lines"))
        miss = [r for r in (tuple(x) for x in o["reply_lines"]) if not any(overlap(r, x) for x in sr)]
        if miss:
            res["passages_missed"].append(dict(item=key[0], reader=key[1], opus_passages_not_named=miss))
        else:
            res["passages_covered"] += 1
    # goes to a checker: an item goes when any reader's point challenges it
    sgo = {it: any(srow.get((it, r), {}).get("said") == "challenges" for r in ("Mimo", "GLM")) for it in op["items"]}
    res["items"] = len(op["items"])
    res["goes_to_checker_equal"] = sum(1 for it in op["items"] if sgo[it] == op["goes_to_checker"].get(it))
    res["goes_to_checker_diff"] = [dict(item=it, opus=op["goes_to_checker"].get(it), sonnet=sgo[it])
                                   for it in op["items"] if sgo[it] != op["goes_to_checker"].get(it)]
    # wordings: Opus's printed wording against the reply's block; the sheet's copied wording against both
    wd = []
    sw = {w["block"]: w.get("text", "") for r in ext.get("rows", []) for w in r.get("wordings", [])}
    for bid in sorted(set(op["wordings"]) | set(sw), key=lambda b: (b.split("-")[0], int(b.split("B")[-1]))):
        block = bl.get(bid, {}).get("text")
        wd.append(dict(block=bid, opus_equals_reply=(op["wordings"].get(bid) == block) if bid in op["wordings"] else None,
                       sheet_equals_reply=(sw.get(bid) == block) if bid in sw else None))
    res["wordings"] = wd
    res["wordings_opus_exact"] = sum(1 for w in wd if w["opus_equals_reply"])
    res["wordings_sheet_exact"] = sum(1 for w in wd if w["sheet_equals_reply"])
    res["wordings_sheet_given"] = sum(1 for w in wd if w["sheet_equals_reply"] is not None)
    res["blocks_in_replies"] = len(bl)
    res["ok"] = (not res["missed"] and not res["extra"] and not res["said_diff"] and not res["blocks_diff"]
                 and not res["lines_diff"] and not res["passages_missed"] and not res["goes_to_checker_diff"])
    return res


QUOTED = re.compile(r"“([^”]{2,400})”|\"([^\"\n]{2,400})\"")


def fill(ext, replies, text_path):
    """The program's half of each row: the wordings, copied from the blocks byte for byte, and every quotation in
    double quotation marks inside the row's reply passages (outside the blocks), with the lines of the text where it
    stands (empty: not found in the text)."""
    bl = {b["id"]: b for r in replies for b in r["blocks"]}
    rd = {r["reader"]: r for r in replies}
    text_lines = H.read_text(text_path).split("\n") if text_path else None
    normed = [norm(l) for l in text_lines] if text_lines else None
    out = json.loads(json.dumps(ext))
    for row in out.get("rows", []):
        row["wordings"] = [dict(block=b, text=bl[b]["text"], by="program") for b in row.get("blocks", []) if b in bl]
        row["lines_to_change"] = sorted({ln for b in row.get("blocks", []) if b in bl for ln in bl[b]["lines_named_first_line"]})
        r = rd.get(row.get("reader"))
        if not (r and text_lines):
            continue
        lines = r["text"].split("\n")
        inblock = {i for b in r["blocks"] for i in range(b["reply_lines"][0], b["reply_lines"][1] + 1)}
        qs = []
        for a, b in ranges(row.get("reply_lines")):
            for i in range(max(1, a), min(b, len(lines)) + 1):
                if i in inblock:
                    continue
                for m in QUOTED.finditer(lines[i - 1]):
                    q = m.group(1) or m.group(2)
                    if q not in [x["q"] for x in qs]:
                        qs.append(dict(q=q, reply_line=i, found_at=quote_lines(q, text_lines, normed)))
        row["quotations"] = qs
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["items", "blocks", "quote", "sheet", "check", "fill", "opus", "compare"])
    ap.add_argument("--brief")
    ap.add_argument("--reply", action="append", default=[])
    ap.add_argument("--prefix")
    ap.add_argument("--text")
    ap.add_argument("--q", action="append", default=[])
    ap.add_argument("--extraction")
    ap.add_argument("--tabulation")
    ap.add_argument("--part", type=int)
    ap.add_argument("--out")
    ap.add_argument("--no-blocks", action="store_true")
    ap.add_argument("--prefill", action="store_true")
    ap.add_argument("--lines-by-program", action="store_true",
                    help="check: do not ask lines_to_change to match the blocks (fill sets them from the blocks)")
    a = ap.parse_args()
    if a.cmd == "items":
        it = items_of(H.read_text(a.brief))
        H.emit(dict(ok=bool(it), brief=H.rel(a.brief), count=len(it), items=it))
    if a.cmd == "blocks":
        b, unclosed = blocks_of(H.read_text(a.reply[0]), a.prefix)
        H.emit(dict(ok=not unclosed, reply=H.rel(a.reply[0]), count=len(b), unclosed_fence=unclosed, blocks=b))
    if a.cmd == "quote":
        tl = H.read_text(a.text).split("\n")
        nl = [norm(l) for l in tl]
        rows = [dict(q=q, found_at=quote_lines(q, tl, nl)) for q in a.q]
        H.emit(dict(ok=all(r["found_at"] for r in rows), text=H.rel(a.text), quotes=rows))
    replies = parse_replies(a.reply)
    if a.cmd == "sheet":
        s = sheet(a.brief, replies, with_blocks=not a.no_blocks)
        if a.prefill:
            s = prefill(s, replies)
        if a.out:
            H.write_json(a.out, s)
        H.emit(dict(ok=True, **s))
    ext = H.load_json(a.extraction) if a.extraction else None
    if a.cmd == "check":
        H.emit(dict(job="tabulation_check", extraction=H.rel(a.extraction),
                    **check(ext, a.brief, a.text, replies, lines_by_program=a.lines_by_program)))
    if a.cmd == "fill":
        out = fill(ext, replies, a.text)
        H.write_json(a.out, out)
        H.emit(dict(ok=True, out=H.rel(a.out), rows=len(out.get("rows", []))))
    if a.cmd == "opus":
        H.emit(dict(ok=True, **opus_rows(a.tabulation, a.part)))
    if a.cmd == "compare":
        H.emit(dict(job="tabulation_compare", extraction=H.rel(a.extraction), part=a.part,
                    **compare(ext, a.tabulation, a.part, replies)))


if __name__ == "__main__":
    main()
