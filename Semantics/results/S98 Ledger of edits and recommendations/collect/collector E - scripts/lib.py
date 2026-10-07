"""Collector E helpers (log S98): texts with their md5s, headings, sentence bounds, extraction.

Reads only. Nothing here writes a file.
"""
import hashlib, re, subprocess

SEM = "/home/user/ThreadSmith/Semantics/"

# Target texts: name -> (path under Semantics/, md5, label used in "target_text")
TEXTS = {
    "file 11": ("authority/11 Claude Fable Semantics - standalone theory, revision 1.md",
                "5e494c1095d920d128b9a79de378f923",
                "file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md)"),
    "file 12": ("authority/12 Claude Fable Semantics - causality, standalone theory.md",
                "ce7e8e2c5f89d982fa888c19587d508b",
                "file 12 (authority/12 Claude Fable Semantics - causality, standalone theory.md)"),
    "draft 3": ("tests/Revision 2 - file 13 draft 3, theory text.md",
                "403c4f2fb3e5d57bb48a5647011c9f91",
                "file 13 draft 3, theory text (md5 403c4f2fb3e5d57bb48a5647011c9f91)"),
    "draft 4": ("tests/Revision 2 - file 13 draft 4, theory text.md",
                "fc55b470c63cd4b3c27d6aa64d8d8c17",
                "file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17)"),
    "draft 5": ("tests/Revision 2 - file 13 draft 5, theory text.md",
                "7f1d8ad02adf96e27622593bd263252e",
                "file 13 draft 5, theory text (md5 7f1d8ad02adf96e27622593bd263252e)"),
    "latest text": ("tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md",
                    "ebca15a047f686b15d5f5766b69825c9",
                    "latest text (md5 ebca15a047f686b15d5f5766b69825c9)"),
    "scrubbed copy": ("tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md",
                      "2517ef4ec1f274e8de2bfb7e6661ef94", "scrubbed copy"),
    "repaired copy": ("tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md",
                      "8bb4d19d5aad53de2492b2193fd23ff1", "repaired copy"),
    "change list": ("tests/Revision 2 - change list, draft of 23 September.md",
                    "c6d25ec1ccc3ea3e72136a75a794be62",
                    "change list, draft 5 state (tests/Revision 2 - change list, draft of 23 September.md, md5 c6d25ec1ccc3ea3e72136a75a794be62), entry W38.1, the note of sources and departures"),
}


def md5b(b):
    return hashlib.md5(b).hexdigest()


def read(path):
    """Text of a file under Semantics/ (path relative), and its md5."""
    raw = open(SEM + path, "rb").read()
    return raw.decode("utf-8"), md5b(raw)


def load(name):
    path, h, _ = TEXTS[name]
    t, got = read(path)
    if got != h:
        raise SystemExit("md5 of %s is %s, not %s" % (name, got, h))
    return t.split("\n")


def git_md5(commit, path):
    raw = subprocess.run(["git", "-C", SEM, "show", "%s:Semantics/%s" % (commit, path)],
                         capture_output=True, check=True).stdout
    return raw.decode("utf-8"), md5b(raw)


LABEL_RX = re.compile(r"^\*\*([^*]{1,80}?)\.?\*\*")


def part_at(lines, n):
    """'H1 / H2 / bold label' in force at 1-based line n (label: the nearest bold paragraph label
    at or above n within the same heading section)."""
    h1 = h2 = lab = None
    for i in range(0, n):
        l = lines[i]
        m = re.match(r"^(#{1,6})\s+(.*)$", l)
        if m:
            if len(m.group(1)) == 1:
                h1, h2, lab = m.group(2).strip(), None, None
            elif len(m.group(1)) == 2:
                h2, lab = m.group(2).strip(), None
            continue
        m = LABEL_RX.match(l)
        if m:
            lab = m.group(1).strip().rstrip(".")
    out = h1 or ""
    if h2:
        out += " / " + h2
    if lab:
        out += " / " + lab
    return out


ABBR = {"e.g", "i.e", "cf", "l", "ll", "p", "pp", "vs", "no", "fig", "resp", "etc", "al", "viz", "ch", "sec", "eq"}


def _math_mask(s):
    m = [False] * len(s)
    for rx in (r"\\\((.*?)\\\)", r"\\\[(.*?)\\\]"):
        for mm in re.finditer(rx, s):
            for k in range(mm.start(), mm.end()):
                m[k] = True
    return m


def sentence_starts(s):
    starts = [0]
    mask = _math_mask(s)
    for m in re.finditer(r"[.?!][\"'”’*_)\]]*(\s+)(?=[A-Z\"“‘*(\\\[_`])", s):
        p = m.start()
        if mask[p]:
            continue
        j = p
        while j > 0 and not s[j - 1].isspace() and s[j - 1] not in "(\"“":
            j -= 1
        tok = s[j:p]
        t = tok.lower().strip("*_")
        if t in ABBR or t.rstrip(".") in ABBR:
            continue
        if re.fullmatch(r"[A-Z]", tok):
            continue
        if re.fullmatch(r"\d+", tok) and s[:j].strip() == "":
            continue
        starts.append(m.end())
    return sorted(set(starts))


def sentence_bounds(s, a, b):
    st = sentence_starts(s)
    lo = max(x for x in st if x <= a)
    nxt = [x for x in st if x >= max(b, a + 1)]
    hi = nxt[0] if nxt else len(s)
    return lo, hi


def sentence_of(line, frag):
    """The whole sentence(s) of line that contain frag (which must occur once)."""
    c = line.count(frag)
    if c != 1:
        raise ValueError("fragment occurs %d times: %r" % (c, frag[:80]))
    p = line.index(frag)
    a, b = sentence_bounds(line, p, p + len(frag))
    return line[a:b].strip()


def replaced_sentence(line, old, new):
    """Apply old -> new once in line; return (old_sentence, new_sentence)."""
    c = line.count(old)
    if c != 1:
        raise ValueError("old occurs %d times: %r" % (c, old[:80]))
    p = line.index(old)
    a, b = sentence_bounds(line, p, p + max(1, len(old)))
    nl = line[:p] + new + line[p + len(old):]
    d = len(new) - len(old)
    return line[a:b].strip(), nl[a:b + d].strip()


def find_unique_line(lines, frag, near=None):
    hits = [i + 1 for i, l in enumerate(lines) if frag in l]
    if near is not None and near in hits:
        return near
    if len(hits) != 1:
        raise ValueError("fragment on %d lines %s: %r" % (len(hits), hits[:8], frag[:80]))
    return hits[0]


def between(text, start, end, incl_start=True, incl_end=True, after=None):
    """The unique span of text from start to the first end after it (after: an earlier marker)."""
    base = 0
    if after is not None:
        if text.count(after) != 1:
            raise ValueError("after-marker occurs %d times: %r" % (text.count(after), after[:80]))
        base = text.index(after)
    p = text.index(start, base)
    if after is None and text.count(start) != 1:
        raise ValueError("start occurs %d times: %r" % (text.count(start), start[:80]))
    q = text.index(end, p + len(start))
    a = p if incl_start else p + len(start)
    b = q + len(end) if incl_end else q
    return text[a:b]


def quoted_after(text, marker, occurrence=1):
    """Content of the first double-quoted string ("..." or “...”) after a unique marker."""
    if text.count(marker) != 1:
        raise ValueError("marker occurs %d times: %r" % (text.count(marker), marker[:80]))
    p = text.index(marker) + len(marker)
    for _ in range(occurrence):
        m = re.search(r"[\"“]", text[p:])
        qa = p + m.start()
        close = "”" if text[qa] == "“" else "\""
        qb = text.index(close, qa + 1)
        res = text[qa + 1:qb]
        p = qb + 1
    return res


def unquote_block(block):
    """Strip one level of Markdown blockquote markers ('> ' or '>') from each line."""
    out = []
    for l in block.split("\n"):
        if l.startswith("> "):
            out.append(l[2:])
        elif l.startswith(">"):
            out.append(l[1:])
        else:
            out.append(l)
    return "\n".join(out)


def entry_fields(text, eid):
    """OLD and NEW fenced blocks of change-list-style entry '### eid ...' (first such heading)."""
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("### " + eid + " ")]
    if not idx:
        raise ValueError("no entry " + eid)
    i = idx[0]
    j = i + 1
    while j < len(lines) and not lines[j].startswith("### "):
        j += 1
    seg = lines[i:j]
    res = {"heading": lines[i], "line": i + 1}
    k = 0
    while k < len(seg):
        m = re.match(r"^- \*\*(OLD|NEW|FILE-11 LINE|WHERE|KIND):\*\*\s*(.*)$", seg[k])
        if m and m.group(1) in ("OLD", "NEW"):
            f = k + 1
            fence = re.match(r"^(`{3,})", seg[f]).group(1)
            e = f + 1
            while not (seg[e].strip() == fence):
                e += 1
            res[m.group(1)] = "\n".join(seg[f + 1:e])
            k = e
        elif m:
            res[m.group(1)] = m.group(2)
        k += 1
    return res
