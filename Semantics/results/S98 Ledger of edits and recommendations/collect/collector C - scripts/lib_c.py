"""Collector C (S98) helpers: reading, sentence splitting, change-list and brief parsing.
The sentence splitter follows collector A's lib.py (math spans never split)."""
import re, hashlib, json, os, subprocess

ROOT = '/home/user/ThreadSmith/Semantics'
SP = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/c'
OUTDIR = ROOT + '/results/S98 Ledger of edits and recommendations/collect'
F11 = 'authority/11 Claude Fable Semantics - standalone theory, revision 1.md'
CL = 'tests/Revision 2 - change list, draft of 23 September.md'
TEXTS = [  # label, path
    ('file 13 draft 1 (as sent)', 'tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md'),
    ('file 13 draft 2 (as sent)', 'tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md'),
    ('file 13 draft 3', 'tests/Revision 2 - file 13 draft 3, theory text.md'),
    ('file 13 draft 4', 'tests/Revision 2 - file 13 draft 4, theory text.md'),
    ('file 13 draft 5', 'tests/Revision 2 - file 13 draft 5, theory text.md'),
    ('scrubbed copy', 'tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md'),
    ('repaired copy', 'tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md'),
    ('latest text', 'tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md'),
]
# change-list versions (commit -> label, file-13 draft built from it, round)
CL_VERSIONS = [
    ('12e73da', 'change list draft 1 (12e73da)', 'file 13 draft 1 (as sent)', 'S90'),
    ('587eebf', 'change list draft 2 (587eebf)', 'file 13 draft 2 (as sent)', 'S90'),
    ('99e9cd0', 'change list draft 3 (99e9cd0)', 'file 13 draft 3', 'S90'),
    ('3f7c3ab', 'change list draft 4 (3f7c3ab)', 'file 13 draft 4', 'S91'),
    ('8816fcf', 'change list draft 5 (8816fcf)', 'file 13 draft 5', 'S93'),
]


def read(p):
    return open(p if p.startswith('/') else ROOT + '/' + p, encoding='utf-8').read()


def md5(p):
    return hashlib.md5(open(p if p.startswith('/') else ROOT + '/' + p, 'rb').read()).hexdigest()


MATH = re.compile(r'\\\(.*?\\\)|\\\[.*?\\\]')
ABBR = {'e.g', 'i.e', 'cf', 'etc', 'vs', 'Fig', 'al', 'No', 'pp', 'p'}


def split_spans(t0):
    """Split one line of prose into sentences; returns (start, end) offsets. Math never split."""
    t = MATH.sub(lambda mo: 'M' * len(mo.group(0)), t0)
    out, start, i, n = [], 0, 0, len(t)
    while i < n:
        ch = t[i]
        if ch in '.!?∎':
            j = i + 1
            while j < n and t[j] in '*”"’)_':
                j += 1
            if j < n and t[j] == ' ':
                k = j
                while k < n and t[k] == ' ':
                    k += 1
                if k < n and (t[k].isupper() or t[k].isdigit() or t[k] in '“"(*\\[<'):
                    prev = re.search(r'([A-Za-z.]+)$', t[start:i])
                    word = prev.group(1) if prev else ''
                    if word.rstrip('.') not in ABBR and not re.fullmatch(r'[A-Z]', word):
                        out.append((start, j))
                        start = k
                        i = k
                        continue
        i += 1
    if start < n:
        out.append((start, n))
    # merge a bare bold label ("**Repair.**") into the next sentence
    merged = []
    for s, e in out:
        if merged and re.fullmatch(r'\*\*[^*]+\*\*', t0[merged[-1][0]:merged[-1][1]].strip()):
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((s, e))
    return merged


class Text:
    def __init__(self, path, label=None):
        self.path = path
        self.label = label or path
        self.raw = read(path)
        self.lines = self.raw.split('\n')
        self.starts = []
        off = 0
        for l in self.lines:
            self.starts.append(off)
            off += len(l) + 1
        self.part = {}
        part = sub = lead = ''
        indisp = False
        for i, l in enumerate(self.lines, 1):
            if l.startswith('# '):
                part, sub, lead = l[2:].strip(), '', ''
            elif l.startswith('## '):
                sub, lead = l[3:].strip(), ''
            elif indisp or l.strip() == '' or l.strip().startswith('\\['):
                if l.strip().startswith('\\[') and not l.strip().endswith('\\]'):
                    indisp = True
                elif indisp and l.strip().endswith('\\]'):
                    indisp = False
            else:
                mo = re.match(r'\*\*([^*]+?)\.?\*\*', l)
                lead = mo.group(1).strip() if mo else ''
            if i < 9 and not part.startswith('Part'):
                part = 'Front matter (before Part 0)'
            name = part
            if sub:
                name += ' / ' + sub
            if lead and len(lead) < 80:
                name += ' / ' + lead
            self.part[i] = name

    def count(self, s):
        return self.raw.count(s)

    def line_of(self, off):
        lo, hi = 0, len(self.starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.starts[mid] <= off:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    def sentences_around(self, s):
        """If s occurs once: (first_line, last_line, sentence text covering s) with whole sentences."""
        if not s or self.raw.count(s) != 1:
            return None
        a = self.raw.index(s)
        b = a + len(s)
        la, lb = self.line_of(a), self.line_of(max(a, b - 1))
        # extend start to sentence start on line la, end to sentence end on line lb
        la_start = self.starts[la - 1]
        spans = split_spans(self.lines[la - 1])
        sa = la_start
        for x, y in spans:
            if la_start + x <= a < la_start + y + 1:
                sa = la_start + x
                break
        lb_start = self.starts[lb - 1]
        spans = split_spans(self.lines[lb - 1])
        sb = lb_start + len(self.lines[lb - 1])
        for x, y in spans:
            if lb_start + x < b <= lb_start + y + 1:
                sb = lb_start + y
                break
        return la, lb, self.raw[sa:sb], sa, sb


FENCE = re.compile(r'^(\s*)(````+)(\w*)\s*$')


def fenced_after(lines, i):
    """Given index i at or before a fence opening line, return (content, index after closing fence)."""
    while i < len(lines) and not FENCE.match(lines[i]):
        i += 1
    if i >= len(lines):
        return None, i
    m = FENCE.match(lines[i])
    ind, ticks = m.group(1), m.group(2)
    j = i + 1
    buf = []
    while j < len(lines):
        m2 = FENCE.match(lines[j])
        if m2 and m2.group(2) == ticks and m2.group(3) == '':
            break
        l = lines[j]
        if ind and l.startswith(ind):
            l = l[len(ind):]
        buf.append(l)
        j += 1
    return '\n'.join(buf), j + 1


def parse_changelist(text):
    lines = text.split('\n')
    start = next(i for i, l in enumerate(lines) if l.strip() == '## The entries')
    entries = []
    cur = None
    infence = None
    i = start + 1
    while i < len(lines):
        l = lines[i]
        m = FENCE.match(l)
        if m:
            if infence is None:
                infence = m.group(2)
            elif m.group(2) == infence and m.group(3) == '':
                infence = None
            i += 1
            continue
        if infence:
            i += 1
            continue
        if l.startswith('### '):
            h = l[4:].strip()
            mo = re.match(r'(W[^ ]+(?: \+ W[^ ]+)*) — (.*)$', h)
            cur = {'id': mo.group(1) if mo else h, 'title': mo.group(2) if mo else '', 'heading': h,
                   'fields': {}, 'line_no': i + 1}
            entries.append(cur)
            i += 1
            continue
        if l.startswith('## ') and cur is not None:
            cur = None
        if cur is not None:
            mo = re.match(r'^- \*\*([A-Z0-9 /\-]+):\*\*\s?(.*)$', l)
            if mo:
                key, val = mo.group(1), mo.group(2)
                if (key in ('OLD', 'NEW') and val.strip() == '') or key in ('LOCATOR', 'LAYER-2 ROW'):
                    if i + 1 < len(lines) and FENCE.match(lines[i + 1]):
                        content, j = fenced_after(lines, i + 1)
                        cur[key] = content
                        cur['fields'][key] = val
                        i = j
                        continue
                # collect continuation lines (indented) for the field
                buf = [val]
                j = i + 1
                while j < len(lines) and (lines[j].startswith('  ') or lines[j].strip() == '') and not lines[j].startswith('- **'):
                    if FENCE.match(lines[j]):
                        break
                    if lines[j].strip() == '' and j + 1 < len(lines) and not lines[j + 1].startswith('  '):
                        break
                    buf.append(lines[j])
                    j += 1
                cur['fields'][key] = '\n'.join(buf).strip()
                i = j
                continue
        i += 1
    return entries


def parse_brief(text):
    """Items '### R01 · place' with **Kind:** line, **Declaration:**, **Old:**/**New:** fenced blocks."""
    lines = text.split('\n')
    items = []
    i = 0
    while i < len(lines):
        mo = re.match(r'^### ([CRX]\d\d) · (.*)$', lines[i])
        if mo:
            it = {'id': mo.group(1), 'place': mo.group(2), 'line_no': i + 1}
            j = i + 1
            while j < len(lines) and not lines[j].startswith('### ') and not lines[j].startswith('## '):
                l = lines[j]
                if l.startswith('**Kind:**'):
                    it['kind_line'] = l
                if l.startswith('**Declaration:**'):
                    it['declaration'] = l[len('**Declaration:**'):].strip()
                if l.strip() in ('**Old:**', '**New:**'):
                    key = 'old' if 'Old' in l else 'new'
                    content, k = fenced_after(lines, j + 1)
                    it[key] = content
                    j = k
                    continue
                j += 1
            items.append(it)
            i = j
            continue
        i += 1
    return items


def write_jsonl(path, recs):
    with open(path, 'w', encoding='utf-8') as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
