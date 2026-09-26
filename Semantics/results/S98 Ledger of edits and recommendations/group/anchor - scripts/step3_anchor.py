"""Step 3: anchor every collected record to the sentences of the latest text, name its terms, join duplicates."""
import json, sys, os, re, bisect
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import *

MAPS = json.load(open(GROUP + '/line maps.json', encoding='utf-8'))
TO_LATEST = {v: {int(k): d for k, d in m.items()} for v, m in MAPS['to_latest'].items()}
INV = {}
for v, m in TO_LATEST.items():
    inv = {}
    for k, d in m.items():
        if d['latest'] is not None and d['latest'] not in inv:
            inv[d['latest']] = k
    INV[v] = inv

TEXTS = {k: lines_of(k) for k in CHAIN}
LX = Indexed('latest')
UNITS = LX.units
UID = {u['id']: j for j, u in enumerate(UNITS)}
LAT = TEXTS['latest']
OFF = [0]
for l in LAT:
    OFF.append(OFF[-1] + len(l) + 1)
JOINED = '\n'.join(LAT)
for u in UNITS:
    u['g0'] = OFF[u['line'] - 1] + u['start']
    u['g1'] = OFF[u['line_end'] - 1] + u['end']
USTARTS = [u['g0'] for u in UNITS]
LATEST_PARTS = dict(LX.part_titles)


# ---------- normalised search with a position map ----------
QMAP = {'’': "'", '‘': "'", '“': '"', '”': '"'}


def build_norm(text, quotes=True):
    out, pos = [], []
    i, n = 0, len(text)
    prev_space = False
    while i < n:
        if text.startswith('<u>', i):
            i += 3; continue
        if text.startswith('</u>', i):
            i += 4; continue
        c = text[i]
        if c.isspace():
            if not prev_space:
                out.append(' '); pos.append(i)
            prev_space = True
            i += 1
            continue
        prev_space = False
        out.append(QMAP.get(c, c) if quotes else c)
        pos.append(i)
        i += 1
    return ''.join(out), pos


NORM_CACHE = {}


def normed(key):
    if key not in NORM_CACHE:
        NORM_CACHE[key] = build_norm('\n'.join(TEXTS[key]))
    return NORM_CACHE[key]


def line_of(key, gpos):
    if key == 'latest':
        return bisect.bisect_right(OFF, gpos)
    offs = OFFS[key]
    return bisect.bisect_right(offs, gpos)


OFFS = {}
for k in CHAIN:
    o = [0]
    for l in TEXTS[k]:
        o.append(o[-1] + len(l) + 1)
    OFFS[k] = o


def find_all(key, s):
    """All (start, end) original offsets of s in text key, whitespace and quotes normalised."""
    q, _ = build_norm(s)
    q = q.strip()
    if not q:
        return []
    nt, pos = normed(key)
    res, i = [], nt.find(q)
    while i >= 0:
        a = pos[i]
        b = pos[i + len(q) - 1] + 1
        res.append((a, b))
        i = nt.find(q, i + 1)
    return res


def units_overlapping(a, b):
    j = bisect.bisect_right(USTARTS, a) - 1
    j = max(j, 0)
    out = []
    while j < len(UNITS) and UNITS[j]['g0'] < b:
        u = UNITS[j]
        if u['g1'] > a and u['g0'] < b:
            out.append(j)
        j += 1
    return out


def lines_to_units(lines):
    out = []
    for ln in lines:
        for j in LX.by_line.get(ln, []):
            if j not in out:
                out.append(j)
    return out


# ---------- versions named by the records ----------

def target_version(r):
    t = r['target_text']
    if t.startswith('file 10') or t.startswith('file 20'):
        return 'f10'
    if t.startswith('file 11'):
        return 'f11'
    if t.startswith('file 12'):
        return 'f12'
    if t.startswith('the note') or t.startswith('change list, draft 5 state'):
        return 'note'
    mo = re.match(r'file 13 draft (\d)', t)
    if mo:
        return 'd' + mo.group(1)
    if t == 'draft 5':
        return 'd5'
    if t.startswith('scrubbed copy'):
        return 'scrubbed'
    if t.startswith('repaired copy'):
        return 'repaired'
    if t.startswith('stage-1 text'):
        return 'stage1'
    return None


def applied_version(r):
    a = r['applied_in']
    if not a or a.startswith('none') or a.startswith('file 20'):
        return None
    for pat, k in [(r'draft 1\b', 'd1'), (r'draft 2\b', 'd2'), (r'draft 3\b', 'd3'), (r'draft 4\b', 'd4'),
                   (r'draft 5\b', 'd5'), (r'^file 11', 'f11'), (r'^scrubbed copy', 'scrubbed'),
                   (r'^repaired copy', 'repaired'), (r'^latest text', 'latest')]:
        if re.search(pat, a):
            return k
    return None


def chain_key(v):
    return {'stage1': 'repaired'}.get(v, v)


def to_latest(v, line):
    v = chain_key(v)
    if v not in TO_LATEST or line is None:
        return None
    return TO_LATEST[v].get(int(line))


PLACEHOLDER = '[no wording given]'


def real(s):
    return bool(s) and not s.startswith(PLACEHOLDER) and s.strip() != ''


def locate_line(v, s):
    """First line of s in version v (chain versions only)."""
    v = chain_key(v)
    if v not in TEXTS or not real(s) or len(s.strip()) < 12:
        return []
    return sorted({line_of(v, a) for a, b in find_all(v, s)})


ROM = re.compile(r'Part ([0IVXL]+)\b')


def roman_of(part):
    mo = ROM.search(part or '')
    return mo.group(1) if mo else None


# ---------- terms ----------

def term_list():
    terms = {}   # term -> kind
    t = JOINED
    skip_inline = {'A premise that is the denial.', 'Conflict with a claim.', 'Construction:', 'Premises taken as given.',
                   'Selection:', 'plus a selection or construction history'}
    for l in LAT:
        for m in re.finditer(r'\*\*(.+?)\*\*', l):
            x = m.group(1).strip()
            lead = l[:m.start()].strip() == ''
            if not lead and x not in skip_inline:
                x = re.sub(r'\\\(([^)]*)\\\)', lambda mo: '', x).strip()
                x = re.sub(r'\s+on$|\s+for$|\s+given$', '', x).strip()
                if x:
                    terms.setdefault(x, 'defined in the latest text')
    label_terms = ['Component fidelity', 'Question fidelity', 'Non-circular dependence', 'Non-vacuity', 'Bearing',
                   'Usability', 'Rivals', 'Problems', 'Achievement', 'Tasks', 'Histories', 'Episodes', 'Ownership',
                   'Owned capability', 'Newness', 'Origin', 'Repair', 'Appraisal', 'Recoding', 'Deployment',
                   'Membership', 'Scrutinizability', 'Universality', 'Recursive capacity', 'Tolerances', 'Barriers',
                   'Interference', 'Retention fixed point', 'Retained realization', 'Declared inputs', 'Imports',
                   'Historical index', 'Consequence', 'Relational transport', 'Functional transport',
                   'Approximate transport', 'Infinitary routes', 'Redundant routes', 'Dependence order',
                   'Created explanation', 'Reason use', 'Finite monotone claim', 'Tasks', 'Selected', 'Constructed']
    for x in label_terms:
        terms.setdefault(x, 'defined in the latest text (run-in label)')
    for tag in ['K3', 'CT2', 'CA']:
        terms.setdefault('(%s)' % tag, 'defined in the latest text (labelled condition)')
    for tag in sorted(set(re.findall(r'\\tag\{([^}]+)\}', t))):
        if len(tag) >= 2:
            terms.setdefault('(%s)' % tag, 'defined in the latest text (tagged condition)')
    # old names the S95 vocabulary replaced (the draft 5 column of the vocabulary as used)
    voc = read('tests/S95 Scrub - vocabulary, as used.md').split('\n')
    drop = {"a condition's exclusion", 'establish where no assessor is meant', 'proof as mathematics',
            'l', 'P_j(φ)', 'N_j(φ)', 'Lic_j(u)', 'Standing (K2)', 'witness (construction)', 'witness (mathematics)',
            'primitive(s)', 'primitive 2', 'Derivation 1–10', '*Proof.*', 'understanding (Part X)',
            'surprise (Part IV)', 'worth (everywhere)', 'truth (objection', 'axiom (l. 49)', 'licensed (l. 608)',
            'accept (l. 67)', 'permitted (l. 13', 'Explanatory realism (l. 67)', 'right', 'holds (satisfaction)',
            'true or false (a predicate)', 'establish (a test)', 'ground', 'grounded (l. 159', 'strength (l. 277)',
            'knowledge: (EK)', 'CreateEK', 'obligation(s) (Part XI)', 'physical obligations (l. 45'}
    for l in voc:
        if not l.startswith('| ') or l.startswith('| draft 5') or l.startswith('|---'):
            continue
        cell = l.strip('|').split(' | ')[0].strip()
        for item in re.split(r';|,', cell):
            item = item.strip()
            if not item or '"' in item or item in drop:
                continue
            item = re.sub(r'\s*\(.*$', '', item).strip()
            item = item.replace('*', '').strip()
            if not item or item in drop or len(item.split()) > 4 or item.startswith('l.') or item.startswith('…'):
                continue
            if re.search(r'[_\\(]', item):
                continue
            terms.setdefault(item, 'old name replaced by the S95 vocabulary')
    for x in ['witness', 'primitive', 'primitives', 'derivation', 'derivations', 'theorem', 'proof', 'axiom',
              'licensed', 'permitted', 'knowledge', 'normative relation', 'epistemic obligation', 'obligation',
              'ground', 'grounded', 'truth', 'true', 'right', 'standing', 'expectation', 'worth', 'verdict']:
        terms.setdefault(x, 'old name replaced by the S95 vocabulary')
    # tidy: no line numbers, one entry per word whatever its case or inflection
    terms = {k: v for k, v in terms.items() if not re.search(r'\d|\)', k.replace('(F1)', '').replace('(F2)', '')) or k.startswith('(')}
    terms = {k: v for k, v in terms.items() if not (re.search(r'\d|\)', k) and not k.startswith('('))}
    out = {}
    for k in sorted(terms, key=lambda x: (len(x), x.lower() != x)):
        low = k.lower()
        dup = False
        for o in out:
            ol = o.lower()
            if low == ol or low in (ol + 's', ol + 'es', ol + 'd', ol + 'ed') or low == ol + ' from':
                dup = True
                break
        if not dup:
            # a defined term keeps its defined kind over an old-name kind
            out[k] = terms[k]
        else:
            if 'defined' in terms[k] and 'old name' in out.get(o, ''):
                out[o] = terms[k]
    return out


TERMS = term_list()
TERM_RE = []
for x in sorted(TERMS, key=lambda s: -len(s)):
    if x.startswith('('):
        rx = re.compile(re.escape(x))
    else:
        body = r'\s+'.join(re.escape(w) for w in x.split())
        rx = re.compile(r'(?<![A-Za-z])' + body + r'(?:s|es|d|ed)?(?![A-Za-z])', re.I)
    TERM_RE.append((x, rx))


def terms_in(*texts):
    found = []
    blob = ' \n '.join(t for t in texts if t)
    blob = blob.replace('**', '')
    for x, rx in TERM_RE:
        if rx.search(blob):
            found.append(x)
    return sorted(found, key=str.lower)


# ---------- term records ----------

def keys_of(cell):
    cell = cell or ''
    if cell.startswith(PLACEHOLDER):
        return []
    ks = re.findall(r'\*\*(.+?)\*\*', cell)
    ks += re.findall(r'"([^"]{3,80})"', cell)
    head = re.sub(r'\([^)]*\)', '', cell)
    head = re.sub(r'"[^"]*"', '', head)
    head = re.sub(r'\*\*[^*]*\*\*', '', head)
    for item in re.split(r'[;,:]', head):
        item = item.strip(' .…').replace('*', '')
        if 2 <= len(item) <= 60 and len(item.split()) <= 6 and not item.startswith('l.'):
            ks.append(item)
    out = []
    bad = {'dropped', 'kept', 'keep', 'keep: the real numbers', 'BORDERLINE', 'differs from the sceptic', 'provisional',
           'the', 'and', 'or', 'l'}
    for k in ks:
        k = k.strip(' .…')
        k = re.sub(r'\s*…\s*', ' ', k).strip()
        if k and k not in bad and not k.lower().startswith('claude') and len(k) >= 3 and k not in out:
            out.append(k)
    return out


def line_refs(*cells):
    out = []
    for c in cells:
        for mo in re.finditer(r'\bl\. (\d+)(?:[–-](\d+))?((?:, \d+)*)', c or ''):
            a = int(mo.group(1))
            b = int(mo.group(2)) if mo.group(2) else a
            if b - a <= 40:
                out += list(range(a, b + 1))
            for x in re.findall(r'\d+', mo.group(3) or ''):
                out.append(int(x))
    return sorted(set(out))


def key_rx(k):
    body = r'\s+'.join(re.escape(w) for w in k.split())
    return re.compile(r'(?<![A-Za-z])' + body, re.I)


def unit_has(j, keys):
    t = UNITS[j]['text'].replace('**', '')
    return any(key_rx(k).search(t) for k in keys)


def frags(cell, minlen=10):
    """Quoted phrases of a vocabulary cell, cut at ellipses."""
    out = []
    for q in re.findall(r'"([^"]+)"', cell or ''):
        for piece in re.split(r'\s*…\s*|\.\.\.', q):
            piece = piece.strip(' .,;:')
            if len(piece) >= minlen and piece not in out:
                out.append(piece)
    return out


IDX_CACHE = {}


def indexed(v):
    if v not in IDX_CACHE:
        IDX_CACHE[v] = Indexed(v)
    return IDX_CACHE[v]


def old_places(base, keys, limit=60):
    """Sentences of the base text holding one of the keys, mapped to the most similar unit on the mapped latest line."""
    ix = indexed(base)
    hits = []
    for u in ix.units:
        if u['kind'] == 'heading':
            t = u['text']
        else:
            t = u['text']
        t = t.replace('**', '')
        if any(key_rx(k).search(t) for k in keys):
            hits.append(u)
    if not hits or len(hits) > limit:
        return [], len(hits)
    out = []
    for u in hits:
        d = to_latest(base, u['line'])
        if not d or not d['latest']:
            continue
        cand = lines_to_units([d['latest']])
        if not cand:
            continue
        bj = max(cand, key=lambda j: ratio(u['text'], UNITS[j]['text']))
        if bj not in out:
            out.append(bj)
    return out, len(hits)


def anchor_term(r, tv):
    nk, ok = keys_of(r['new']), keys_of(r['old'])
    nf, of_ = frags(r['new']), frags(r['old'])
    refs = line_refs(r['old'], r['new'])
    applied = r['status'] == 'applied'
    first, second = (nk, ok) if applied else (ok, nk)
    base = chain_key(tv) if tv in ('d5', 'scrubbed', 'repaired', 'stage1', 'f11', 'd1', 'd2', 'd3', 'd4', 'f10') else None
    # A. the lines the entry names
    if refs and base:
        lat = []
        for ln in refs:
            d = to_latest(base, ln)
            if d and d['latest']:
                lat.append(d['latest'])
        cand = lines_to_units(lat)
        for keys, what in ((first, 'new' if applied else 'old'), (second, 'old' if applied else 'new')):
            hit = [j for j in cand if keys and unit_has(j, keys)]
            if hit:
                return hit, 'term: the lines the entry names, sentences holding its %s words' % what
        if cand:
            return [j for j in cand if UNITS[j]['kind'] != 'heading'] or cand, 'term: the lines the entry names (the whole paragraph)'
    # B. a phrase the entry quotes as its new wording, found in the latest text
    if applied and nf:
        hit = []
        for q in nf:
            for a, b in find_all('latest', q):
                for j in units_overlapping(a, b):
                    if j not in hit:
                        hit.append(j)
        if hit and len(hit) <= 40:
            return hit, 'term: a phrase the entry quotes as new wording, found in the latest text'
    # C. the places where the old words stood in the target text, carried to the latest text
    if base:
        keys = of_ + [k for k in ok if k not in of_]
        if keys:
            hit, n = old_places(base, keys)
            if hit:
                return hit, 'term: the %d places where its old words stood in %s, carried to the latest text' % (n, VLABEL.get(base, base))
    # D. places where the new words stand now and the old words stood in the target text
    if base and nk and ok and applied:
        hit = []
        for j, u in enumerate(UNITS):
            if unit_has(j, nk):
                vl = INV.get(base, {}).get(u['line'])
                if vl:
                    old_line = TEXTS[base][vl - 1].replace('**', '')
                    if any(key_rx(k).search(old_line) for k in ok):
                        hit.append(j)
        if hit:
            return hit, 'term: sentences holding the new words whose line in the target text held the old words'
    if not applied:
        for keys, what in ((ok, 'old'), (nk, 'new')):
            hit = [j for j in range(len(UNITS)) if keys and unit_has(j, keys)]
            if hit and len(hit) <= 60:
                return hit, 'term: sentences of the latest text holding its %s words' % what
    if r['target_line'] and base:
        d = to_latest(base, r['target_line'])
        if d and d['latest']:
            cand = lines_to_units([d['latest']])
            hit = [j for j in cand if unit_has(j, nk + ok)]
            if hit:
                return hit, 'term: the target line, sentences holding its words'
    return [], None


# ---------- the anchoring of one record ----------

def best_on_lines(r, lines):
    cand = lines_to_units(lines)
    heads = any(real(x) and x.lstrip().startswith('#') for x in (r['old'], r['new'], r['old_sentence'], r['new_sentence']))
    if heads:
        cand = [j for j in cand if UNITS[j]['kind'] == 'heading'] or cand
    else:
        cand = [j for j in cand if UNITS[j]['kind'] != 'heading'] or cand
    if not cand:
        return [], 0.0
    newrefs = [(s, full) for s, full in ((r['new_sentence'], True), (r['new'], False)) if real(s) and len(s.strip()) >= 8]
    oldrefs = [(s, full) for s, full in ((r['old_sentence'], True), (r['old'], False)) if real(s) and len(s.strip()) >= 8]
    if len(newrefs) == 2 and norm(newrefs[0][0]) == norm(newrefs[1][0]):
        newrefs = newrefs[:1]
    if len(oldrefs) == 2 and norm(oldrefs[0][0]) == norm(oldrefs[1][0]):
        oldrefs = oldrefs[:1]
    if not newrefs and not oldrefs:
        return cand, 0.0
    first, second = (newrefs, oldrefs) if r['status'] == 'applied' else (oldrefs, newrefs)

    def best_of(refs):
        best, bj = -1.0, None
        for j in cand:
            for s, full in refs:
                x = ratio(s, UNITS[j]['text']) if full else contain_ratio(s, UNITS[j]['text'])
                if x > best:
                    best, bj = x, j
        return best, bj
    best, bj = best_of(first) if first else (-1.0, None)
    if best < 0.35 and second:
        b2, j2 = best_of(second)
        if b2 > best:
            best, bj = b2, j2
    return [bj], round(best, 3)


def search_latest(s, hint, near=2, strict=False):
    """Units holding s. Short strings only near the hint line; with strict, any string only within 5 lines of it."""
    occ = find_all('latest', s)
    if not occ:
        return [], ''
    lines = [line_of('latest', a) for a, b in occ]
    if strict and hint is not None:
        keep = [(o, ln) for o, ln in zip(occ, lines) if abs(ln - hint) <= 5]
        if not keep:
            return [], ''
        occ = [o for o, ln in keep]
        lines = [ln for o, ln in keep]
    if len(s.strip()) < 25:
        if hint is None:
            return [], ''
        occ = [o for o, ln in zip(occ, lines) if abs(ln - hint) <= near]
        if not occ:
            return [], ''
        occ = [min(occ, key=lambda o: abs(line_of('latest', o[0]) - hint))]
        how = 'near the mapped line'
    elif len(occ) > 1:
        if hint is not None:
            occ = [min(occ, key=lambda o: abs(line_of('latest', o[0]) - hint))]
            how = 'nearest of %d places to the mapped line' % len(lines)
        else:
            how = 'all %d places' % len(occ)
    else:
        how = 'one place'
    out = []
    for a, b in occ:
        for j in units_overlapping(a, b):
            if j not in out:
                out.append(j)
    return out, how


def global_fuzzy(r, roman):
    refs = [s for s in (r['new_sentence'], r['new'], r['old_sentence'], r['old']) if real(s) and len(s.strip()) >= 30]
    if not refs:
        return [], 0.0
    cand = [j for j, u in enumerate(UNITS) if u['kind'] != 'heading' and (roman is None or roman_of(u['part']) == roman)]
    best, bj = 0.0, None
    for s in refs:
        ls = loose(s)
        for j in cand:
            lt = loose(UNITS[j]['text'])
            sm = difflib.SequenceMatcher(None, ls, lt, autojunk=False)
            if sm.real_quick_ratio() < 0.55 or sm.quick_ratio() < 0.55:
                continue
            x = sm.ratio()
            if x > best:
                best, bj = x, j
    return ([bj] if bj is not None else []), round(best, 3)


PLACE_RX = [
    (re.compile(r'file-11 (?:line |L)(\d+)(?:[-–](\d+))?'), 'f11'),
    (re.compile(r'draft 5 L(\d+)(?:[-–](\d+))?'), 'd5'),
]


def declared_place(r):
    """A note record that names the theory place it declares: (version, [lines])."""
    for field in (r['target_part'], r['source_ref']):
        for rx, v in PLACE_RX:
            mo = rx.search(field or '')
            if mo:
                a = int(mo.group(1))
                b = int(mo.group(2)) if mo.group(2) else a
                return v, list(range(a, b + 1))
    return None


def is_note(r, tv):
    tp = r['target_part'] or ''
    if tv == 'note':
        return True
    if tp.startswith('Note of sources') or tp.startswith('Change list entry W38.1'):
        return True
    if "revision note" in tp or (tp.startswith('Front matter') and 'note' in tp.lower()):
        return True
    ai = r['applied_in'] or ''
    if 'meta block' in ai and tp.startswith('Front matter'):
        return True
    return False


def anchor(r):
    tv = target_version(r)
    av = applied_version(r)
    info = {'target_version': tv}
    # places outside the theory text
    if tv == 'f12':
        return dict(info, sentences=[], status='not locatable', reason='file 12 is a separate text (the causality text); the latest text does not hold it', method=None)
    if is_note(r, tv):
        dp = declared_place(r)
        if dp:
            v, lns = dp
            lat = [d['latest'] for d in (to_latest(v, ln) for ln in lns) if d and d['latest']]
            if lat and not [j for j in lines_to_units(lat) if UNITS[j]['kind'] != 'heading']:
                # the place is a rule or blank line: take the nearest paragraph before it, else after it
                for step in (-1, -2, -3, 1, 2, 3):
                    near = [ln + step for ln in lat]
                    if [j for j in lines_to_units(near) if UNITS[j]['kind'] != 'heading']:
                        lat = near
                        break
            if lat:
                js, x = best_on_lines(r, lat)
                if not js or x < 0.25:
                    js = [j for j in lines_to_units(lat) if UNITS[j]['kind'] != 'heading']
                    how = 'a declaration in the note about the place at %s line %s; the whole paragraph now there' % (VLABEL[v], lns[0])
                else:
                    how = 'a declaration in the note about the place at %s line %s; the most similar sentence now there' % (VLABEL[v], lns[0])
                return dict(info, sentences=js, status='anchored', method=how, ratio=x if js else None, new_in_latest='n/a', hint=lat[0], hint_how='declared place')
        return dict(info, sentences=[], status='not locatable', reason='the change is to a note (the revision note, the note of sources and departures, or the revision record); the theory texts after file 11 carry no such note', method=None)
    if r['scope'] == 'whole text':
        return dict(info, sentences=[], status='not locatable', reason='a change to the whole text, with no one place', method=None)

    # the hint: where the place of the change stands in the latest text
    hint, hint_how, lost = None, '', None

    def from_new():
        if not av:
            return None
        for s in (r['new_sentence'], r['new']):
            ls = locate_line(av, s)
            if len(ls) == 1:
                d = to_latest(av, ls[0])
                if d:
                    return d['latest'], (None if d['latest'] else d['last_present_in']), 'new wording found at line %d of %s' % (ls[0], av)
        return None

    def from_target():
        if r['target_line'] is not None and chain_key(tv) in TO_LATEST:
            d = to_latest(tv, r['target_line'])
            if d:
                return d['latest'], (None if d['latest'] else d['last_present_in']), 'target line %s of %s' % (r['target_line'], tv)
        return None

    def from_old():
        for s in (r['old_sentence'], r['old']):
            ls = locate_line(tv, s) if tv else []
            if len(ls) == 1:
                d = to_latest(tv, ls[0])
                if d:
                    return d['latest'], (None if d['latest'] else d['last_present_in']), 'old wording found at line %d of %s' % (ls[0], tv)
        return None

    def from_applied_line():
        mo = re.search(r'line (\d+)', r['applied_in'] or '')
        if (r['applied_in'] or '').startswith('file 11') and mo:
            d = to_latest('f11', int(mo.group(1)))
            if d:
                return d['latest'], (None if d['latest'] else d['last_present_in']), 'the line of file 11 its applied_in names (%s)' % mo.group(1)
        return None

    def from_ref():
        mo = re.search(r'\bf11 L(\d+)', r['source_ref'] or '')
        if mo and r['rid'].startswith('B-') and r['kind'] == 'edit':
            d = to_latest('f11', int(mo.group(1)))
            if d:
                return d['latest'], (None if d['latest'] else d['last_present_in']), 'the file-11 line its source_ref names (%s)' % mo.group(1)
        return None

    order = (from_new, from_ref, from_applied_line, from_target, from_old) if (av and r['status'] == 'applied') else (from_target, from_old, from_applied_line)
    for fn in order:
        h = fn()
        if h:
            hint, lost, hint_how = h
            break
    info['hint'] = hint
    info['hint_how'] = hint_how

    if r['scope'] == 'term':
        js, how = anchor_term(r, tv)
        if js:
            return dict(info, sentences=js, status='anchored', method=how, ratio=None,
                        new_in_latest='n/a')
        return dict(info, sentences=[], status='not locatable' if r['status'] == 'applied' else 'never applied',
                    reason='a vocabulary entry whose words could not be placed on sentences of the latest text', method=None)

    # 1. the new wording, verbatim
    applied = r['status'] == 'applied'
    for s, what in ((r['new_sentence'], 'new sentence'), (r['new'], 'new wording')):
        if real(s):
            js, how = search_latest(s, hint, strict=(what == 'new wording' or not applied))
            if js:
                return dict(info, sentences=js, status='anchored', method='%s verbatim in the latest text (%s)' % (what, how),
                            ratio=1.0, new_in_latest='yes')
    new_in = 'no' if real(r['new']) else 'n/a'
    # 2. the old wording, verbatim (the place still reads as before)
    for s, what in ((r['old_sentence'], 'old sentence'), (r['old'], 'old wording')):
        if real(s):
            js, how = search_latest(s, hint, strict=(what == 'old wording'))
            if js:
                return dict(info, sentences=js, status='anchored', method='%s verbatim in the latest text (%s)' % (what, how),
                            ratio=1.0, new_in_latest=new_in)
    # 3. the mapped line
    roman = roman_of(r['target_part'])
    if hint is not None:
        js, x = best_on_lines(r, [hint])
        how = 'line map (%s), most similar sentence on that line' % hint_how
        if js and x == 0.0:
            return dict(info, sentences=js, status='anchored',
                        method='line map (%s), the paragraph on that line (the record gives no wording to compare)' % hint_how,
                        ratio=None, new_in_latest=new_in)
        if js and x < 0.5:
            js2, x2 = best_on_lines(r, list(range(hint - 2, hint + 3)))
            if js2 and x2 > x + 0.1:
                js, x = js2, x2
                how = 'line map (%s), most similar sentence within two lines of it' % hint_how
        if js and x < 0.5:
            g, gx = global_fuzzy(r, roman)
            if g and gx >= 0.6 and gx > x + 0.15:
                return dict(info, sentences=g, status='anchored',
                            method='most similar sentence in %s (the mapped line holds none as close)' % (('Part ' + roman) if roman else 'the latest text'),
                            ratio=gx, new_in_latest=new_in)
        if js:
            if x >= 0.25:
                return dict(info, sentences=js, status='anchored', method=how, ratio=x, new_in_latest=new_in)
            allj = [j for j in lines_to_units([hint]) if UNITS[j]['kind'] != 'heading'] or js
            return dict(info, sentences=allj, status='anchored',
                        method='line map (%s); no sentence on that line is close, so the whole paragraph' % hint_how,
                        ratio=x, new_in_latest=new_in)
    # 4. similarity over the latest text (inside the Part named, if any)
    js, x = global_fuzzy(r, roman)
    if js and x >= 0.6:
        return dict(info, sentences=js, status='anchored',
                    method='most similar sentence in %s (difflib ratio)' % (('Part ' + roman) if roman else 'the latest text'),
                    ratio=x, new_in_latest=new_in)
    if lost:
        return dict(info, sentences=[], status='removed',
                    reason='its place (%s) was last present in %s and is gone from the text after it; no sentence of the latest text is similar (highest ratio %.2f)' % (hint_how, VLABEL.get(lost, lost), x),
                    method=None, lost_after=lost)
    why = 'no wording to search for' if not any(real(s) for s in (r['new'], r['old'], r['new_sentence'], r['old_sentence'])) else \
        'no line to map and no sentence of the latest text is similar enough (highest ratio %.2f)' % x
    st = 'never applied' if r['status'] != 'applied' else 'not locatable'
    return dict(info, sentences=[], status=st, reason=why, method=None)


# ---------- run ----------
recs = []
for c in 'ABCDE':
    with open(COLLECT + '/collector %s.jsonl' % c, encoding='utf-8') as f:
        for l in f:
            recs.append(json.loads(l))
RID = {r['rid']: i for i, r in enumerate(recs)}

results = []
for i, r in enumerate(recs):
    a = anchor(r)
    results.append(a)
    if i % 200 == 0:
        print('..', i, file=sys.stderr)

# ---------- duplicates: one change seen in several sources ----------
parent = list(range(len(recs)))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b, why):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[max(ra, rb)] = min(ra, rb)
    JOIN_WHY[(min(a, b), max(a, b))] = why


JOIN_WHY = {}
# change-list entries held by collector C (entry id -> rid)
CL_ENTRY = {}
WL_ITEM = {}
for i, r in enumerate(recs):
    if r['rid'].startswith('C-'):
        mo = re.match(r'change list draft 5, entry (W[^ ]+) ', r['source_ref'])
        if mo:
            CL_ENTRY.setdefault(mo.group(1), []).append(i)
external = []
for i, r in enumerate(recs):
    for s in r['same_as']:
        if s in RID:
            union(i, RID[s], 'same_as')
        elif '#' in s:
            path, key = s.split('#', 1)
            parts = [k.strip() for k in key.split('+')]
            hit = [k for k in parts if k in CL_ENTRY]
            if path.endswith('change list, draft of 23 September.md') and hit:
                for k in hit:
                    for j in CL_ENTRY[k]:
                        union(i, j, 'same_as (change-list entry %s)' % k)
            else:
                external.append((r['rid'], s))


def nkey(s):
    return re.sub(r'\s+', ' ', norm(s)).strip()


groups = defaultdict(list)
for i, r in enumerate(recs):
    if not real(r['new']) and not real(r['old']):
        continue
    if r['new'].startswith(PLACEHOLDER):
        continue
    o, n = nkey(r['old']), nkey(r['new'])
    groups[(r['scope'] == 'term', o, n)].append(i)


def place_of(i):
    """Where a record's change sits: its latest sentences, else its target line."""
    a = results[i]
    if a['sentences']:
        return {('s', UNITS[j]['id']) for j in a['sentences']}
    if recs[i]['target_line'] is not None:
        return {('t', a.get('target_version'), recs[i]['target_line'])}
    return None


for k, v in groups.items():
    if len(v) < 2:
        continue
    is_term = k[0]
    if is_term:
        for j in v[1:]:
            union(v[0], j, 'same old and new (vocabulary entry)')
        continue
    placed = [(i, place_of(i)) for i in v]
    known = [(i, p) for i, p in placed if p]
    # records whose places overlap are one change
    for x in range(len(known)):
        for y in range(x + 1, len(known)):
            if known[x][1] & known[y][1]:
                union(known[x][0], known[y][0], 'same old and new, same place')
    # a record with no place joins only when the others have one place between them
    roots_known = {find(i) for i, p in known}
    unplaced = [i for i, p in placed if not p]
    if unplaced and len(roots_known) <= 1:
        anchor_i = known[0][0] if known else unplaced[0]
        for i in unplaced:
            if i != anchor_i:
                union(anchor_i, i, 'same old and new (one has no place)')

comp = defaultdict(list)
for i in range(len(recs)):
    comp[find(i)].append(i)
roots = sorted(comp, key=lambda x: min(comp[x]))
CID = {}
for n, root in enumerate(roots, 1):
    for i in comp[root]:
        CID[i] = 'CH-%04d' % n

# a record with no place takes the place of the most similar record of the same change
for root in roots:
    members = comp[root]
    placed = [i for i in members if results[i]['sentences']]
    for i in members:
        why = results[i].get('reason') or ''
        keep_out = ('note' in why) or ('separate text' in why) or ('whole text' in why)
        if not results[i]['sentences'] and placed and not keep_out:
            def sim(j):
                x = 0.0
                for f in ('new', 'old', 'new_sentence', 'old_sentence'):
                    if real(recs[i][f]) and real(recs[j][f]):
                        x = max(x, ratio(recs[i][f], recs[j][f]))
                return x
            src = max(placed, key=sim)
            results[i] = dict(results[i], sentences=list(results[src]['sentences']), status='anchored',
                              method='same change as %s' % recs[src]['rid'], ratio=None,
                              new_in_latest=results[i].get('new_in_latest', 'n/a'), reason=None,
                              was=results[i]['status'])

# ---------- the nearest sentence, for records left without a place ----------
STOP = set(('the a an of to in and or is are be by for on at as that this it its with from not no any one two which when '
            'where whose there their than then so if only each every same other under into between does do has have was '
            'were been being can may must would could should all some more most such these those what who how also but '
            'nor own').split())


def words(s):
    s = loose(s)
    s = re.sub(r'\\\(.*?\\\)', ' ', s)
    return {w for w in re.findall(r'[A-Za-z][A-Za-z-]+', s.lower()) if w not in STOP and len(w) > 2}


UW = [words(u['text']) for u in UNITS]
NEAREST = {}
for i, r in enumerate(recs):
    a = results[i]
    if a['sentences'] or a['status'] == 'not locatable' and ('note' in (a.get('reason') or '') or 'separate text' in (a.get('reason') or '')):
        continue
    ref = ' '.join(x for x in (r['new_sentence'] if real(r['new_sentence']) else r['new'] if real(r['new']) else '',
                               r['old_sentence'] if real(r['old_sentence']) else r['old'] if real(r['old']) else '') if x)
    ws = words(ref)
    if len(ws) < 3:
        continue
    roman = roman_of(r['target_part'])
    best = (0.0, None)
    for j, u in enumerate(UNITS):
        if u['kind'] == 'heading' or not UW[j]:
            continue
        if roman and roman_of(u['part']) != roman:
            continue
        inter = len(ws & UW[j])
        if not inter:
            continue
        x = 0.5 * inter / len(ws) + 0.5 * inter / len(ws | UW[j])
        if x > best[0]:
            best = (x, j)
    if best[1] is not None and best[0] >= 0.15:
        NEAREST[i] = (UNITS[best[1]]['id'], round(best[0], 3))

# ---------- write ----------
out_path = GROUP + '/anchored.jsonl'
with open(out_path, 'w', encoding='utf-8') as f:
    for i, r in enumerate(recs):
        a = results[i]
        js = sorted(set(a['sentences']))
        units = [UNITS[j] for j in js]
        o = dict(r)
        o['latest_sentences'] = [u['id'] for u in units]
        o['latest_status'] = a['status']
        if a['status'] != 'anchored':
            o['latest_reason'] = a.get('reason')
        if units:
            u0 = units[0]
            o['latest_part'] = u0['part']
            o['latest_heading'] = LX.heading_path(u0)
            o['latest_parts'] = sorted({u['part'] for u in units}, key=lambda p: [x['part'] for x in UNITS].index(p))
            o['latest_lines'] = sorted({u['line'] for u in units})
        else:
            roman = roman_of(r['target_part'])
            lost = a.get('lost_after')
            if lost and r['target_line'] is not None:
                # the Part the line stood in, in the last text that held it
                pass
            o['latest_part'] = LATEST_PARTS.get(roman, '') if roman else ('Front matter (before Part 0)' if 'Front matter' in (r['target_part'] or '') else '')
            sub = (r['target_part'] or '').split(' / ', 1)[1] if ' / ' in (r['target_part'] or '') else ''
            head = ''
            if sub and roman:
                for u in UNITS:
                    if roman_of(u['part']) == roman and (u['heading'] == sub or u['label'] == sub.rstrip('.')):
                        head = LX.heading_path(u)
                        break
            o['latest_heading'] = head
            romans = re.findall(r'Part ([0IVXL]+)\b', r['target_part'] or '')
            o['latest_parts'] = [LATEST_PARTS[x] for x in dict.fromkeys(romans) if x in LATEST_PARTS] or ([o['latest_part']] if o['latest_part'] else [])
            o['latest_lines'] = [a['hint']] if a.get('hint') else []
        if i in NEAREST:
            o['latest_nearest'] = {'sentence': NEAREST[i][0], 'word_overlap': NEAREST[i][1],
                                   'note': 'the latest-text sentence sharing most content words with the record, in the Part named; not an anchor'}
        o['anchor_method'] = a.get('method')
        o['anchor_ratio'] = a.get('ratio')
        o['new_in_latest'] = a.get('new_in_latest', 'n/a')
        o['target_version'] = a.get('target_version')
        o['terms'] = terms_in(r['old'], r['new'])
        o['change_id'] = CID[i]
        o['change_members'] = [recs[j]['rid'] for j in sorted(comp[find(i)])]
        f.write(json.dumps(o, ensure_ascii=False) + '\n')

json.dump({'terms': TERMS, 'external_same_as': external,
           'joins': [[recs[a]['rid'], recs[b]['rid'], w] for (a, b), w in sorted(JOIN_WHY.items())]},
          open(GROUP + '/anchor - scripts/step3 side data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('records', len(recs))
print(Counter(a['status'] for a in results))
print('changes', len(roots), 'largest', sorted((len(v) for v in comp.values()), reverse=True)[:10])
