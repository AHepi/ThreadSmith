#!/usr/bin/env python3
"""S100: strong candidates and the most altered sections, by program.

Reads the S98 ledger (records, tree, sentence index, line maps, term list) and the ten theory texts of the
chain file 10 -> file 11 -> drafts 1-5 -> scrubbed copy -> repaired copy -> latest text. Writes two files beside
this script: the analysis page and the data table. Nothing else is written; no input is changed.

Run: PYTHONDONTWRITEBYTECODE=1 python3 "S100 Strong candidates and the most altered sections - script.py"
"""
import sys, os, json, re, csv, hashlib, difflib, statistics
from collections import Counter, defaultdict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = '/home/user/ThreadSmith/Semantics'
LED = SEM + '/results/S98 Ledger of edits and recommendations'
sys.path.insert(0, LED + '/group/anchor - scripts')
from lib_anchor import norm, loose, ratio, contain_ratio, split_sents, Indexed, CHAIN, VLABEL, VPATH  # noqa: E402

NAME = 'S100 Strong candidates and the most altered sections'
OUT_MD = os.path.join(HERE, NAME + '.md')
OUT_CSV = os.path.join(HERE, NAME + ' - data.csv')
SCRIPT = NAME + ' - script.py'

INPUTS = {
    LED + '/line-up/data/records.jsonl': '591a7cc8d07cc376dc324dd725a11579',
    LED + '/line-up/data/tree.json': '9a4a27438e68a77224c624319afd6b7b',
    LED + '/group/sentence index of the latest text.jsonl': 'fdaf069a0c1d71be4e17b38d2f6bce82',
    LED + '/group/line maps.json': '0334e1504051e76d5622cdb67a97fde2',
    LED + '/group/anchor - scripts/step3 side data.json': 'c0f85a845fdeff160881b3f57e78bd6e',
    LED + '/group/anchor - scripts/lib_anchor.py': 'bc5411ae431dc51aac5860fd279bf8dc',
}


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


for p, h in INPUTS.items():
    assert md5(p) == h, 'input changed: ' + p
LM = json.load(open(LED + '/group/line maps.json', encoding='utf-8'))
for k in CHAIN:
    assert md5(SEM + '/' + VPATH[k]) == LM['versions'][k]['md5'], 'theory text changed: ' + k

VSHORT = {'f10': 'file 10', 'f11': 'file 11', 'd1': 'draft 1', 'd2': 'draft 2', 'd3': 'draft 3', 'd4': 'draft 4',
          'd5': 'draft 5', 'scrubbed': 'scrubbed copy', 'repaired': 'repaired copy', 'latest': 'latest text'}

# =====================================================================================
# 1. Trace every unit of the latest text back through the versions
# =====================================================================================
IX = {k: Indexed(k) for k in CHAIN}


def bare(t):
    t = re.sub(r'\\(operatorname|mathcal|mathsf|mathrm|text|mathbf)\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\\[()\[\]]', ' ', t)
    return t


def cwords(t):
    t = re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', ' ', t, flags=re.S)
    return {w.lower() for w in re.findall(r'[A-Za-z][A-Za-z-]{3,}', t)}


def overlap(a, b):
    A, B = cwords(a), cwords(b)
    if not A or not B:
        return 1.0 if not A and not B else 0.0
    return len(A & B) / len(A | B)


def rev_map(a, b):
    m = LM['pairs']['%s->%s' % (a, b)]['map']
    r = {}
    for la, v in m.items():
        if v[0]:
            r.setdefault(v[0], []).append(int(la))
    return r


def predecessor(a, u, rv):
    """The unit of version a that unit u of the next version comes from, or None (in any wording)."""
    A = IX[a]
    t = norm(u['text'])
    lines = rv.get(u['line'], [])
    cand_lines = set()
    for ln in lines:
        cand_lines.update(range(ln - 1, ln + 2))
    near = [A.units[j] for ln in sorted(cand_lines) for j in A.by_line.get(ln, [])]
    exact = [x for x in A.units if norm(x['text']) == t]
    if exact:
        tgt = lines[0] if lines else u['line']
        return min(exact, key=lambda x: abs(x['line'] - tgt)), 1.0, 'same'
    best, bu = 0.0, None
    for x in near:
        r = ratio(u['text'], x['text'])
        if r > best:
            best, bu = r, x
    if bu is not None and best >= 0.5 and (best >= 0.65 or ratio(bare(u['text']), bare(bu['text'])) >= 0.45):
        return bu, round(best, 3), 'reworded'
    for x in near:
        if len(loose(u['text'])) >= 30:
            c = contain_ratio(u['text'], x['text'])
            if c >= 0.8 and c > best:
                best, bu = c, x
    if bu is not None and best >= 0.8:
        return bu, round(best, 3), 'part of'
    best, bu = 0.0, None
    lu = loose(u['text'])
    for x in A.units:
        if difflib.SequenceMatcher(None, lu, loose(x['text'])).real_quick_ratio() < 0.6:
            continue
        r = ratio(u['text'], x['text'])
        if r > best:
            best, bu = r, x
    if bu is not None and best >= 0.6 and (best >= 0.65 or overlap(u['text'], bu['text']) >= 0.3):
        return bu, round(best, 3), 'moved'
    return None, 0.0, 'new'


CH = {u['id']: [('latest', u, 1.0, 'here')] for u in IX['latest'].units}
for i in range(len(CHAIN) - 1, 0, -1):
    a, b = CHAIN[i - 1], CHAIN[i]
    rv = rev_map(a, b)
    for uid, ch in CH.items():
        if ch[-1][0] != b:
            continue
        p, r, how = predecessor(a, ch[-1][1], rv)
        if p is not None:
            ch.append((a, p, r, how))
# oldest first
CHAINS = {uid: [dict(v=v, id=x['id'], text=x['text'], ratio=r, how=how) for v, x, r, how in reversed(ch)]
          for uid, ch in CH.items()}
LINK_HOW = Counter(h['how'] for c in CHAINS.values() for h in c if h['how'] != 'here')
# earlier units shared by more than one latest unit (a split)
ANCESTOR_USERS = defaultdict(set)
for uid, ch in CHAINS.items():
    for h in ch:
        if h['v'] != 'latest':
            ANCESTOR_USERS[(h['v'], h['id'])].add(uid)

# =====================================================================================
# 2. The ledger: records, sections, classes
# =====================================================================================
recs = [json.loads(l) for l in open(LED + '/line-up/data/records.jsonl', encoding='utf-8')]
REC = {r['rid']: r for r in recs}
tree = json.load(open(LED + '/line-up/data/tree.json', encoding='utf-8'))
units = [json.loads(l) for l in open(LED + '/group/sentence index of the latest text.jsonl', encoding='utf-8')]
assert [u['id'] for u in units] == [u['id'] for u in IX['latest'].units]
U = {u['id']: u for u in units}
ORDER = {u['id']: i for i, u in enumerate(units)}
TERMS = json.load(open(LED + '/group/anchor - scripts/step3 side data.json', encoding='utf-8'))['terms']

SECTIONS, SEC_OF, GROUP_OF = [], {}, {}
for g in tree['groups']:
    for s in g.get('sections', []):
        SECTIONS.append(dict(id=s['id'], group=g['id'], gname=g['name'], part=s['part'], part_key=s['part_key'],
                             name=s['name'], first=s['first_line'], last=s['last_line'],
                             units=[x['id'] for x in s['units']], block=s['block'],
                             filed=s['filed_from_other_part']))
        for x in s['units']:
            SEC_OF[x['id']] = s['id']
            GROUP_OF[x['id']] = (g['id'], g['name'])
SECTIONS.sort(key=lambda s: s['first'])
SEC = {s['id']: s for s in SECTIONS}
assert len(SECTIONS) == 134 and len(SEC_OF) == 756


def is_note(uid):
    """The dated note on how the text was made (line 2): not part of the theory; the stand-alone copy drops it."""
    return U[uid]['line'] == 2


def rclass(r):
    """vocab: word swaps and term-wide swaps, as the ledger marks them; owner: the owner-directed passes; crit: the rest."""
    sf, ref = r['source_file'], r['source_ref']
    if r['scope'] in ('term', 'whole text'):
        return 'vocab'
    if 'S95 Scrub - scripts/replacements.json' in sf:
        return 'vocab' if re.search(r'; swap(;|$)', ref) else 'owner'
    if 'S96 Repair - scripts/replacements.json' in sf:
        g = re.search(r'group ([A-Z])', ref)
        if (g and g.group(1) in 'PCFG') or 'replace_lines["2"]' in ref:
            return 'owner'
        return 'crit'
    if 'replacements_stage2.json' in sf:
        g = re.search(r'group ([A-Z])', ref)
        return 'owner' if g and g.group(1) == 'N' else 'crit'
    if 'replacements_stage3.json' in sf:
        g = re.search(r'group ([A-Z])', ref)
        return 'owner' if ('S28' in ref or (g and g.group(1) in 'ON')) else 'crit'
    return 'crit'


NOTE_ONLY = re.compile(r'^(revision 2 note draft|revision record of file 13|full file 13 drafts? .*(the note|meta block))')
for r in recs:
    r['_cls'] = rclass(r)
    r['_note_only'] = bool(NOTE_ONLY.search(r['applied_in']))
    r['_prop'] = r['kind'] == 'recommendation' or r['status'] in ('declined', 'not applied')

ROUNDS = ['file 20 (before log 25)', 'R2 (log 25)', 'round 4 (log 28)', 'round 5 and Stage C (logs 29, 30)',
          'Stage B (logs 41, 55)', 'S62 (log S63)', 'S64 (log S65)', 'S65 (log S70)', 'S70 (log S71)',
          'S72 (log S75)', 'S75', 'S76', 'S81', 'S88', 'S89', 'S90', 'S91', 'S93', 'S94', 'S95', 'S96', 'S97']
SEEN = {r: 'f10' for r in ROUNDS[:12]}
SEEN.update({'S81': 'f11', 'S88': 'f11', 'S89': 'f11', 'S90': 'd2', 'S91': 'd4', 'S93': 'd4', 'S94': 'd5',
             'S95': 'd5', 'S96': 'scrubbed', 'S97': 'repaired'})
# the rounds whose applied changes first appear in each version
MADE_BY = {'f11': ROUNDS[:12], 'd1': ['S81', 'S88', 'S89', 'S90'], 'd2': ['S90'], 'd3': ['S90'], 'd4': ['S91'],
           'd5': ['S93'], 'scrubbed': ['S95'], 'repaired': ['S95', 'S96'], 'latest': ['S97']}
BY_UNIT = defaultdict(list)
for r in recs:
    for s in r['latest_sentences']:
        BY_UNIT[s].append(r)
PREC = ['applied', 'open for the owner', 'declined', 'not applied', 'superseded', 'unknown']

# =====================================================================================
# 3. Per unit
# =====================================================================================


def held_sequence(uid):
    """Wordings the unit held, oldest first: its text in each version, with the wordings of the S96 stage-1 text
    (never kept as a file) placed between the scrubbed and the repaired copy. Consecutive equal wordings collapse."""
    seq = []
    for h in CHAINS[uid]:
        seq.append((h['v'], h['text']))
        if h['v'] == 'scrubbed':
            for r in sorted(BY_UNIT.get(uid, []), key=lambda r: r['lineup_order']):
                if r['kind'] == 'edit' and r['status'] == 'superseded' and r['applied_in'].startswith('stage-1'):
                    w = r['new_sentence'] or ''
                    if not w:
                        continue
                    # the record may carry several sentences (a passage added beside the unit): keep the one
                    # that is the unit's own sentence in that text
                    pieces = split_sents(w) if '\n' not in w else [w]
                    best = max(pieces, key=lambda x: ratio(x, h['text']))
                    lab = re.match(r'\*\*[^*]+\*\* ', h['text'])
                    if lab and not best.startswith('**'):
                        best = lab.group(0) + best
                    if ratio(best, h['text']) >= 0.5:
                        seq.append(('stage1', best))
    out = []
    for v, t in seq:
        if out and loose(out[-1]['text']) == loose(t):
            out[-1]['to'] = v
            continue
        out.append(dict(frm=v, to=v, text=t))
    return out


def seq_label(w):
    f, t = w['frm'], w['to']
    lab = lambda v: 'the S96 stage-1 text (not kept)' if v == 'stage1' else VSHORT[v]
    return lab(f) if f == t else '%s to %s' % (lab(f), lab(t))


def observed(uid, c):
    """Text changes between consecutive versions of the unit, each marked layout, vocab, recorded or unrecorded."""
    ch = CHAINS[uid]
    out = []
    for a, b in zip(ch, ch[1:]):
        A, B = norm(a['text']), norm(b['text'])
        if A == B:
            continue
        if loose(A) == loose(B) or A in B or B in A:
            how = 'layout'
        elif c['crit'] + c['owner'] + c['sup_nonvocab'] > 0:
            how = 'recorded'
        elif c['vocab'] > 0 and CHAIN.index(b['v']) >= CHAIN.index('scrubbed'):
            how = 'vocab'
        else:
            how = 'unrecorded'
        out.append((a['v'], b['v'], how))
    return out


ROWS = {}
for u in units:
    uid = u['id']
    ch = CHAINS[uid]
    first = ch[0]['v']
    rs = BY_UNIT.get(uid, [])
    byc = defaultdict(list)
    for r in rs:
        byc[r['change_id']].append(r)
    c = Counter()
    props, changes = [], []
    for cid, members in byc.items():
        appl = [r for r in members if r['status'] == 'applied' and not r['_note_only']]
        if appl:
            if all(r['_cls'] == 'vocab' for r in appl):
                k = 'vocab'
            elif any(r['_cls'] == 'owner' for r in appl):
                k = 'owner'
            else:
                k = 'crit'
            c[k] += 1
            changes.append((cid, k))
        isprop = [r for r in members if r['_prop']]
        if isprop and not appl:
            out = min((r['status'] for r in isprop), key=PREC.index)
            voc = all(r['_cls'] == 'vocab' for r in isprop)
            c['p_' + out + ('_v' if voc else '')] += 1
            props.append(dict(cid=cid, outcome=out, vocab=voc, recs=sorted(isprop, key=lambda r: r['lineup_order'])))
    sup = {}
    for r in sorted(rs, key=lambda r: r['lineup_order']):
        if r['status'] == 'superseded':
            sup.setdefault(norm(r['new_sentence'] or r['new']), r)
    c['sup'] = len(sup)
    c['sup_owner'] = sum(1 for r in sup.values() if r['_cls'] == 'owner')
    c['sup_vocab'] = sum(1 for r in sup.values() if r['_cls'] == 'vocab')
    c['sup_nonvocab'] = c['sup'] - c['sup_vocab']
    row = dict(id=uid, kind=u['kind'], line=u['line'], text=u['text'], section=SEC_OF[uid], group=GROUP_OF[uid],
               first=first, nver=len(ch), rounds=sum(1 for x in ROUNDS if CHAIN.index(SEEN[x]) >= CHAIN.index(first)),
               c=c, props=props, changes=changes, nrec=len(rs), note=is_note(uid))
    row['subst'] = c['crit'] + c['owner'] + c['sup_nonvocab']
    row['total'] = c['crit'] + c['owner'] + c['vocab'] + c['sup']
    row['obs'] = observed(uid, c)
    row['seq'] = held_sequence(uid)
    ROWS[uid] = row

for u in units:
    uid = u['id']
    i = ORDER[uid]
    nb = set(SEC[SEC_OF[uid]]['units']) | {units[j]['id'] for j in range(max(0, i - 2), min(len(units), i + 3))}
    nb.discard(uid)
    nb = sorted((x for x in nb if not is_note(x)), key=ORDER.get)
    r = ROWS[uid]
    r['nb'] = nb
    r['nb_subst'] = statistics.mean(ROWS[x]['subst'] for x in nb) if nb else 0.0
    r['nb_crit'] = statistics.mean(ROWS[x]['c']['crit'] for x in nb) if nb else 0.0
    r['nb_total'] = statistics.mean(ROWS[x]['total'] for x in nb) if nb else 0.0

# terms, as the ledger names them (the S98 anchoring step's term list and matching rule)
TERM_RE = []
for x in sorted(TERMS, key=lambda s: -len(s)):
    if x.startswith('('):
        rx = re.compile(re.escape(x))
    else:
        body = r'\s+'.join(re.escape(w) for w in x.split())
        rx = re.compile(r'(?<![A-Za-z])' + body + r'(?:s|es|d|ed)?(?![A-Za-z])', re.I)
    TERM_RE.append((x, rx))


def terms_in(t):
    blob = t.replace('**', '')
    return sorted((x for x, rx in TERM_RE if rx.search(blob)), key=str.lower)


for r in ROWS.values():
    r['terms'] = terms_in(r['text'])

# =====================================================================================
# 4. Strong candidates
# =====================================================================================
ELIG = [r for r in ROWS.values() if r['kind'] != 'heading' and not r['note']]


def quant(xs, q):
    xs = sorted(xs)
    return xs[int(round(q * (len(xs) - 1)))]


NB_CUT = round(quant([r['nb_subst'] for r in ELIG], 0.75), 2)
AGE_CUT = 10  # carried in every one of the ten versions, file 10 to the latest text
for r in ROWS.values():
    r['stable'] = (r['kind'] != 'heading' and not r['note'] and r['subst'] == 0
                   and all(h != 'unrecorded' for _, _, h in r['obs']))
    r['nonvocab_props'] = [p for p in r['props'] if not p['vocab']]
    r['vocab_props'] = [p for p in r['props'] if p['vocab']]
    r['strong'] = ''
    if r['stable'] and r['nver'] >= AGE_CUT and r['nb_subst'] >= NB_CUT:
        r['strong'] = 'challenged and kept' if r['nonvocab_props'] else 'never challenged'
STRONG_C = sorted([r for r in ROWS.values() if r['strong'] == 'challenged and kept'], key=lambda r: (-r['nb_subst'], ORDER[r['id']]))
STRONG_N = sorted([r for r in ROWS.values() if r['strong'] == 'never challenged'], key=lambda r: (-r['nb_subst'], ORDER[r['id']]))
NEAR_AGE = sorted([r for r in ROWS.values() if r['stable'] and 8 <= r['nver'] < AGE_CUT and r['nb_subst'] >= NB_CUT],
                  key=lambda r: (-r['nb_subst'], ORDER[r['id']]))
UNRECORDED = [r for r in ROWS.values() if r['kind'] != 'heading' and not r['note'] and r['subst'] == 0
              and any(h == 'unrecorded' for _, _, h in r['obs'])]

# =====================================================================================
# 5. Sections
# =====================================================================================
SROWS = []
for s in SECTIONS:
    us = [x for x in s['units'] if not is_note(x)]
    if not us:
        continue
    cids = defaultdict(set)
    for x in us:
        for r in BY_UNIT.get(x, []):
            cids[r['change_id']].add(r['rid'])
    nblock = 0
    for b in s['block']:
        for rid in b['records']:
            cids[b['change_id']].add(rid)
            nblock += 1
    c = Counter()
    sup = {}
    for cid, rids in cids.items():
        members = [REC[i] for i in rids]
        appl = [r for r in members if r['status'] == 'applied' and not r['_note_only']]
        if appl:
            if all(r['_cls'] == 'vocab' for r in appl):
                c['vocab'] += 1
            elif any(r['_cls'] == 'owner' for r in appl):
                c['owner'] += 1
            else:
                c['crit'] += 1
        isprop = [r for r in members if r['_prop']]
        if isprop and not appl:
            out = min((r['status'] for r in isprop), key=PREC.index)
            c['p_' + out] += 1
        for r in sorted(members, key=lambda r: r['lineup_order']):
            if r['status'] == 'superseded':
                sup.setdefault(norm(r['new_sentence'] or r['new']), r)
    c['sup'] = len(sup)
    c['sup_owner'] = sum(1 for r in sup.values() if r['_cls'] == 'owner')
    n = len(us)
    tot = c['crit'] + c['owner'] + c['vocab'] + c['sup']
    SROWS.append(dict(s=s, units=us, n=n, c=c, nblock=nblock, crit_pu=c['crit'] / n, tot_pu=tot / n, tot=tot,
                      owner_share=(c['owner'] + c['sup_owner']) / tot if tot else 0.0))
BY_CRIT = sorted(SROWS, key=lambda x: (-x['crit_pu'], -x['tot_pu'], x['s']['first']))
BY_TOT = sorted(SROWS, key=lambda x: (-x['tot_pu'], -x['crit_pu'], x['s']['first']))
TOP_SECTIONS = BY_CRIT[:10]
UNIT_ORDER = sorted([r for r in ROWS.values() if not r['note']],
                    key=lambda r: (-r['subst'], -r['c']['crit'], -r['total'], ORDER[r['id']]))
TOP_UNITS = UNIT_ORDER[:15]

# =====================================================================================
# 6. Patterns in a run of wordings
# =====================================================================================
STOP = set('a an the of to in on and or for by with as at is are be it its that this which not no from into its'.split())


def toks(t):
    return re.findall(r'\\[A-Za-z]+|[A-Za-z0-9_\'’-]+|[^\sA-Za-z0-9]', loose(t))


def content(span):
    return any(len(w) >= 4 and w.lower() not in STOP and not w.startswith('\\') for w in span)


def patterns(uid):
    seq = ROWS[uid]['seq']
    feats = dict(returns=[], near_returns=[], added_removed=[], removed_restored=[], swaps=[], grew=None,
                 split=False, joined=False, n=len(seq), words=[len(loose(w['text']).split()) for w in seq])
    L = [loose(w['text']) for w in seq]
    for k in range(len(seq)):
        for i in range(k - 1):
            if L[i] == L[k]:
                feats['returns'].append((i, k))
                break
        else:
            for i in range(k - 1):
                if difflib.SequenceMatcher(None, L[i], L[k], autojunk=False).ratio() >= 0.97 and \
                        all(difflib.SequenceMatcher(None, L[j], L[k], autojunk=False).ratio() < 0.97 for j in range(i + 1, k)):
                    feats['near_returns'].append((i, k))
                    break
    added, removed = [], []
    for s in range(len(seq) - 1):
        A, B = toks(seq[s]['text']), toks(seq[s + 1]['text'])
        sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                continue
            old, new = A[i1:i2], B[j1:j2]
            if tag == 'replace' and 1 <= len(old) <= 3 and 1 <= len(new) <= 3 and content(old + new):
                feats['swaps'].append((' '.join(old), ' '.join(new), s + 1))
            if new and content(new):
                added.append((' '.join(new), s + 1))
            if old and content(old):
                removed.append((' '.join(old), s + 1))
    for a, sa in added:
        for d, sd in removed:
            if sd > sa and (a == d or (len(a) > 12 and a in d)):
                if (a, sa, sd) not in feats['added_removed']:
                    feats['added_removed'].append((a, sa, sd))
                break
    for d, sd in removed:
        for a, sa in added:
            if sa > sd and (a == d or (len(d) > 12 and d in a)):
                if (d, sd, sa) not in feats['removed_restored']:
                    feats['removed_restored'].append((d, sd, sa))
                break
    w = feats['words']
    if len(w) >= 3 and all(y > x for x, y in zip(w, w[1:])):
        feats['grew'] = 'longer at every change'
    elif len(w) >= 3 and all(y < x for x, y in zip(w, w[1:])):
        feats['grew'] = 'shorter at every change'
    elif len(w) >= 2 and w[-1] >= 1.3 * w[0]:
        feats['grew'] = 'longer overall'
    elif len(w) >= 2 and w[-1] <= 0.77 * w[0]:
        feats['grew'] = 'shorter overall'
    for h in CHAINS[uid]:
        if h['how'] == 'part of' or len(ANCESTOR_USERS[(h['v'], h['id'])]) > 1:
            feats['split'] = True
    feats['joined'] = any(how == 'layout' and CHAINS[uid][0]['text'] != ROWS[uid]['text'] for _, _, how in ROWS[uid]['obs'])
    return feats


def pattern_line(uid):
    f = patterns(uid)
    seq = ROWS[uid]['seq']
    lab = lambda k: seq_label(seq[k])
    bits = []
    if f['n'] <= 1:
        return 'one wording throughout'
    bits.append('%d wordings, %s words' % (f['n'], ' → '.join(str(x) for x in f['words'])))
    if f['grew']:
        bits.append('grew ' + f['grew'] if f['grew'].startswith('longer') else 'got ' + f['grew'])
    for i, k in f['returns']:
        bits.append('the wording of %s came back in %s' % (lab(i), lab(k)))
    for i, k in f['near_returns']:
        bits.append('the wording of %s came back, all but a few characters, in %s' % (lab(i), lab(k)))
    if f['swaps']:
        sw = []
        for o, n_, s in f['swaps'][:6]:
            sw.append('"%s" → "%s" (%s)' % (o, n_, lab(s)))
        bits.append('words swapped: ' + '; '.join(sw) + (' and %d more' % (len(f['swaps']) - 6) if len(f['swaps']) > 6 else ''))
    for a, sa, sd in f['added_removed'][:4]:
        bits.append('"%s" added (%s) and taken out again (%s)' % (a[:80], lab(sa), lab(sd)))
    for d, sd, sa in f['removed_restored'][:4]:
        bits.append('"%s" taken out (%s) and put back (%s)' % (d[:80], lab(sd), lab(sa)))
    if f['split']:
        bits.append('made from an earlier sentence that also gave rise to another sentence (a split)')
    return '; '.join(bits)


# every return of an earlier wording, anywhere in the text
RETURNS = []
for u in units:
    if is_note(u['id']):
        continue
    f = patterns(u['id'])
    for i, k in f['returns']:
        RETURNS.append((u['id'], 'exact', i, k))
    for i, k in f['near_returns']:
        RETURNS.append((u['id'], 'near', i, k))
PHRASE_RETURNS = []
for u in units:
    if is_note(u['id']):
        continue
    f = patterns(u['id'])
    for a, sa, sd in f['added_removed']:
        PHRASE_RETURNS.append((u['id'], 'added, then taken out', a, sa, sd))
    for d, sd, sa in f['removed_restored']:
        PHRASE_RETURNS.append((u['id'], 'taken out, then put back', d, sd, sa))

# =====================================================================================
# 7. Dependence order (Part XIV of the latest text), quoted
# =====================================================================================
LAT = IX['latest']
DEP_SENTS = [x['text'] for x in LAT.units if x['line'] in (515, 517, 518, 520, 526)]


def dep_sentence(key):
    for s in DEP_SENTS:
        if key in s:
            return s
    raise KeyError(key)


def vi_clause(key):
    s = dep_sentence('In Part VI, conflict depends on')
    for part in re.split(r', (?=conflict with|rivals|being ruled|a problem|and easy)', s):
        if part.startswith(key) or part.startswith('In Part VI, ' + key) or part.startswith('and ' + key):
            return part.strip().rstrip('.')
    return s


DEP = [  # (name, test on the unit's text, clause quoted from the latest text)
    ('(O)', r'\(O\)|organi[sz]ation', lambda: dep_sentence('(O) and (Q) depend on nothing')),
    ('(Q)', r'\(Q\)|\bquestion', lambda: dep_sentence('(O) and (Q) depend on nothing')),
    ('declared indices and inputs', r'\bcontracts?\b|\bgrain\b|\bboundary\b(?! condition)|\bcontinuity\b|declared input',
     lambda: dep_sentence('(O) and (Q) depend on nothing')),
    ('(K)', r'\(K\)|\bkinds?\b|\bsignatures?\b', lambda: dep_sentence('(K) depends on')),
    ('(F1), (F2), (A)', r'\(F1\)|\(F2\)|\(A\)|fidelity|faithful', lambda: dep_sentence('(F1), (F2), (A) depend on')),
    ('(E)', r'\(E\)|\baccounts?\b', lambda: dep_sentence('(E) depends on')),
    ('(S), (B), (D)', r'\((S|B|D)\)', lambda: dep_sentence('(S), (B), (D) depend on')),
    ('(R)', r'\(R\)|\brepresent', lambda: dep_sentence('(R) depends on')),
    ('provenance', r'provenance', lambda: dep_sentence('Provenance, from physical history')),
    ('roles', r'\broles?\b', lambda: dep_sentence('Roles, from admitted edits')),
    ('respect of a question', r'\brespect\b|\bquery\b', lambda: dep_sentence('The respect of a question')),
    ('(K1), (K2), (K3)', r'\(K[123]\)|\bbearing\b|\busab', lambda: dep_sentence('(K1) depends on')),
    ('Deploy', r'Deploy', lambda: dep_sentence('Deploy depends on')),
    ('Ownership, owned capability', r'[Oo]wnership|owned capability', lambda: dep_sentence('Ownership depends on')),
    ('Build', r'\bBuild\b|\bconstruct', lambda: dep_sentence('Build depends on')),
    ('(N), (G)', r'\((N|G)\)|newness|\borigin', lambda: dep_sentence('(N), (G) depend on')),
    ('(P), (EX)', r'\((P|EX)\)|\brepair|[Cc]reated explanation|ProducedBy', lambda: dep_sentence('(P), (EX) depend on')),
    ('(RC), (U1)–(U3)', r'\((RC|U[123])\)|recursi|universal', lambda: dep_sentence('(RC), (U1)')),
    ('conflict', r'\bconflict', lambda: vi_clause('conflict')),
    ('rivals', r'\brivals?\b', lambda: vi_clause('rivals on conflict')),
    ('ruled out', r'ruled? out', lambda: vi_clause('being ruled out')),
    ('problem', r'\bproblems?\b', lambda: vi_clause('a problem for')),
    ('easy to vary', r'easy to vary', lambda: vi_clause('easy to vary')),
    ('physical module (import 1)', r'physical module|\\Theta', lambda: dep_sentence('The **physical module**')),
    ('appraisal relation (import 2)', r'apprais|\\mathcal N|aesthet', lambda: dep_sentence('The **appraisal relation**')),
]


def deps_of(text):
    out = []
    for name, rx, fn in DEP:
        if re.search(rx, text):
            out.append((name, fn()))
    return out


# =====================================================================================
# 8. The values group
# =====================================================================================
VAL_RX = re.compile(r'worth|apprais|normative|aesthet|\\mathcal N\b|merit|ranking of thinkers|orders explanations', re.I)
VALUES = [u['id'] for u in units if not is_note(u['id']) and
          (GROUP_OF[u['id']][0] == 'G11' or any(VAL_RX.search(h['text']) for h in CHAINS[u['id']]))]

# =====================================================================================
# 8b. The ten sections, in plain words: patterns only, read from the runs below (written after the first run)
# =====================================================================================
SECTION_PATTERN = {
    'sec-L542-542': 'One sentence, in the text since file 11, four wordings of about 90 words each. The scrub swapped eight words or phrases in it at once ("Derivation" to "Argument", "theorem" to "claim", "a demonstration" and "a showing" to "an argument", "witness" to "trace", "primitive layer" to "object layer"). The repaired copy then rewrote the second and third of its three clauses, taking out one "an argument" the scrub had put in ("an argument that every construction trace can be rewritten" became "a method that rewrites every construction trace"); the latest text renamed its label, "(D)" to "(Prov)". Length stayed flat.',
    'sec-L544-544': 'One sentence since file 10, five wordings. Its opening changed at nearly every step: an instruction ("Show that ...") became a noun ("A showing that ..."), then "An argument that ...", then, in the repaired copy, two cases ("A case of finding a new question that ... fails to capture; or an episode that is not creative which that treatment counts as creative"). "Genuine" and "the right question" went out in the scrubbed copy ("a new question"). The label was renamed, "(E)" to "(QF)".',
    'sec-L538-538': 'The first sentence has five wordings and three labels ("An explanation without a faithful transport", then "(B) Necessity", then "(Nec) Necessity"). What would count moved from "A genuine explanation" (file 10 to draft 5) to "An explanation, argued to be one and not a non-explanation by an argument that does not use (E)" (scrubbed copy), to "A candidate that an argument not using (E) rules out as a non-explanation" (repaired copy), to "A candidate such that an argument not using (E) rules out the claim that it is a non-explanation" (latest text). "Under any physically admitted contract" became "under any contract on its target" in an owner-directed pass. The second sentence kept one wording.',
    'sec-L540-540': 'The first sentence changed once, in file 11 (the instruction "Produce a case in which ..." became "A case where ..."), and then only its label ("(C)" to "(Elim)"). The second grew from 9 to 26 words over five wordings, each naming what the case would rule out a little differently: "This refutes Derivation 1", "Such a case would rule out Argument 1", "... the Claim of Argument 1", "An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it", "... the Consequence of Argument 1".',
    'sec-L536-536': 'The first sentence has five wordings, and its ending went back and forth: "plainly explains nothing" (file 10), "plainly provides no account" (file 11 to draft 5), "nonetheless explains nothing" (scrubbed copy: the words of file 10 came back), "an argument not using (E) rules out as an explanation of what its question asks" (repaired copy), "an argument not using (E) rules out the claim that it is an explanation of what its question asks" (latest text). "On a physically admitted contract" became "on a contract of its question" (owner-directed), and "a non-declared transport" became "a transport whose provenance is not declared (Part IV)"; it went from 28 words in file 10 to 47. The third sentence, new in file 11, grew at every change and took the same new ending. The second sentence has kept one wording since file 11, when it took the place of an earlier sentence.',
    'sec-L522-522': 'All three sentences grew at every change. The list of declared inputs gained an item in draft 1 (a weighting of credit among contributions) and another in the repaired copy (an assessor\'s inference forms, scope and premises), and the words "tentatively accepts" joined that item in the repaired copy; the first sentence went from 57 to 111 words. The scrub swapped "primitives", "obligations", "verdict", "unsettled", "normative relation" and "worth" across the three.',
    'sec-L33-35': 'Its two units kept one wording each. The churn is elsewhere in the section: a chain of twelve proposed wordings of a clause on narrowed claims (round 4 to S70), whose last wording (S72) the ledger marks applied but cannot place in the latest text, all standing in the section\'s block, placed there by the section their source names; and two fragments removed in file 11. The sentence that stands was added in file 11.',
    'sec-L29-31': 'Three of its five units grew, two at every change. "Everything else is derived." (4 words, file 10) became a 30-word sentence over five wordings, adding in turn "in the order Part XIV states", "from the two primitives, the declared indices and the declared inputs", and "the structural vocabulary of (O) and (Q)". The sentence naming the predicates "really explains", "is a cause" and "is knowledge" has five wordings; "is a created explanation" was put in by the scrub and taken out in the repaired copy, which added "(EX) is a defined relation of an episode, not such a predicate". The heading and the word pairs "primitive"/"import", "derived"/"defined" were swapped by the scrub.',
    'sec-L427-427': 'Small changes on long sentences: one word taken out in draft 1 ("the system\'s own today" became "the system\'s own"), "Credit for content" became "Contribution of content", and "the capability it is meant to ground" became "the capability attributed through it". A proposal in the section\'s block was never applied.',
    'sec-L47-47': 'Two of the three sentences grew, one at every change. The answer to the grievance was qualified in the latest text ("Selection appears once, at the bottom" became "Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, ..."), and its last sentence was reworded three times ("the semantics forbids that reduction in Part IV"; "Part IV forbids the reduction and Part XV names its refutation"; "... names what would rule it out"; "Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out"). The middle sentence changed only "witness" to "trace".',
}
assert set(SECTION_PATTERN) == {x['s']['id'] for x in TOP_SECTIONS}, sorted(x['s']['id'] for x in TOP_SECTIONS)

# =====================================================================================
# 9. Writing
# =====================================================================================
os.makedirs(HERE, exist_ok=True)
CLS_NAME = {'crit': 'criticism-driven', 'owner': 'owner-directed', 'vocab': 'vocabulary only'}


def q(t):
    """A wording as a blockquote, verbatim."""
    return '\n'.join('> ' + l if l else '>' for l in t.split('\n'))


def f2(x):
    return ('%.2f' % x).rstrip('0').rstrip('.') if x != int(x) else '%d' % x


def sec_title(s):
    pk = {'FM': 'Front matter'}.get(s['part_key'], 'Part ' + s['part_key'])
    return '%s · %s (lines %d–%d)' % (pk, s['name'], s['first'], s['last']) if s['first'] != s['last'] else \
        '%s · %s (line %d)' % (pk, s['name'], s['first'])


def prop_wording(r):
    w = r['new_sentence'] or r['new']
    if not w:
        return '*(proposed removal of:)*\n' + q(r['old_sentence'] or r['old'])
    return q(w)


def unit_block(r, with_props=True, with_deps=True):
    out = []
    s = SEC[r['section']]
    out.append('**%s** · %s · %s · group %s %s' % (r['id'], r['kind'], sec_title(s), r['group'][0], r['group'][1]))
    out.append('')
    out.append(q(r['text']))
    out.append('')
    out.append('- In the text since %s: %d of 10 versions; came through %d of the 22 rounds of edits and proposals.'
               % (VSHORT[r['first']], r['nver'], r['rounds']))
    vc = r['c']['vocab']
    if vc or r['obs']:
        swaps = [x for x in r['obs'] if x[2] == 'vocab']
        lay = [x for x in r['obs'] if x[2] == 'layout']
        bits = []
        if vc:
            bits.append('%d vocabulary-only change%s (the ledger marks %s)' % (vc, '' if vc == 1 else 's', 'it' if vc == 1 else 'them'))
        if lay:
            bits.append('a change of layout only (%s)' % ', '.join('%s to %s' % (VSHORT[a], VSHORT[b]) for a, b, _ in lay))
        vrecs = []
        for x in sorted(BY_UNIT.get(r['id'], []), key=lambda x: x['lineup_order']):
            if x['status'] == 'applied' and x['_cls'] == 'vocab' and not x['_note_only']:
                pair = (x['old'].strip(), x['new'].strip())
                if pair not in [v[0] for v in vrecs]:
                    vrecs.append((pair, x))
        if vrecs:
            bits.append('the ledger\'s vocabulary records on it: ' + '; '.join(
                '"%s" → "%s" (%s, %s)' % (o[:90] + ('…' if len(o) > 90 else ''), n_[:90] + ('…' if len(n_) > 90 else ''), x['rid'], x['round'])
                for (o, n_), x in vrecs))
        if vc and len(r['seq']) == 1:
            bits.append('its own wording is the same in every version (the vocabulary change stands on words it shares with a record placed on it)')
        out.append('- Allowed changes: ' + '; '.join(bits) + '.')
        if len(r['seq']) > 1:
            out.append('- Earlier wording%s:' % ('' if len(r['seq']) == 2 else 's'))
            for w in r['seq'][:-1]:
                out.append('  - %s:' % seq_label(w))
                out.append('\n'.join('    ' + l for l in q(w['text']).split('\n')))
    else:
        out.append('- Changes: none of any kind; the same wording in every version.')
    out.append('- Neighbours (%d: the other units of its section and the units within two either side): %s substantive '
               'changes each on average (criticism-driven alone: %s).' % (len(r['nb']), f2(round(r['nb_subst'], 2)), f2(round(r['nb_crit'], 2))))
    if with_props:
        if r['nonvocab_props']:
            out.append('- Proposals it came through (%d):' % len(r['nonvocab_props']))
            for p in r['nonvocab_props']:
                seen = set()
                for x in p['recs']:
                    key = norm(x['new_sentence'] or x['new']) + '|' + x['status']
                    if key in seen:
                        continue
                    seen.add(key)
                    placed = '' if not x['anchor_method'] or not x['anchor_method'].startswith('line map') else \
                        ' · placed by the line it was written against, not by its own words'
                    out.append('  - %s · %s · %s · %s · written against %s · source: %s — %s%s' % (
                        x['rid'], x['round'], x['kind'], x['status'], x['target_text'].split(' (')[0],
                        x['source_file'], x['source_ref'], placed))
                    out.append('\n'.join('    ' + l for l in prop_wording(x).split('\n')))
        if r['vocab_props']:
            out.append('- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): %s.' %
                       '; '.join('%s (%s)' % (p['cid'], p['outcome']) for p in r['vocab_props']))
    if with_deps:
        out.append('- Terms it uses (the ledger\'s term list): %s.' % (', '.join(r['terms']) if r['terms'] else 'none on the list'))
        ds = deps_of(r['text'])
        if ds:
            out.append('- What the dependence order of the latest text (Part XIV) says of what it names:')
            done = set()
            for name, clause in ds:
                if clause in done:
                    out.append('  - %s: the same sentence as above.' % name)
                    continue
                done.add(clause)
                out.append('  - %s: "%s"' % (name, clause))
    out.append('')
    return out


def seq_block(uid, indent=''):
    r = ROWS[uid]
    out = []
    for w in r['seq']:
        out.append('%s- %s:' % (indent, seq_label(w)))
        out.append('\n'.join(indent + '  ' + l for l in q(w['text']).split('\n')))
    return out


def owner_marks(uid):
    r = ROWS[uid]
    c = r['c']
    bits = []
    if c['owner'] or c['sup_owner']:
        bits.append('%d of its changes and %d of its replaced wordings came from the owner-directed passes' % (c['owner'], c['sup_owner']))
    else:
        bits.append('none of its changes came from the owner-directed passes')
    return '; '.join(bits)


L = []
w = L.append
w('# S100 — Strong candidates and the most altered sections')
w('')
w('*Log S100, 26 September 2026, under decision S31. Made by program (`%s`), from the S98 ledger (`results/S98 Ledger of edits and recommendations/`) and the ten theory texts from file 10 to the latest text; nothing in them was changed. One agent (decision S22). Sentences are quoted byte for byte; no reason given for any change or proposal is copied.*' % SCRIPT)
w('')
w('## What was asked')
w('')
w('The owner, 26 September 2026, answering Claude\'s suggestion "For your \'strong candidates\', I\'d start with the sentences that came through many rounds without being touched, while the sentences around them kept changing.": "Yup do that. Also collect the sections that are most altered. Because they might tell me what isn\'t well understand, what\'s difficult to express in prose or whatever." Earlier, the aim: to "isolate the strong candidates, See what else they depend on and maybe even figure out, for example, whether values should be part of the theory, or separate."')
w('')

# ---- figures used in the summary
n_elig = len(ELIG)
n_stable = sum(1 for r in ELIG if r['stable'])
n_stable10 = sum(1 for r in ELIG if r['stable'] and r['nver'] == 10)
w('## In short')
w('')
w('- **The unit** is the ledger\'s: a sentence, heading, displayed formula or list item of the latest text (756). Headings (%d) and the dated note on how the text was made (%d sentences, line 2) are left out of the candidate lists; %d units remain.' % (
    sum(1 for r in ROWS.values() if r['kind'] == 'heading'), sum(1 for r in ROWS.values() if r['note']), n_elig))
w('- **Untouched in substance:** %d of the %d have no criticism-driven change, no owner-directed change and no replaced wording in the ledger, and no change between versions that the ledger has no record of; %d of them have been in the text since file 10.' % (n_stable, n_elig, n_stable10))
w('- **Thresholds:** in all ten versions (since file 10, through all 22 rounds), and neighbours that averaged at least %s substantive changes each, the upper quartile over all %d units.' % (f2(NB_CUT), n_elig))
w('- **Strong candidates:** %d, of which %d were **challenged and kept** (a proposal was made against the sentence and not taken) and %d were **never challenged** (no proposal ever touched the sentence alone; it may simply never have been examined).' % (
    len(STRONG_C) + len(STRONG_N), len(STRONG_C), len(STRONG_N)))
w('- **Most altered:** the ten sections with the most criticism-driven changes per unit are %s.' % '; '.join(
    '%s (%s per unit)' % (x['s']['name'], f2(round(x['crit_pu'], 2))) for x in TOP_SECTIONS))
gtop = Counter(x['s']['group'] for x in TOP_SECTIONS)
rest = [x['s']['name'] for x in TOP_SECTIONS if x['s']['group'] not in ('G15', 'G14')]
w('- **Where the most altered stand:** %d of those ten are items of the theory\'s own list of what would rule it out (group G15), %d are about what the theory imports, takes as input or defines (group G14), and the other %d are %s. Owner-directed passes account for at most %d%% of any one\'s churn.' % (
    gtop.get('G15', 0), gtop.get('G14', 0), len(rest), '; '.join(rest), round(100 * max(x['owner_share'] for x in TOP_SECTIONS))))
nret = len({x[0] for x in RETURNS})
w('- **Wordings that came back:** %d unit%s hold%s a wording that repeats an earlier one after a different wording between (%d exactly, %d all but a few characters); %d phrases were added and later taken out, or taken out and later put back.' % (
    nret, '' if nret == 1 else 's', 's' if nret == 1 else '', sum(1 for x in RETURNS if x[1] == 'exact'), sum(1 for x in RETURNS if x[1] == 'near'), len(PHRASE_RETURNS)))
w('')

# ---- 1. method
w('## 1. How the measures were made')
w('')
w('### 1.1 Versions and rounds')
w('')
w('Each unit of the latest text was followed back through the chain file 10 → file 11 → drafts 1 to 5 → scrubbed copy → repaired copy → latest text, one step at a time, by program: the ledger\'s line maps (`group/line maps.json`) name the earlier line or lines; on them, the same sentence in any wording is the one with the same text, or failing that the most similar one (similarity at least 0.5 on the whole sentence, and at least 0.45 once formula markup is set aside, unless 0.65 or more), or one that holds the unit as a part (a split); failing those, a sentence anywhere in the earlier text with similarity at least 0.6 (moved). The first version reached is where the unit first stands. Links made: %s.' % ', '.join('%s %d' % (k, v) for k, v in sorted(LINK_HOW.items()) if k != 'here'))
w('')
fv = Counter(r['first'] for r in ROWS.values())
w('| first in | ' + ' | '.join(VSHORT[k] for k in CHAIN) + ' |')
w('| --- | ' + ' | '.join('---:' for _ in CHAIN) + ' |')
w('| units (all 756) | ' + ' | '.join(str(fv.get(k, 0)) for k in CHAIN) + ' |')
fv2 = Counter(r['first'] for r in ELIG)
w('| units (%d, no headings, no note) | ' % n_elig + ' | '.join(str(fv2.get(k, 0)) for k in CHAIN) + ' |')
w('')
w('"Rounds" are the ledger\'s 22 rounds of edits and proposals, in its order (file 20 and R2 to S97). A unit in file 10 came through all 22; one first in file 11 through the ten from S81; one first in a draft of revision 2 through those from the round that read that draft (S90 read drafts 1 and 2, S91 and S93 draft 4, S94 and S95 draft 5, S96 the scrubbed copy, S97 the repaired copy).')
w('')
w('### 1.2 What each record of the ledger counts as')
w('')
cc = Counter((r['_cls'], r['status']) for r in recs)
w('A record touches a unit when the unit is among its sentences in the latest text (`latest_sentences`: its home sentence, its pointer sentences and, for a vocabulary record, every sentence it names). Records with no sentence in the latest text (%d) are counted only for their section (§4). Every record is one of three classes:' % sum(1 for r in recs if not r['latest_sentences']))
w('')
w('- **Vocabulary only** (%d records): what the ledger marks as vocabulary, scope `term` or `whole text`, and the scrub\'s edits that its own list marks `swap` (265 of the 300 edits of `S95 Scrub - scripts/replacements.json`).' % sum(v for (k, s), v in cc.items() if k == 'vocab'))
w('- **Owner-directed** (%d records): the scrub\'s other edits (its 33 marked `rewording` and the two lines it filled, lines 2 and 8); the S96 repair of physical possibility, conflict and premises (groups P, C, F and G of `S96 Repair - scripts/replacements.json`, on decisions S23 to S27, and its rewrite of the dated note); the S28 wording points (group O of `replacements_stage3.json`, and every entry whose ruling names S28) and the note of that stage (group N).' % sum(v for (k, s), v in cc.items() if k == 'owner'))
w('- **Criticism-driven** (%d records): everything else — the readers\' and auditors\' proposals, the rulings, the errata and the defects, the change list of revision 2, the repairs the S95 readings asked for (group R of the S96 repair, applied with the owner-directed pass but found by readers), the second stage after the two readings of the first, and the S97 rulings on the outside cross-examination (group X).' % sum(v for (k, s), v in cc.items() if k == 'crit'))
w('')
w('Changes are counted once each (the ledger\'s `change_id`), not once per record: a change with an applied record, other than one applied only in a note, is an **applied change** of the unit, classed vocabulary only if all its applied records are, owner-directed if any is, and criticism-driven otherwise. %d applied records changed only a note (the revision note, the revision record, the note of sources) and are not counted as changes. A change with no applied record and at least one proposal (a recommendation, or an edit declined or not applied) is a **proposal** of the unit, with the first of these outcomes among its records: open for the owner, declined, not applied, superseded, unknown. A **replaced wording** is a distinct wording of a record whose status is superseded (applied in a draft or in the S96 stage-1 text and later changed, or proposed and replaced by a later wording).' % sum(1 for r in recs if r['_note_only'] and r['status'] == 'applied'))
w('')
w('- **Substantive changes** of a unit: criticism-driven changes + owner-directed changes + replaced wordings other than vocabulary ones.')
w('- **Total churn:** criticism-driven + owner-directed + vocabulary-only changes + all replaced wordings.')
w('- **Neighbours:** the other units of its section and the units within two either side in text order (headings included, the dated note left out). **Neighbour churn** is the mean of their substantive changes.')
w('- **Changes in the texts the ledger does not hold:** each step between versions where the unit\'s text differs is marked *layout* (only emphasis or spacing, or a unit joined with or split from its neighbour), *vocabulary* (after draft 5, on a unit whose only applied changes are vocabulary only), *recorded* (the unit has a substantive change in the ledger) or *unrecorded* (none of these).')
w('')
w('Owner-directed passes add to churn by design: they touched sentences because the owner asked for a change of words or of what the theory says, not because a reader found a fault there. Every count below gives them apart.')
w('')

# ---- 2. distributions
w('## 2. Distributions, and where the cuts fall')
w('')
w('### 2.1 Substantive changes per unit')
w('')
sd = Counter(r['subst'] for r in ELIG)
w('| substantive changes | ' + ' | '.join(str(k) for k in sorted(sd)) + ' |')
w('| --- | ' + ' | '.join('---:' for _ in sd) + ' |')
w('| units | ' + ' | '.join(str(sd[k]) for k in sorted(sd)) + ' |')
w('')
w('%d of %d units have none. %d of those have a change in the texts that the ledger holds for no record on them, and are left out of the lists (§3.4). That leaves %d units untouched in substance, which are allowed vocabulary-only changes and layout: %d of them have no change of any kind in any version.' % (
    sd[0], n_elig, len(UNRECORDED), n_stable, sum(1 for r in ELIG if r['stable'] and not r['obs'] and not r['c']['vocab'])))
w('')
w('### 2.2 How long the untouched units have stood')
w('')
ag = Counter(r['nver'] for r in ELIG if r['stable'])
ag_all = Counter(r['nver'] for r in ELIG)
w('| versions carried | ' + ' | '.join(str(k) for k in range(1, 11)) + ' |')
w('| --- | ' + ' | '.join('---:' for _ in range(10)) + ' |')
w('| all %d units | ' % n_elig + ' | '.join(str(ag_all.get(k, 0)) for k in range(1, 11)) + ' |')
w('| untouched in substance | ' + ' | '.join(str(ag.get(k, 0)) for k in range(1, 11)) + ' |')
w('')
w('The untouched units fall into two clumps: %d have stood in all ten versions, since file 10, and %d are no older than draft 1; between them stand only %d (in 9 versions, since file 11, or 8, since draft 1). The cut is taken at all ten versions: those units came through all 22 rounds. The %d of 8 or 9 versions that pass every other test are listed apart (§3.3).' % (
    ag.get(10, 0), sum(v for k, v in ag.items() if k <= 7), ag.get(9, 0) + ag.get(8, 0), len(NEAR_AGE)))
w('')
w('### 2.3 Neighbour churn')
w('')
qs = [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]
w('| quantile | ' + ' | '.join(str(x) for x in qs) + ' | mean |')
w('| --- | ' + ' | '.join('---:' for _ in qs) + ' | ---: |')
w('| all %d units | ' % n_elig + ' | '.join(f2(round(quant([r['nb_subst'] for r in ELIG], x), 2)) for x in qs) + ' | %s |' % f2(round(statistics.mean(r['nb_subst'] for r in ELIG), 2)))
st10 = [r for r in ELIG if r['stable'] and r['nver'] == 10]
w('| untouched, in all ten versions (%d) | ' % len(st10) + ' | '.join(f2(round(quant([r['nb_subst'] for r in st10], x), 2)) for x in qs) + ' | %s |' % f2(round(statistics.mean(r['nb_subst'] for r in st10), 2)))
w('')
hist = Counter(min(int(r['nb_subst'] * 4) / 4, 3.0) for r in st10)
w('Untouched units in all ten versions, by neighbour churn (steps of 0.25; the last column is 3 or more):')
w('')
keys = [x / 4 for x in range(0, 13)]
w('| neighbour churn from | ' + ' | '.join(f2(k) for k in keys) + ' |')
w('| --- | ' + ' | '.join('---:' for _ in keys) + ' |')
w('| units | ' + ' | '.join(str(hist.get(k, 0)) for k in keys) + ' |')
w('')
cuts = [0.5, 0.75, 1.0, NB_CUT, 1.5, 2.0]
w('How many candidates each cut would give:')
w('')
w('| neighbour churn at least | ' + ' | '.join(f2(x) for x in cuts) + ' |')
w('| --- | ' + ' | '.join('---:' for _ in cuts) + ' |')
w('| candidates | ' + ' | '.join(str(sum(1 for r in st10 if r['nb_subst'] >= x)) for x in cuts) + ' |')
w('| of them challenged and kept | ' + ' | '.join(str(sum(1 for r in st10 if r['nb_subst'] >= x and r['nonvocab_props'])) for x in cuts) + ' |')
w('')
w('The cut is the upper quartile of neighbour churn over all %d units, %s: a candidate\'s neighbours changed more than those of three units in four. Half of all units have neighbours with fewer than %s substantive changes each. The distribution has no gap to cut at; the quartile is a plain, stated line, and the table above shows what a lower or higher line would give.' % (
    n_elig, f2(NB_CUT), f2(round(quant([r['nb_subst'] for r in ELIG], 0.5), 2))))
w('')

# ---- 3. strong candidates
w('## 3. Strong candidates')
w('')
w('Each unit: its wording now, where it stands, how long it has stood, what changed in it (vocabulary only, if anything), its neighbours\' churn, the proposals it came through (list 1 only), the terms it uses (the ledger\'s term list, matched as the ledger matched them) and what the dependence order of the latest text says those terms depend on. The dependence order names conditions by their tags; the match from a unit\'s words to a tag is by program (for example "account" to (E), "question" to (Q)) and is a lead, not a reading.')
w('')
w('| list | units | by group |')
w('| --- | ---: | --- |')
for nm, lst in (('challenged and kept', STRONG_C), ('never challenged', STRONG_N)):
    gc = Counter(r['group'][0] for r in lst)
    w('| %s | %d | %s |' % (nm, len(lst), ', '.join('%s %d' % kv for kv in sorted(gc.items()))))
w('')
w('### 3.1 Challenged and kept')
w('')
w('Proposals were made against these units and were declined, not applied, replaced by a later wording, or are open; each unit stands with no change in substance.')
w('')
w('| unit | section | since | neighbour churn | proposals (outcome) | vocabulary-only changes |')
w('| --- | --- | --- | ---: | --- | ---: |')
for r in STRONG_C:
    w('| %s | %s | %s | %s | %s | %d |' % (r['id'], SEC[r['section']]['name'], VSHORT[r['first']], f2(round(r['nb_subst'], 2)),
                                       ', '.join('%s %s' % (v, k) for k, v in sorted(Counter(p['outcome'] for p in r['nonvocab_props']).items())),
                                       r['c']['vocab']))
w('')
for r in STRONG_C:
    L.extend(unit_block(r))
w('### 3.2 Never challenged')
w('')
w('No proposal ever touched these units alone. That may mean no reader ever examined them; it does not mean they came through an attack.')
w('')
w('| unit | section | since | neighbour churn | vocabulary-only changes |')
w('| --- | --- | --- | ---: | ---: |')
for r in STRONG_N:
    w('| %s | %s | %s | %s | %d |' % (r['id'], SEC[r['section']]['name'], VSHORT[r['first']], f2(round(r['nb_subst'], 2)), r['c']['vocab']))
w('')
for r in STRONG_N:
    L.extend(unit_block(r, with_props=True))
w('### 3.3 Near the age cut: untouched since file 11 or draft 1')
w('')
w('These pass every test but have stood in eight or nine versions, not ten.')
w('')
if NEAR_AGE:
    w('| unit | section | since | versions | neighbour churn | list it would join |')
    w('| --- | --- | --- | ---: | ---: | --- |')
    for r in NEAR_AGE:
        w('| %s | %s | %s | %d | %s | %s |' % (r['id'], SEC[r['section']]['name'], VSHORT[r['first']], r['nver'], f2(round(r['nb_subst'], 2)),
                                           'challenged and kept' if r['nonvocab_props'] else 'never challenged'))
    w('')
    for r in NEAR_AGE:
        w('- **%s**:' % r['id'])
        w('\n'.join('  ' + l for l in q(r['text']).split('\n')))
    w('')
w('### 3.4 Left out: changed in the texts with no record on them')
w('')
w('These have no substantive change in the ledger, but their text changed between versions in a way the ledger places on another sentence or does not hold. They are not candidates.')
w('')
for r in sorted(UNRECORDED, key=lambda r: ORDER[r['id']]):
    w('- **%s** (%s):' % (r['id'], ', '.join('%s to %s' % (VSHORT[a], VSHORT[b]) for a, b, h in r['obs'] if h == 'unrecorded')))
    L.extend(seq_block(r['id'], '  '))
w('')

# ---- 4. most altered
w('## 4. The most altered')
w('')
w('Per section (the ledger\'s 134, less the dated note), distinct changes over its units and the records in its not-in-the-latest-text block (removed sentences, proposals never applied). Per unit = divided by the number of units in the section (headings included, as the ledger counts them). Sections of one or two units swing most; the counts are given beside the rates.')
w('')
w('Columns: **crit** criticism-driven changes; **owner** owner-directed; **vocab** vocabulary only; **repl** replaced wordings (of them from owner-directed passes); **decl** proposals declined; **n.a.** not applied; **open** open for the owner; **block** records with no sentence in the latest text.')
w('')


def srow(x, i):
    c = x['c']
    return '| %d | %s | %s | %d | %s | %s | %d | %d | %d | %d (%d) | %d | %d | %d | %d | %s |' % (
        i, sec_title(x['s']), x['s']['group'], x['n'], f2(round(x['crit_pu'], 2)), f2(round(x['tot_pu'], 2)),
        c['crit'], c['owner'], c['vocab'], c['sup'], c['sup_owner'], c['p_declined'], c['p_not applied'],
        c['p_open for the owner'], x['nblock'], '%d%%' % round(100 * x['owner_share']))


HDR = '| # | section | group | units | crit per unit | total per unit | crit | owner | vocab | repl (owner) | decl | n.a. | open | block | owner-directed share of churn |'
SEP = '| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |'
w('### 4.1 Sections, most criticism-driven changes per unit first (the first 20)')
w('')
w(HDR)
w(SEP)
for i, x in enumerate(BY_CRIT[:20], 1):
    w(srow(x, i))
w('')
w('### 4.2 Sections, most total churn per unit first (the first 20)')
w('')
w(HDR)
w(SEP)
for i, x in enumerate(BY_TOT[:20], 1):
    w(srow(x, i))
w('')
big = [x for x in SROWS if x['n'] >= 5]
w('### 4.3 Sections of five units or more, most criticism-driven changes per unit first (the first 10)')
w('')
w(HDR)
w(SEP)
for i, x in enumerate(sorted(big, key=lambda x: (-x['crit_pu'], x['s']['first']))[:10], 1):
    w(srow(x, i))
w('')
w('### 4.4 Units, most substantive changes first (the first 15)')
w('')
w('| # | unit | section | since | crit | owner | vocab | repl (owner) | decl | open | substantive | total |')
w('| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |')
for i, r in enumerate(TOP_UNITS, 1):
    c = r['c']
    w('| %d | %s | %s | %s | %d | %d | %d | %d (%d) | %d | %d | %d | %d |' % (
        i, r['id'], SEC[r['section']]['name'], VSHORT[r['first']], c['crit'], c['owner'], c['vocab'], c['sup'], c['sup_owner'],
        c['p_declined'] + c['p_declined_v'], c['p_open for the owner'] + c['p_open for the owner_v'], r['subst'], r['total']))
w('')
w('### 4.5 The ten sections with the most criticism-driven changes per unit: pattern and wordings')
w('')
w('Each section: its counts, the share of its churn from owner-directed passes, a pattern line per unit found by program (words per wording; longer or shorter; wordings that came back; words swapped; phrases added and taken out; splits), and the run of wordings the unit held, oldest first. A run lists the unit\'s text in each version where it differs from the version before, with the S96 stage-1 wordings (never kept as a file) in their place. Units with a single wording are named only.')
w('')
for i, x in enumerate(TOP_SECTIONS, 1):
    s = x['s']
    c = x['c']
    w('#### %d. %s' % (i, sec_title(s)))
    w('')
    w('Group %s %s · %d unit%s · criticism-driven %d, owner-directed %d, vocabulary-only %d, replaced wordings %d (%d from owner-directed passes), declined %d, open %d · owner-directed share of churn %d%%.' % (
        s['group'], s['gname'], x['n'], '' if x['n'] == 1 else 's', c['crit'], c['owner'], c['vocab'], c['sup'], c['sup_owner'], c['p_declined'], c['p_open for the owner'], round(100 * x['owner_share'])))
    w('')
    w('**Pattern, in plain words:** ' + SECTION_PATTERN[s['id']])
    w('')
    single = []
    for uid in x['units']:
        r = ROWS[uid]
        if len(r['seq']) <= 1:
            single.append(uid)
            continue
        w('- **%s** (%s; crit %d, owner %d, vocab %d, replaced %d): %s.' % (uid, r['kind'], r['c']['crit'], r['c']['owner'], r['c']['vocab'], r['c']['sup'], pattern_line(uid)))
        L.extend(seq_block(uid, '  '))
    if single:
        w('- One wording throughout: %s.' % ', '.join(single))
    blk = [b for b in s['block']]
    if blk:
        st = Counter(REC[b['records'][0]]['latest_status'] for b in blk)
        w('- Records with no sentence in the latest text, in the section\'s block: %d, in %d change%s (%s).' % (
            x['nblock'], len(blk), '' if len(blk) == 1 else 's', ', '.join('%s %d' % kv for kv in sorted(st.items()))))
    w('')
w('### 4.6 The fifteen units with the most substantive changes: pattern and wordings')
w('')
for i, r in enumerate(TOP_UNITS, 1):
    s = SEC[r['section']]
    w('#### %d. %s · %s' % (i, r['id'], sec_title(s)))
    w('')
    w('Criticism-driven %d, owner-directed %d, vocabulary-only %d, replaced wordings %d (%d from owner-directed passes), proposals declined %d, open %d; %s.' % (
        r['c']['crit'], r['c']['owner'], r['c']['vocab'], r['c']['sup'], r['c']['sup_owner'], r['c']['p_declined'],
        r['c']['p_open for the owner'], owner_marks(r['id'])))
    w('')
    w('Pattern: %s.' % pattern_line(r['id']))
    w('')
    L.extend(seq_block(r['id']))
    reps = []
    for x in sorted(BY_UNIT.get(r['id'], []), key=lambda x: x['lineup_order']):
        if x['status'] == 'superseded' and not x['applied_in'].startswith('stage-1') and x['_cls'] != 'vocab':
            wd = x['new_sentence'] or x['new']
            if wd and all(loose(wd) != loose(y['text']) for y in r['seq']) and wd not in [z[1] for z in reps]:
                reps.append((x, wd))
    if reps:
        w('- Proposed and replaced by a later wording (never held by the text):')
        for x, wd in reps:
            w('  - %s · %s · %s:' % (x['rid'], x['round'], x['kind']))
            w('\n'.join('    ' + l for l in q(wd).split('\n')))
    w('')
w('### 4.7 Every wording that came back')
w('')
w('A later wording that repeats an earlier one of the same unit after a different wording between: a change that did not stick. *Exact* means the same once emphasis and spacing are set aside; *near* means a similarity of 0.97 or more with a different wording between.')
w('')
if RETURNS:
    w('| unit | section | kind | the wording of | came back in | pattern |')
    w('| --- | --- | --- | --- | --- | --- |')
    for uid, kind, i, k in sorted(RETURNS, key=lambda x: ORDER[x[0]]):
        seq = ROWS[uid]['seq']
        w('| %s | %s | %s | %s | %s | %s |' % (uid, SEC[ROWS[uid]['section']]['name'], kind, seq_label(seq[i]), seq_label(seq[k]), pattern_line(uid).replace('|', '/')))
    w('')
    for uid in sorted({x[0] for x in RETURNS}, key=ORDER.get):
        w('- **%s**:' % uid)
        L.extend(seq_block(uid, '  '))
    w('')
w('Phrases added and later taken out, or taken out and later put back (%d):' % len(PHRASE_RETURNS))
w('')
w('| unit | section | what happened | phrase | first step | second step |')
w('| --- | --- | --- | --- | --- | --- |')
for uid, kind, ph, a, b in sorted(PHRASE_RETURNS, key=lambda x: (ORDER[x[0]], x[3])):
    seq = ROWS[uid]['seq']
    w('| %s | %s | %s | %s | %s | %s |' % (uid, SEC[ROWS[uid]['section']]['name'], kind, ph.replace('|', '/')[:120], seq_label(seq[a]), seq_label(seq[b])))
w('')

# ---- 5. values
w('## 5. The values group')
w('')
w('The units of group G11 (Part XI, "Repair, created explanation, and appraisal", with grievance 8 filed there) and every unit elsewhere whose wording in any version speaks of worth, appraisal, aesthetics, the normative or appraisal relation \\(\\mathcal N\\), merit, or an order of explanations or thinkers: %d units.' % len(VALUES))
w('')
w('| unit | section | since | crit | owner | vocab | repl | decl | open | substantive | neighbour churn | strong list |')
w('| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |')
for uid in VALUES:
    r = ROWS[uid]
    c = r['c']
    w('| %s | %s | %s | %d | %d | %d | %d | %d | %d | %d | %s | %s |' % (
        uid, SEC[r['section']]['name'], VSHORT[r['first']], c['crit'], c['owner'], c['vocab'], c['sup'],
        c['p_declined'] + c['p_declined_v'], c['p_open for the owner'] + c['p_open for the owner_v'], r['subst'],
        f2(round(r['nb_subst'], 2)), r['strong'] or (('untouched, below the neighbour cut' if r['nver'] == 10 else 'untouched, younger than file 10') if r['stable'] else '')))
w('')
vr = [ROWS[u] for u in VALUES]
vs = [r for r in vr if r['kind'] != 'heading']
w('- Units: %d; substantive changes %d in all, %s per unit (all %d units: %s). Criticism-driven %d, owner-directed %d, vocabulary-only %d.' % (
    len(vr), sum(r['subst'] for r in vr), f2(round(sum(r['subst'] for r in vr) / len(vr), 2)), n_elig,
    f2(round(sum(r['subst'] for r in ELIG) / n_elig, 2)), sum(r['c']['crit'] for r in vr), sum(r['c']['owner'] for r in vr), sum(r['c']['vocab'] for r in vr)))
w('- Strong candidates among them: %s.' % (', '.join('%s (%s)' % (r['id'], r['strong']) for r in vr if r['strong']) or 'none'))
w('- Untouched in substance, not on the lists: %s.' % (', '.join('%s (%s)' % (r['id'], 'neighbour churn below the cut' if r['nver'] == 10 else 'since ' + VSHORT[r['first']]) for r in vr if r['stable'] and not r['strong'] and r['kind'] != 'heading') or 'none'))
openv = [(r['id'], p) for r in vr for p in r['props'] if p['outcome'] == 'open for the owner']
w('- Proposals open for the owner on these units: %s.' % ('; '.join('%s on %s' % (p['cid'], uid) for uid, p in openv) or 'none'))
w('')
VAL_WORDS = [u for u in VALUES if any(VAL_RX.search(h['text']) for h in CHAINS[u])]
f10_import = [h['text'] for h in CHAINS['L518.s1'] if h['v'] == 'f10'][0]
nv = ROWS['L455.s5']
w('**Pattern, in plain words.** From file 10 on, the text has taken values from outside it: file 10\'s second import reads "%s" That arrangement stands in every version; what changed is its name and the wording around it. The scrub renamed it ("normative relation" to "appraisal relation", "worth" to "an appraisal", "primitive" to "import"), the heading of Part XI went from "Progress, knowledge, and the normative" to "Repair, created explanation, and appraisal", and "obligations" became "aims". The sentences that say the semantics does not supply or define it grew: "%s" gained a clause in file 11 and its verb changed in the scrub; the import\'s own sentence grew from %d to %d words. The value units have %s substantive changes each, against %s for all units; %d of the %d are strong candidates. One proposal on the Appraisal paragraph is open for the owner (below).' % (
    f10_import.split('. ', 1)[1] if f10_import.startswith('2. ') else f10_import,
    [h['text'] for h in CHAINS['L455.s5'] if h['v'] == 'f10'][0],
    len(loose([h['text'] for h in CHAINS['L518.s1'] if h['v'] == 'f10'][0]).split()), len(loose(ROWS['L518.s1']['text']).split()),
    f2(round(sum(r['subst'] for r in vr) / len(vr), 2)), f2(round(sum(r['subst'] for r in ELIG) / n_elig, 2)),
    sum(1 for r in vr if r['strong']), len(vr)))
w('')
w('Runs of wordings of the %d units whose wording in some version speaks of worth, appraisal, aesthetics, the normative or appraisal relation, merit, or an order of explanations or thinkers (the repair units of Part XI without such words are in the table and the data file only):' % len(VAL_WORDS))
w('')
for uid in VAL_WORDS:
    r = ROWS[uid]
    if len(r['seq']) > 1:
        w('- **%s** (%s): %s.' % (uid, SEC[r['section']]['name'], pattern_line(uid)))
        L.extend(seq_block(uid, '  '))
w('')
OPENV = defaultdict(list)
for uid in VALUES:
    for p in ROWS[uid]['props']:
        if p['outcome'] == 'open for the owner':
            OPENV[p['cid']].append((uid, p))
for cid, lst in OPENV.items():
    for uid, p in lst[:1]:
            w('Open proposal %s (%s), on %s:' % (cid, 'a vocabulary proposal' if p['vocab'] else 'on this sentence', ', '.join(u for u, _ in lst)))
            w('')
            seen = set()
            for x in p['recs']:
                wd = x['new_sentence'] or x['new']
                if wd in seen:
                    continue
                seen.add(wd)
                w('- %s · %s · %s · %s · source: %s — %s' % (x['rid'], x['round'], x['kind'], x['status'], x['source_file'], x['source_ref']))
                w('\n'.join('  ' + l for l in prop_wording(x).split('\n')))
            w('')
w('The dependence order of the latest text does not name the appraisal relation; its list of imports (Part XIV) says:')
w('')
for s in DEP_SENTS:
    if 'appraisal' in s:
        w(q(s))
        w('')

# ---- 6. unsure
w('## 6. What is unsure')
w('')
w('- **Untouched may mean unexamined.** A unit no proposal touched may never have been read closely; list 2 says nothing about how it would fare.')
w('- **The counts depend on how the ledger split and placed things.** A change is counted on the sentences the ledger placed it on; %d records were placed by the line they were written against, not by their own words, and a change to one sentence may stand on its neighbour (§3.4 shows four such cases). R2\'s %d proposals were written against file 20, which the repository does not hold, and read as amendments to file 10.' % (
    sum(1 for r in recs if (r['anchor_method'] or '').startswith('line map')), sum(1 for r in recs if r['round'] == 'R2 (log 25)')))
w('- **Following a unit back is by similarity.** A heavily reworded sentence can be taken for new (it then looks younger than it is), and two different sentences can, rarely, be taken for one (the unit then shows a change it never had, which keeps it off the lists).')
w('- **A record that names several sentences counts on each.** A paragraph-wide edit, or the removal of a sentence listed with the sentences of its paragraph, adds a change to sentences whose own words did not change (L536.s2 has five changes and one wording since file 11). And the scrub recorded each word swap as its own change, so a long sentence can carry many vocabulary-only changes (%d on the Genesis item).' % ROWS['L542.s1']['c']['vocab'])
w('- **Owner-directed passes inflate churn.** The scrub touched %d units and the S96 and S97 owner-directed stages %d; their counts are given apart everywhere, and the neighbour churn used for the cut includes them.' % (
    sum(1 for r in ROWS.values() if any(REC_ for REC_ in BY_UNIT.get(r['id'], []) if REC_['round'] == 'S95' and 'Scrub - scripts/replacements' in REC_['source_file'])),
    sum(1 for r in ROWS.values() if any(x['_cls'] == 'owner' and x['round'] in ('S96', 'S97') for x in BY_UNIT.get(r['id'], [])))))
w('- **Which class a change falls in follows the definitions given**, not a reading of each change: the repairs the S95 readings asked for count as criticism-driven though they were applied with an owner-directed pass; draft 4\'s restatement of hard to vary followed the owner\'s decision S20 and counts as criticism-driven (%d changes on units of the latest text came from S91).' % len({x['change_id'] for x in recs if x['round'] == 'S91' and x['status'] == 'applied' and x['latest_sentences']}))
w('- **Per-unit rates swing for small sections**; §4.3 gives the sections of five units or more.')
w('- **The thresholds are stated lines, not gaps in the data** (§2). A different line moves units on and off the lists.')
w('')
w('## 7. Files and rerun')
w('')
w('- This page; the data, one row per unit (756), `%s - data.csv`; the script, `%s`.' % (NAME, SCRIPT))
w('- Inputs, read only, each tested against its md5 by the script: %s; and the ten theory texts, tested against the md5s the line maps name.' % '; '.join('`%s` (%s)' % (os.path.relpath(p, SEM + '/results'), h) for p, h in INPUTS.items()))
w('- Rerun from `results/`: `PYTHONDONTWRITEBYTECODE=1 python3 "%s"` (about two minutes).' % SCRIPT)
w('')
open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L).rstrip('\n') + '\n')

# ---- CSV
COLS = ['unit_id', 'line', 'kind', 'group', 'group_name', 'section_id', 'section', 'first_version', 'versions_carried',
        'rounds_came_through', 'text_changes_between_versions', 'text_change_kinds', 'criticism_driven_changes',
        'owner_directed_changes', 'vocabulary_only_changes', 'replaced_wordings', 'replaced_wordings_owner_directed',
        'replaced_wordings_vocabulary', 'proposals_declined', 'proposals_not_applied', 'proposals_superseded',
        'proposals_open_for_the_owner', 'proposals_unknown', 'vocabulary_proposals', 'substantive_changes', 'total_churn',
        'neighbours', 'neighbour_substantive_churn_mean', 'neighbour_criticism_driven_mean', 'untouched_in_substance',
        'strong_candidate_list', 'wordings_held', 'wording_came_back', 'values_group', 'is_dated_note', 'terms', 'text']
with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
    cw = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    cw.writerow(COLS)
    back = {x[0] for x in RETURNS}
    for u in units:
        r = ROWS[u['id']]
        c = r['c']
        cw.writerow([r['id'], r['line'], r['kind'], r['group'][0], r['group'][1], r['section'], SEC[r['section']]['name'],
                     VSHORT[r['first']], r['nver'], r['rounds'], len(r['obs']), '; '.join('%s>%s %s' % o for o in r['obs']),
                     c['crit'], c['owner'], c['vocab'], c['sup'], c['sup_owner'], c['sup_vocab'], c['p_declined'],
                     c['p_not applied'], c['p_superseded'], c['p_open for the owner'], c['p_unknown'],
                     sum(v for k, v in c.items() if k.startswith('p_') and k.endswith('_v')), r['subst'], r['total'],
                     len(r['nb']), round(r['nb_subst'], 3), round(r['nb_crit'], 3), 'yes' if r['stable'] else 'no',
                     r['strong'], len(r['seq']), 'yes' if r['id'] in back else 'no', 'yes' if r['id'] in VALUES else 'no',
                     'yes' if r['note'] else 'no', '; '.join(r['terms']), r['text']])
print('wrote', OUT_MD, os.path.getsize(OUT_MD))
print('wrote', OUT_CSV, os.path.getsize(OUT_CSV))
print('strong: challenged', len(STRONG_C), 'never', len(STRONG_N), 'near age', len(NEAR_AGE), 'cut', NB_CUT)
print('returns', len(RETURNS), 'phrase returns', len(PHRASE_RETURNS))
