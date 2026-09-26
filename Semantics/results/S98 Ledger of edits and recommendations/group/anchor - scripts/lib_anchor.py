"""Shared helpers for the S98 anchoring step: texts, sentence splitting, line maps."""
import re, difflib, hashlib, json, os

ROOT = '/home/user/ThreadSmith/Semantics'
LEDGER = ROOT + '/results/S98 Ledger of edits and recommendations'
COLLECT = LEDGER + '/collect'
GROUP = LEDGER + '/group'

T = ROOT + '/tests/'
VERSIONS = [
    ('f10', 'authority/10 Claude Fable Semantics - standalone theory.md', 'file 10'),
    ('f11', 'authority/11 Claude Fable Semantics - standalone theory, revision 1.md', 'file 11'),
    ('d1', 'tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md', 'file 13 draft 1 (as sent)'),
    ('d2', 'tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md', 'file 13 draft 2 (as sent)'),
    ('d3', 'tests/Revision 2 - file 13 draft 3, theory text.md', 'file 13 draft 3'),
    ('d4', 'tests/Revision 2 - file 13 draft 4, theory text.md', 'file 13 draft 4'),
    ('d5', 'tests/Revision 2 - file 13 draft 5, theory text.md', 'file 13 draft 5'),
    ('scrubbed', 'tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md', 'scrubbed copy'),
    ('repaired', 'tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md', 'repaired copy'),
    ('latest', 'tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md', 'latest text'),
]
VPATH = {k: p for k, p, _ in VERSIONS}
VLABEL = {k: l for k, _, l in VERSIONS}
CHAIN = [k for k, _, _ in VERSIONS]


def read(p):
    return open(p if p.startswith('/') else ROOT + '/' + p, encoding='utf-8').read()


def md5(p):
    return hashlib.md5(open(p if p.startswith('/') else ROOT + '/' + p, 'rb').read()).hexdigest()


def lines_of(key):
    return read(VPATH[key]).split('\n')


# ---------- sentence splitting (collector A's method, extended) ----------
MATH = re.compile(r'\\\(.*?\\\)|\\\[.*?\\\]|`[^`]*`')
ABBR = {'e.g', 'i.e', 'cf', 'etc', 'vs', 'Fig', 'al', 'No', 'l', 'L', 'p', 'pp', 'ch', 'Ch', 'eq', 'ff', 'viz'}


def split_sents(text):
    """Split prose into sentences; math and code spans are never split; a bare bold label joins the next sentence."""
    masks = []

    def m(mo):
        masks.append(mo.group(0))
        return '\x00%d\x00' % (len(masks) - 1)
    t = MATH.sub(m, text)
    out, start, i, n = [], 0, 0, len(t)
    while i < n:
        ch = t[i]
        if ch in '.!?':
            j = i + 1
            while j < n and t[j] in '*”"’)_':
                j += 1
            if j < n and t[j] == ' ':
                k = j
                while k < n and t[k] == ' ':
                    k += 1
                if k < n and (t[k].isupper() or t[k].isdigit() or t[k] in '“"(\x00*\\[<'):
                    prev = re.search(r'([A-Za-z.]+)$', t[start:i])
                    word = prev.group(1) if prev else ''
                    numlabel = re.search(r'(^|\s)\**\(?\d+$', t[start:i])
                    if word.rstrip('.') not in ABBR and not re.fullmatch(r'[A-Z]', word) and not numlabel:
                        out.append(t[start:j])
                        start = k
                        i = k
                        continue
        i += 1
    if start < n:
        out.append(t[start:])

    def unm(s):
        return re.sub('\x00(\\d+)\x00', lambda mo: masks[int(mo.group(1))], s)
    res = [unm(s).strip() for s in out if s.strip()]
    # a bold span cut in two is joined again
    joined = []
    for s in res:
        if joined and joined[-1].count('**') % 2 == 1:
            joined[-1] = joined[-1] + ' ' + s
        else:
            joined.append(s)
    merged = []
    for s in joined:
        if merged and re.fullmatch(r'\([A-Za-z]{1,4}\d*\)', s):
            merged[-1] = merged[-1] + ' ' + s
        elif merged and re.fullmatch(r'\*\*[^*]+\*\*', merged[-1]):
            merged[-1] = merged[-1] + ' ' + s
        else:
            merged.append(s)
    return merged


def norm(s):
    s = re.sub(r'</?u>', '', s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def loose(s):
    """For similarity only: drop emphasis marks and ellipses as well."""
    s = norm(s)
    s = s.replace('**', '').replace('…', ' ').replace('...', ' ')
    s = re.sub(r'(?<!\\)\*', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def ratio(a, b):
    a, b = loose(a), loose(b)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def contain_ratio(q, s):
    """Partial ratio: q against the window of s, of q's length, that matches it best (for a span against a sentence)."""
    q, s = loose(q), loose(s)
    if not q or not s:
        return 0.0
    if len(q) >= len(s):
        return difflib.SequenceMatcher(None, q, s, autojunk=False).ratio()
    sm = difflib.SequenceMatcher(None, q, s, autojunk=False)
    best = 0.0
    for blk in sm.get_matching_blocks():
        start = max(0, blk.b - blk.a)
        end = start + len(q)
        if end > len(s):
            start, end = len(s) - len(q), len(s)
        x = difflib.SequenceMatcher(None, q, s[start:end], autojunk=False).ratio()
        if x > best:
            best = x
            if best == 1.0:
                break
    return best


ROMAN = re.compile(r'Part ([0IVXL]+)\b')


class Indexed:
    """A theory text cut into units (heading, sentence, display, list item), each with its Part and heading."""

    def __init__(self, key):
        self.key = key
        self.lines = lines_of(key)
        self.units = []          # dicts
        self.by_line = {}        # line -> [unit index]
        self.part_of_line = {}
        self.head_of_line = {}
        self.label_of_line = {}
        self.part_titles = {}    # roman -> full part heading
        part, head, label = 'Front matter (before Part 0)', '', ''
        self.block_end = {}
        inblock = None
        for i, l in enumerate(self.lines, 1):
            s = l.strip()
            if inblock is not None:
                self.part_of_line[i] = part
                self.head_of_line[i] = head
                self.label_of_line[i] = label
                u = self.units[inblock]
                u['text'] += '\n' + l
                u['line_end'] = i
                u['end'] = len(l)
                self.by_line.setdefault(i, []).append(inblock)
                if '\\]' in l:
                    inblock = None
                continue
            if l.startswith('# '):
                title = l[2:].strip()
                mo = re.match(r'Part ([0IVXL]+) — ', title)
                if mo:
                    part = title
                    self.part_titles[mo.group(1)] = title
                    head, label = '', ''
                else:
                    head = ''
                kind = 'heading'
            elif l.startswith('## ') or l.startswith('### '):
                head = l.lstrip('#').strip()
                label = ''
                kind = 'heading'
            elif not s or s == '---':
                kind = None
            elif s.startswith('\\['):
                kind = 'display'
                if '\\]' not in s:
                    inblock = len(self.units)
            elif re.match(r'^(- |\* |\d+\. )', s):
                kind = 'list item'
            else:
                kind = 'prose'
                mo = re.match(r'\*\*([^*]+?)\.?\*\*', s)
                label = mo.group(1).strip() if mo else ''
            self.part_of_line[i] = part
            self.head_of_line[i] = head
            self.label_of_line[i] = label
            if kind is None:
                continue
            if kind == 'prose':
                pieces = split_sents(l)
            else:
                pieces = [l.strip()]
            pos = 0
            n = 0
            for p in pieces:
                n += 1
                at = l.find(p, pos)
                if at < 0:
                    at = pos
                end = at + len(p)
                pos = end
                u = dict(id='L%d.s%d' % (i, n), line=i, line_end=i, n=n,
                         kind=('sentence' if kind == 'prose' else kind),
                         part=part, heading=head, label=label if kind != 'heading' else '',
                         text=p, start=at, end=end)
                self.by_line.setdefault(i, []).append(len(self.units))
                self.units.append(u)

    def heading_path(self, u):
        h = u['heading']
        if u.get('label'):
            h = (h + ' / ' if h else '') + u['label']
        return h


# ---------- line maps ----------

def line_map(a_lines, b_lines, move_ratio=0.6, pair_ratio=0.3):
    """Map each line of A (1-based) to a line of B or None, with kind and ratio."""
    sm = difflib.SequenceMatcher(None, a_lines, b_lines, autojunk=False)
    res = {}
    unA, unB = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                res[i1 + k + 1] = (j1 + k + 1, 'equal', 1.0)
        elif tag == 'delete':
            unA += list(range(i1, i2))
        elif tag == 'insert':
            unB += list(range(j1, j2))
        else:  # replace: pair by similarity, in order
            A = list(range(i1, i2)); B = list(range(j1, j2))
            usedB = set()
            lastj = -1
            for a in A:
                best, bj = 0.0, None
                if not a_lines[a].strip():
                    # blank line: pair with a blank in B if any in order
                    for b in B:
                        if b > lastj and b not in usedB and not b_lines[b].strip():
                            best, bj = 1.0, b
                            break
                else:
                    for b in B:
                        if b in usedB or not b_lines[b].strip():
                            continue
                        r = difflib.SequenceMatcher(None, a_lines[a], b_lines[b], autojunk=False).ratio()
                        if r > best:
                            best, bj = r, b
                if bj is not None and best >= pair_ratio:
                    res[a + 1] = (bj + 1, 'equal' if a_lines[a] == b_lines[bj] else 'changed', round(best, 3))
                    usedB.add(bj)
                    lastj = bj
                else:
                    unA.append(a)
            unB += [b for b in B if b not in usedB]
    # moved lines: unmatched A lines against unmatched B lines
    usedB = set()
    for a in unA:
        if not a_lines[a].strip() or a_lines[a].strip() == '---':
            res[a + 1] = (None, 'removed', 0.0)
            continue
        best, bj = 0.0, None
        for b in unB:
            if b in usedB or not b_lines[b].strip():
                continue
            r = difflib.SequenceMatcher(None, a_lines[a], b_lines[b], autojunk=False).ratio()
            if r > best:
                best, bj = r, b
        if bj is not None and best >= move_ratio:
            res[a + 1] = (bj + 1, 'moved' if a_lines[a] != b_lines[bj] else 'moved, same', round(best, 3))
            usedB.add(bj)
        else:
            res[a + 1] = (None, 'removed', 0.0)
    return res
