import re, difflib, hashlib, json, os

ROOT = '/home/user/ThreadSmith/Semantics'
F10 = ROOT + '/authority/10 Claude Fable Semantics - standalone theory.md'
F11 = ROOT + '/authority/11 Claude Fable Semantics - standalone theory, revision 1.md'


def read(p):
    return open(p if p.startswith('/') else ROOT + '/' + p, encoding='utf-8').read()


def md5(p):
    return hashlib.md5(open(p if p.startswith('/') else ROOT + '/' + p, 'rb').read()).hexdigest()


# ---------- sentence splitting ----------
MATH = re.compile(r'\\\(.*?\\\)|\\\[.*?\\\]')
ABBR = {'e.g', 'i.e', 'cf', 'etc', 'vs', 'Fig', 'al', 'No'}


def split_sents(text):
    """Split prose into sentences; math spans are never split."""
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
                    if word.rstrip('.') not in ABBR and not re.fullmatch(r'[A-Z]', word):
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
    # merge bare bold labels like "**Repair.**" into next sentence
    merged = []
    for s in res:
        if merged and re.fullmatch(r'\*\*[^*]+\*\*', merged[-1]):
            merged[-1] = merged[-1] + ' ' + s
        else:
            merged.append(s)
    return merged


def norm(s):
    s = re.sub(r'</?u>', '', s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


# ---------- file 10 index ----------
class TextIndex:
    def __init__(self, path, label):
        self.label = label
        self.lines = read(path).split('\n')
        self.parts = {}      # line -> part string
        self.sents = []      # (sentence, line)
        part = ''
        sub = ''
        self.part_titles = {}
        self.deriv_titles = {}
        for i, l in enumerate(self.lines, 1):
            if l.startswith('# '):
                part = l[2:].strip()
                sub = ''
                mo = re.match(r'Part ([0IVXL]+) — ', part)
                if mo:
                    self.part_titles[mo.group(1)] = part
            elif l.startswith('## '):
                sub = l[3:].strip()
                mo = re.match(r'(\d+)\. ', sub)
                if mo and part.startswith('Part XVI'):
                    self.deriv_titles[mo.group(1)] = sub
            lead = ''
            mo = re.match(r'\*\*([^*]+?)\.?\*\*', l)
            if mo and not sub:
                lead = mo.group(1)
            self.parts[i] = part + (' / ' + sub if sub else (' / ' + lead if lead else ''))
            if l.strip() and not l.startswith('#') and l.strip() != '---':
                for s in split_sents(l):
                    self.sents.append((s, i))

    def find(self, s):
        """Line of a verbatim substring, or None."""
        for i, l in enumerate(self.lines, 1):
            if s in l:
                return i
        return None

    def match_sentence(self, q, near=None):
        """Map a quoted sentence to this text's own sentence: exact, normalized, then fuzzy."""
        for s, i in self.sents:
            if s == q:
                return s, i, 1.0
        nq = norm(q)
        for s, i in self.sents:
            if norm(s) == nq:
                return s, i, 1.0
        best = (None, None, 0.0)
        for s, i in self.sents:
            if near and abs(i - near) > 40:
                continue
            r = difflib.SequenceMatcher(None, norm(s), nq).ratio()
            if r > best[2]:
                best = (s, i, r)
        return best

    def part_name(self, roman, sub=None):
        t = self.part_titles.get(roman, 'Part ' + roman)
        if sub:
            t += ' / ' + self.deriv_titles.get(sub, sub + '.')
        return t


def token_span(old, new):
    """Common prefix/suffix at word level; returns (old_span, new_span) or None."""
    a = re.findall(r'\S+|\s+', old)
    b = re.findall(r'\S+|\s+', new)
    p = 0
    while p < len(a) and p < len(b) and a[p] == b[p]:
        p += 1
    q = 0
    while q < len(a) - p and q < len(b) - p and a[-1 - q] == b[-1 - q]:
        q += 1
    os_ = ''.join(a[p:len(a) - q]).strip()
    ns_ = ''.join(b[p:len(b) - q]).strip()
    return os_, ns_
