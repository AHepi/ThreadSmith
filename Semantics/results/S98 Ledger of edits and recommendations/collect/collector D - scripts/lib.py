"""Collector D helpers: the four line-aligned texts, headings, sentence bounds, span application.

Reads only. Nothing here writes a file.
"""
import collections, hashlib, json, re

SEM = "/home/user/ThreadSmith/Semantics/"
TEXTS = {
    "draft 5": ("tests/Revision 2 - file 13 draft 5, theory text.md", "7f1d8ad02adf96e27622593bd263252e"),
    "scrubbed copy": ("tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md",
                      "2517ef4ec1f274e8de2bfb7e6661ef94"),
    "repaired copy": ("tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md",
                      "8bb4d19d5aad53de2492b2193fd23ff1"),
    "latest text": ("tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md",
                    "ebca15a047f686b15d5f5766b69825c9"),
}
STAGE1_NAME = "stage-1 text (S96; scrubbed copy with stage 1 applied, rebuilt in memory)"
STAGE1_MD5 = "c1eecbd1587e5aec91fd0ba7d46e1469"


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def load_text(name):
    path, h = TEXTS[name]
    raw = open(SEM + path, "rb").read()
    got = hashlib.md5(raw).hexdigest()
    if got != h:
        raise SystemExit("md5 of %s is %s, not %s" % (name, got, h))
    return raw.decode("utf-8").split("\n")


def headings(lines):
    """For each 1-based line number, 'H1 / H2' of the nearest preceding headings."""
    out = {}
    h1 = h2 = None
    for i, l in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.*)$", l)
        if m:
            lvl = len(m.group(1))
            if lvl == 1:
                h1, h2 = m.group(2).strip(), None
            elif lvl == 2:
                h2 = m.group(2).strip()
        out[i] = (h1 or "") + ((" / " + h2) if h2 else "")
    return out


ABBR = {"e.g", "i.e", "cf", "l", "ll", "p", "pp", "vs", "no", "fig", "resp", "etc", "al", "viz", "ch", "sec", "eq"}


def math_mask(s):
    """Boolean list: True where inside \\( \\) or \\[ \\]."""
    m = [False] * len(s)
    for rx in (r"\\\((.*?)\\\)", r"\\\[(.*?)\\\]"):
        for mm in re.finditer(rx, s):
            for k in range(mm.start(), mm.end()):
                m[k] = True
    return m


def sentence_starts(s):
    """Start offsets of the sentences of one line (always includes 0)."""
    starts = [0]
    mask = math_mask(s)
    for m in re.finditer(r"[.?!][\"'”’*_)\]]*(\s+)(?=[A-Z\"“‘*(\\\[_`])", s):
        p = m.start()
        if mask[p]:
            continue
        # token before the period
        j = p
        while j > 0 and not s[j - 1].isspace() and s[j - 1] not in "(\"“":
            j -= 1
        tok = s[j:p]
        t = tok.lower().strip("*_")
        if t in ABBR or t.rstrip(".") in ABBR:
            continue
        if re.fullmatch(r"[A-Z]", tok):            # an initial
            continue
        if re.fullmatch(r"\d+", tok) and s[:j].strip() == "":   # list number at line start
            continue
        starts.append(m.end(1) if False else m.end())
    return sorted(set(starts))


def sentence_bounds(s, a, b):
    """Extend [a,b) to whole sentences of s."""
    st = sentence_starts(s)
    lo = max(x for x in st if x <= a)
    nxt = [x for x in st if x >= max(b, a + 1)]
    hi = nxt[0] if nxt else len(s)
    if b > a and b <= lo:
        hi = hi
    return lo, hi


def apply_line(orig, spans_old_new):
    """spans_old_new: list of (old, new, key). Old spans must occur once. Returns new line and
    the list of (p, q, new, key) in old coordinates, sorted."""
    spans = []
    for old, new, key in spans_old_new:
        c = orig.count(old) if old else 0
        if c != 1:
            raise ValueError("span %r occurs %d times" % (old[:60], c))
        p = orig.index(old)
        spans.append((p, p + len(old), new, key))
    spans.sort()
    s = orig
    for p, q, new, key in reversed(spans):
        s = s[:p] + new + s[q:]
    return s, spans


def map_pos(x, spans, side):
    """Map an offset of the old line to the new line; x must not be strictly inside a span."""
    d = 0
    for p, q, new, key in spans:
        if q <= x and not (side == "left" and p == x == q):
            d += len(new) - (q - p)
        elif p < x < q:
            raise ValueError("inside span")
    return x + d


def sentences_for(orig, new_line, spans, key):
    """old_sentence and new_sentence for the span with this key."""
    p, q = next((sp[0], sp[1]) for sp in spans if sp[3] == key)
    a, b = sentence_bounds(orig, p, q if q > p else p + 1)
    # widen to cover any other span overlapping the sentence, then re-extend
    for _ in range(10):
        changed = False
        for sp in spans:
            if sp[0] < b and sp[1] > a and (sp[0] < a or sp[1] > b):
                a2, b2 = sentence_bounds(orig, min(a, sp[0]), max(b, sp[1]))
                if (a2, b2) != (a, b):
                    a, b, changed = a2, b2, True
        if not changed:
            break
    na = map_pos(a, spans, "left")
    nb = map_pos(b, spans, "right")
    os_ = orig[a:b].strip()
    ns_ = new_line[na:nb].strip()
    return os_, ns_


def locate_sentence(line, frag):
    """The sentence(s) of line containing frag (verbatim), or ''."""
    if not frag or line.count(frag) < 1:
        return ""
    p = line.index(frag)
    a, b = sentence_bounds(line, p, p + len(frag))
    return line[a:b].strip()


def scope_of(orig, old, old_sentence, whole_line=False):
    if old == "" or whole_line or old.strip() == orig.strip():
        return "paragraph" if not orig.lstrip().startswith("#") else "sentence"
    if old.strip() == old_sentence.strip():
        return "sentence"
    return "span"
