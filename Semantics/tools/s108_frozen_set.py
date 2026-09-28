#!/usr/bin/env python3
"""s108_frozen_set.py: Part A of decision S52 (log S108): the frozen set, "the parts that are hard to vary", by
program from the record. Written 28 September 2026 by a Claude subagent (Opus 5.5) for the orchestrator.

Claude's working reading of S52 (not approved by the owner): the parts that are hard to vary are the sentences and
definitions that readers tried to vary across the rounds and that came through unchanged while the parts around them
kept changing (the owner's own approach of S31). Applied here as a criterion on every sentence of the current text and
every definition of the current formal core:

  FROZEN when both hold:
   (a) it was put to the readers or checkers at least once (challenged or tested);
   (b) no round or step changed it.
  Everything else is the MIDDLE. Where the record cannot tell, the item goes to the middle and its reason says so.

  python3 Semantics/tools/s108_frozen_set.py --state s106 --out-dir DIR   the history up to S106 (round 4 not in)
  python3 Semantics/tools/s108_frozen_set.py --state r4                    the state after round 4: writes
        results/S108 Part A - the frozen set.json and .md (refuses to write over a file whose content differs)
  python3 Semantics/tools/s108_frozen_set.py --state r4 --check            rebuild in memory, compare, write nothing

It reads only. Every input is checked by md5 where the record gives one. A rerun gives the same bytes.
"""
import argparse, csv, difflib, hashlib, json, os, re, sys
from collections import Counter, defaultdict, OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE) if os.path.basename(HERE) == 'tools' else '/home/user/ThreadSmith/Semantics'
LED = SEM + '/results/S98 Ledger of edits and recommendations'
sys.path.insert(0, LED + '/group/anchor - scripts')
from lib_anchor import split_sents  # noqa: E402  (read only: the ledger's own sentence splitter, as S100 used it)

R = 'results/'
T = 'tests/'
OUT_JSON = R + 'S108 Part A - the frozen set.json'
OUT_MD = R + 'S108 Part A - the frozen set.md'

S100_CSV = R + 'S100 Strong candidates and the most altered sections - data.csv'
S101_GRAPH = R + 'S101 What the tested strong candidates depend on - graph.json'
UNITS = R + 'S98 Ledger of edits and recommendations/group/sentence index of the latest text.jsonl'
R2_PART = T + 'S104 Round 2 - the maths against the words - part '
R2_TAB = R + 'S104 Round 2 - tabulation of the replies, before any ruling.json'
R3_TAB = (R + 'S105 Round 3 - tabulation of the replies, before any ruling.md', '## 3. Findings', '## 4. Proposals whole')

VERSIONS = [
    ('latest', "the ledger's latest text", T + 'Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md',
     'ebca15a047f686b15d5f5766b69825c9'),
    ('S99', 'S99 (the text made to stand alone)', T + '99 The semantics, standing alone.md', '74f4a4c7619345747f4fa976ddac9548'),
    ('R1', 'round 1 (S103)', T + '103 The semantics, standing alone, after round 1.md', 'f31ebb1f050783f1a84f6136cec20fcd'),
    ('R2', 'round 2 (S104)', T + '104 The semantics, standing alone, after round 2.md', '735ec1e8256cc6a251715a031944ea65'),
    ('Q', "the owner's answers step (S41)", T + "104 The semantics, standing alone, after round 2, with the owner's answers.md",
     'bc14045aae3139df710d8339a9c1c81b'),
    ('R3', 'round 3 (S105)', T + '105 The semantics, standing alone, after round 3.md', 'da9a30cd052d46f2a5ead259cea97d3c'),
    ('S106', 'S106 (the written-in test taken out; S47 inside it)',
     T + '106 The semantics, standing alone, without the written-in test.md', 'c7af964c329ab7959243405d394e6574'),
]
CORES = [
    ('R2build', 'round 2, as put to the readers', R + 'S104 Round 2 - maths/formal core.md', None),
    ('R2', "round 2's reading, its second check and the owner's answers step",
     R + 'S104 Round 2 - maths after the reading/formal core, after round 2.md', None),
    ('R3', 'round 3 (S105)', R + 'S105 Round 3 - maths after the reading/formal core, after round 3.md',
     '9202ad317a5987481d4374cf5d718d8b'),
    ('S106', 'S106 (with S47)', R + 'S106 The written-in test taken out/formal core, after S106.md',
     '40d7c80ec78574794962fece34a4cb51'),
]
CLAIMS = (R + 'S106 The written-in test taken out/formal claims, after S106.json', 'e02291ba44e78e56a44a23cb626a703b')
# The state after round 4 (log S107), final after its second checker (ea1047a): tests/107 is tests/106 byte for byte
# (round 4's two text changes were withdrawn); the maths changed.
R4M = R + 'S107 Round 4 - maths after the reading/'
R4 = {
    'version': ('R4', 'round 4 (S107)', T + '107 The semantics, standing alone, after round 4.md',
                'c7af964c329ab7959243405d394e6574'),
    'core': ('R4', 'round 4 (S107) and its second check', R4M + 'formal core, after round 4.md',
             'd6e6ec62acbc6ef763e07b7cd7b29540'),
    'claims': (R4M + 'formal claims, after round 4.json', '3d9864f1be8ec8b88914dc2800af4288'),
    'tab': (R + 'S107 Round 4 - tabulation of the replies, before any ruling.md', '## 3. Findings', '## 4. Proposals whole'),
}
LIST = re.compile(r'^(- |\d+\. )')   # a list line is one unit, as the ledger indexes it
MARK = re.compile(r'^(r\d+b?|owner S\d+|S\d+b?)\s*:')
DEF = re.compile(r'^\*\*((?:D\d+\.(?:\d+|new\d+|XV))|(?:E\d+))\b')
STAGE_OF_MARK = [(re.compile(r'^r2b?:'), 'R2'), (re.compile(r'^owner S41:'), 'Q'), (re.compile(r'^r3b?:'), 'R3'),
                 (re.compile(r'^(S106b?|S47):'), 'S106'), (re.compile(r'^(r4b?|S107b?):'), 'R4')]
SECTION_PART = {0: 'Part 0', 1: 'Part II', 2: 'Part II', 3: 'Part III', 4: 'Part II', 5: 'Part IV', 6: 'Part V',
                7: 'Part VI', 8: 'Part VI', 9: 'Part IX', 10: 'Part VI', 11: 'Part IV', 12: 'Part IV', 13: 'Part X',
                14: 'Part XI', 15: 'Part XII', 16: 'Part XIII', 17: 'Part VII', 18: 'Part XIV'}
DEF_PART = {'D16.XV': 'Part XV'}   # its body is Part XV's defeat conditions, which it quotes inside, not above
PARTS = ['Front matter', 'Part 0', 'Part I', 'Part II', 'Part III', 'Part IV', 'Part V', 'Part VI', 'Part VII',
         'Part VIII', 'Part IX', 'Part X', 'Part XI', 'Part XII', 'Part XIII', 'Part XIV', 'Part XV', 'Part XVI']


def p(rel):
    return os.path.join(SEM, rel)


def read(rel):
    with open(p(rel), encoding='utf-8') as f:
        return f.read()


def md5f(rel):
    with open(p(rel), 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def md5s(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit('refused: ' + msg)


def lines_of(rel):
    ls = read(rel).split('\n')
    return ls[:-1] if ls and ls[-1] == '' else ls


# ------------------------------------------------------------------ the text
def parts_of(lines):
    out, cur = {}, 'Front matter'
    for n, l in enumerate(lines, 1):
        m = re.match(r'^# (Part [0IVX]+) — ', l)
        if m:
            cur = m.group(1)
        out[n] = cur
    return out


def current_items(lines):
    """Every sentence of the current text as the ledger splits it; a display (\\[ … \\]) and a list line are one item
    each; headings, rules (---) and blank lines are left out."""
    items, n, N = [], 1, len(lines)
    while n <= N:
        l = lines[n - 1]
        if l.strip() == '\\[':
            m = n
            while m <= N and lines[m - 1].strip() != '\\]':
                m += 1
            items.append({'line': n, 'line_end': m, 'kind': 'display', 'text': '\n'.join(lines[n - 1:m]), 'k': 1})
            n = m + 1
            continue
        if l.startswith('#') or not l.strip() or l.strip() == '---':
            n += 1
            continue
        if LIST.match(l):
            items.append({'line': n, 'line_end': n, 'kind': 'list item', 'text': l, 'k': 1})
        else:
            for k, s in enumerate(split_sents(l), 1):
                items.append({'line': n, 'line_end': n, 'kind': 'sentence', 'text': s, 'k': k})
        n += 1
    return items


def sents_at(lines, n, line_end):
    if line_end != n:
        return ['\n'.join(lines[n - 1:line_end])]
    if n > len(lines):
        return []
    return [lines[n - 1]] if LIST.match(lines[n - 1]) else split_sents(lines[n - 1])


# ------------------------------------------------------------------ the formal core
def _bracket_end(s, i):
    depth, j = 0, i
    while j < len(s):
        if s[j] == '[':
            depth += 1
        elif s[j] == ']':
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return len(s) - 1


def strip_marks(s):
    """The body of a definition without its change marks ([r2: …], [owner S41: …], [S106: …], nested brackets allowed)
    and without invention references ([I04], [I40, fixed]); bold and spacing normalized."""
    out, i = [], 0
    while i < len(s):
        if s[i] == '[':
            j = _bracket_end(s, i)
            inner = s[i + 1:j]
            if MARK.match(inner) or re.match(r'^(I\d+|Inn)', inner):
                i = j + 1
                continue
        out.append(s[i])
        i += 1
    t = ''.join(out).replace('**', '')
    t = re.sub(r'\s+', ' ', t).strip()
    return re.sub(r'\s+([.;,:])', r'\1', t)


def marks_in(s):
    found, i = [], 0
    while i < len(s):
        if s[i] == '[':
            j = _bracket_end(s, i)
            inner = s[i + 1:j]
            if MARK.match(inner):
                found.append(inner)
        i += 1
    return found


def parse_core(rel):
    """Definitions D§.n and encodings En in order, each with the quotations `> Lnnn | …` above it (and those above
    an unnumbered note that follows it in the same section) and its body."""
    blocks, section, pending, cur = [], None, [], None
    for i, l in enumerate(read(rel).split('\n'), 1):
        if l.startswith('## '):
            section, cur, pending = l[3:].strip(), None, []
            continue
        m = DEF.match(l)
        if m:
            cur = {'id': m.group(1), 'section': section, 'quotes': list(pending), 'body': [l], 'at': i}
            blocks.append(cur)
            pending = []
            continue
        q = re.match(r'^> L(\d+) \| ?(.*)$', l)
        if q:
            pending.append((int(q.group(1)), q.group(2)))
            continue
        if not l.strip():
            continue
        if l.startswith('**Vague') or l.startswith('#') or (l.startswith('*') and not l.startswith('**')) \
                or l.startswith('**Counts') or l.startswith('**What'):
            cur, pending = None, []
            continue
        if cur is not None and cur['section'] == section:
            cur['body'].append(l)
            cur['quotes'] += pending
            pending = []
            continue
        pending = []
    return OrderedDict((b['id'], b) for b in blocks)


def quote_units(n, qtext, units_by_line):
    """The units of line n (or of the display holding n) that a quoted fragment covers (' … ' joins fragments)."""
    frags = [f.strip() for f in qtext.split(' … ') if f.strip()]
    hit = []
    for u in units_by_line.get(n, []):
        ut = u['text']
        for f in frags:
            if f in ut or ut in f:
                hit.append(u['id'])
                break
            m = difflib.SequenceMatcher(None, f, ut, autojunk=False).find_longest_match(0, len(f), 0, len(ut))
            if m.size >= min(30, max(8, int(0.8 * min(len(f), len(ut))))):
                hit.append(u['id'])
                break
    return hit


def table_rows(text, start, end):
    """Rows of the markdown tables between two headings: (first cell, cells)."""
    a = text.index(start)
    b = text.index(end, a)
    for row in text[a:b].split('\n'):
        if not row.startswith('| ') or row.startswith('|---') or re.match(r'^\| *id\b', row):
            continue
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        if len(cells) >= 3:
            yield cells[0].split(' ')[0], cells


def stage_label(k, stages, labels):
    """The core after round 2 was written by round 2's reading, its second check and the owner's answers step: say
    which, from the marks the definition carries."""
    if k != 'R2':
        return labels[k]
    r2, q = 'R2' in stages, 'Q' in stages
    if r2 and q:
        return "round 2 (S104) and the owner's answers step (S41)"
    if q:
        return "the owner's answers step (S41)"
    if r2:
        return 'round 2 (S104)'
    return "round 2 or the owner's answers step (no mark says which)"


# ------------------------------------------------------------------ the analysis
def analyse(state):
    versions = list(VERSIONS) + ([R4['version']] if state == 'r4' else [])
    cores = list(CORES) + ([R4['core']] if state == 'r4' else [])
    claims_rel, claims_md5 = R4['claims'] if state == 'r4' else CLAIMS
    tabs = [R3_TAB] + ([R4['tab']] if state == 'r4' else [])
    inputs = OrderedDict()
    for k, lab, rel, h in versions:
        need(os.path.isfile(p(rel)), '%s is not there' % rel)
        inputs[rel] = md5f(rel)
        need(h is None or inputs[rel] == h, '%s has md5 %s, expected %s' % (rel, inputs[rel], h))
    for k, lab, rel, h in cores:
        need(os.path.isfile(p(rel)), '%s is not there' % rel)
        inputs[rel] = md5f(rel)
        need(h is None or inputs[rel] == h, '%s has md5 %s, expected %s' % (rel, inputs[rel], h))
    need(os.path.isfile(p(claims_rel)), '%s is not there' % claims_rel)
    inputs[claims_rel] = md5f(claims_rel)
    need(claims_md5 is None or inputs[claims_rel] == claims_md5, '%s: md5' % claims_rel)
    for rel in [S100_CSV, S101_GRAPH, UNITS, R2_TAB] + [t[0] for t in tabs]:
        inputs[rel] = md5f(rel)
    parts17 = sorted(f for f in os.listdir(p(T)) if f.startswith(os.path.basename(R2_PART)))
    need(len(parts17) == 17, 'round 2 has %d parts, 17 expected' % len(parts17))
    for f in parts17:
        inputs[T + f] = md5f(T + f)

    units = [json.loads(x) for x in read(UNITS).splitlines() if x.strip()]
    s100 = {r['unit_id']: r for r in csv.DictReader(open(p(S100_CSV), encoding='utf-8'))}
    g101 = json.load(open(p(S101_GRAPH), encoding='utf-8'))
    unit_nodes = defaultdict(list)
    for nd in g101['nodes']:
        for s in nd.get('sentences') or []:
            unit_nodes[s['id']].append('%s (%s)' % (nd['id'], nd.get('stability')))
    vlines = OrderedDict((k, lines_of(rel)) for k, _, rel, _ in versions)
    vlabel = {k: lab for k, lab, _, _ in versions}
    for k, ls in vlines.items():
        need(len(ls) == 632, '%s has %d lines, not 632: the texts are no longer one line to one line' % (k, len(ls)))
    cur_key = list(vlines)[-1]
    cur = vlines[cur_key]
    part_of = parts_of(cur)
    ubl = defaultdict(list)
    for u in units:
        for n in range(u['line'], u['line_end'] + 1):
            ubl[n].append(u)
    for u in units:
        u['absent_in'] = [k for k, ls in vlines.items() if u['text'] not in sents_at(ls, u['line'], u['line_end'])]

    # ---- formal cores: every definition of the last core, its history of bodies
    core = OrderedDict((k, parse_core(rel)) for k, _, rel, _ in cores)
    clabel = {k: lab for k, lab, _, _ in cores}
    ckeys = list(core)
    last = core[ckeys[-1]]
    defs = OrderedDict()
    for did, b in last.items():
        d = {'id': did, 'section': b['section'], 'quotes': b['quotes'], 'present_in': [], 'changed_at': [],
             'marks': marks_in('\n'.join(b['body']))}
        prev = None
        for k in ckeys:
            bb = core[k].get(did)
            if bb is None:
                continue
            body = strip_marks('\n'.join(bb['body']))
            d['present_in'].append(k)
            if prev is not None and body != prev:
                d['changed_at'].append(k)
            prev = body
        d['first'] = d['present_in'][0]
        d['mark_stages'] = sorted({st for m in d['marks'] for rx, st in STAGE_OF_MARK if rx.match(m)})
        lines = sorted({q[0] for q in d['quotes']})
        d['lines'] = lines
        sec = int(re.match(r'§(\d+)', b['section']).group(1))
        parts = Counter(part_of[n] for n in lines)
        d['part'] = DEF_PART.get(did) or (parts.most_common(1)[0][0] if parts else SECTION_PART[sec])
        d['part_by'] = 'fixed' if did in DEF_PART else ('its quotations' if parts else 'its section of the core')
        defs[did] = d
    gone = [did for k in ckeys for did in core[k] if did not in last]

    unit_defs = defaultdict(set)
    for did, d in defs.items():
        d['units'] = []
        for n, qt in d['quotes']:
            for uid in quote_units(n, qt, ubl):
                if uid not in d['units']:
                    d['units'].append(uid)
                unit_defs[uid].add(did)
    claims = json.load(open(p(claims_rel), encoding='utf-8'))['claims']
    unit_claims, claim_lines = defaultdict(set), {}
    for c in claims:
        claim_lines[c['id']] = sorted({s['line'] for s in c.get('source') or []})
        for s in c.get('source') or []:
            for uid in quote_units(s['line'], s.get('quote') or '', ubl):
                unit_claims[uid].add(c['id'])
    r2q = defaultdict(set)
    for f in parts17:
        pn = int(re.search(r'part (\d+)', f).group(1))
        for l in read(T + f).split('\n'):
            q = re.match(r'^> L(\d+) \| ?(.*)$', l)
            if q:
                for uid in quote_units(int(q.group(1)), q.group(2), ubl):
                    r2q[uid].add(pn)
    tab2 = json.load(open(p(R2_TAB), encoding='utf-8'))
    r2_put = {i['id'] for i in tab2['items'] + tab2['rule7_records'] if i['kind'] in ('definition', 'encoding')}
    r2_chal = {i['id'] for i in tab2['items'] if i['kind'] in ('definition', 'encoding')}
    find_lines, find_defs = defaultdict(set), defaultdict(set)
    for i in tab2['items']:
        for n in i.get('lines') or []:
            find_lines[n].add('R2:' + i['id'])
    for rel, a, b in tabs:
        rnd = 'R3' if 'S105' in rel else 'R4'
        for fid, cells in table_rows(read(rel), a, b):
            for n in re.findall(r'L(\d+)', cells[2]):
                find_lines[int(n)].add('%s:%s' % (rnd, fid))
            for did in re.findall(r'\b(D\d+\.(?:\d+|new\d+|XV)|E\d)\b', cells[1]):
                find_defs[did].add('%s:%s' % (rnd, fid))
    round1 = {uid for uid, r in s100.items() if r['strong_candidate_list'] == 'never challenged'}

    # ---- the sentences of the current text
    ukey = {(u['line'], u['text']): u for u in units}
    out = []
    for it in current_items(cur):
        u = ukey.get((it['line'], it['text']))
        rec = OrderedDict(id=None, line=it['line'], line_end=it['line_end'], part=part_of[it['line']],
                          kind=it['kind'], text=it['text'])
        line_defs = sorted(d for d, dd in defs.items() if it['line'] in dd['lines'])
        line_claims = sorted(c for c, ls in claim_lines.items() if it['line'] in ls)
        if u is None:
            first = next((k for k in vlines if it['text'] in sents_at(vlines[k], it['line'], it['line_end'])), None)
            need(first != 'latest', 'L%d: a sentence of the latest text the ledger does not index: %r' % (it['line'], it['text'][:60]))
            rec.update(id='L%d.n%d' % (it['line'], it['k']), unit=None, status='MIDDLE',
                       changed_by=[vlabel.get(first, '?')], defs=line_defs, claims=line_claims, evidence_a=[],
                       s101_nodes=[], s100_list='',
                       reason='its words are new since the ledger\'s latest text: written by %s' % vlabel.get(first, '?'))
            out.append(rec)
            continue
        uid, r = u['id'], s100.get(u['id'], {})
        ev = []
        props = sum(int(r.get(k) or 0) for k in ('proposals_declined', 'proposals_not_applied',
                                                 'proposals_superseded', 'proposals_open_for_the_owner'))
        if props:
            ev.append('challenged before the review rounds: %d proposal(s) placed on it by the ledger, none applied' % props)
        if uid in round1:
            ev.append('put to both readers in round 1 and kept')
        if r2q.get(uid):
            ev.append('quoted beside its maths to both readers in round 2 (part %s)' % ', '.join(str(x) for x in sorted(r2q[uid])))
        if unit_claims.get(uid):
            ev.append('tested by the program: %s' % ', '.join(sorted(unit_claims[uid], key=claim_key)))
        fl = sorted(find_lines.get(it['line'], set()))
        alone = len([x for x in ubl[it['line']] if x['kind'] != 'heading']) == 1
        if fl and alone:
            ev.append('named by findings on its line, which holds no other sentence: %s' % ', '.join(fl[:6]))
        changed = []
        if r.get('untouched_in_substance') != 'yes':
            changed.append("before the review rounds (%s substantive change(s) in the ledger, as S100 counts them)"
                           % (r.get('substantive_changes') or '?'))
        changed += [vlabel[k] for k in u['absent_in']]
        rec.update(id=uid, unit=uid, first_version=r.get('first_version'), versions_carried=r.get('versions_carried'),
                   s100_list=r.get('strong_candidate_list') or '', s101_nodes=unit_nodes.get(uid, []),
                   defs=sorted(unit_defs.get(uid, set()) or set(line_defs), key=def_key),
                   defs_by='quotation' if unit_defs.get(uid) else ('line' if line_defs else ''),
                   claims=sorted(unit_claims.get(uid, set()) or set(line_claims), key=claim_key),
                   evidence_a=ev, findings_on_line=fl, changed_by=changed)
        if changed:
            rec['status'] = 'MIDDLE'
            rec['reason'] = 'changed: ' + '; '.join(changed)
        elif ev:
            rec['status'] = 'FROZEN'
            rec['reason'] = 'unchanged in every version and step; ' + ev[0]
        elif fl:
            rec['status'] = 'MIDDLE'
            rec['reason'] = ('unchanged; only its line was named by findings (%s), and the line holds other sentences: '
                             'the record cannot tell whether it was put' % ', '.join(fl[:3]))
        else:
            rec['status'] = 'MIDDLE'
            rec['reason'] = 'unchanged, but the record shows it never put to a reader or checker by itself'
        out.append(rec)

    # ---- the definitions of the current core
    outd = []
    for did, d in defs.items():
        ev = []
        if did in r2_put:
            ev.append('put to both readers in round 2' + (', challenged' if did in r2_chal else ', not challenged'))
        if find_defs.get(did):
            ev.append('named by findings: %s' % ', '.join(sorted(find_defs[did])[:6]))
        changed = []
        if d['first'] != ckeys[0]:
            changed.append('new in ' + stage_label(d['first'], d['mark_stages'], clabel))
        changed += ['changed in ' + stage_label(k, d['mark_stages'], clabel) for k in d['changed_at']]
        rec = OrderedDict(id=did, section=d['section'], part=d['part'], part_by=d['part_by'], lines=d['lines'], units=d['units'],
                          claims=sorted({c for c, ls in claim_lines.items() if set(ls) & set(d['lines'])}, key=claim_key),
                          first=clabel[d['first']], changed_by=changed, mark_stages=d['mark_stages'], evidence_a=ev)
        if changed:
            rec['status'], rec['reason'] = 'MIDDLE', '; '.join(changed)
        elif not ev:
            rec['status'], rec['reason'] = 'MIDDLE', 'unchanged, but the record shows no reader or checker given it'
        else:
            notes = [m for m in d['marks']]
            rec['status'] = 'FROZEN'
            rec['reason'] = 'unchanged since round 2 put it to the readers; ' + ev[0] + (
                '; its marks are notes only, the body unchanged' if notes else '')
        outd.append(rec)
    return {'state': state, 'current': (cur_key, vlabel[cur_key]), 'sentences': out, 'definitions': outd,
            'gone_definitions': sorted(set(gone)), 'inputs': inputs, 'versions': [(k, lab) for k, lab, _, _ in versions],
            'cores': [(k, lab) for k, lab, _, _ in cores], 'claims_file': claims_rel}


def def_key(d):
    m = re.match(r'D(\d+)\.(\d+|new\d+|XV)', d)
    if m:
        b = m.group(2)
        return (int(m.group(1)), int(b) if b.isdigit() else (100 if b == 'XV' else 50 + int(b[3:])), 0)
    m = re.match(r'E(\d+)', d)
    return (17, int(m.group(1)) if m else 0, 1)


def claim_key(c):
    m = re.match(r'FC(\d+)(?:\.new(\d+))?', c)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (999, 0)


# ------------------------------------------------------------------ the page
def short(t, n=130):
    t = re.sub(r'\s+', ' ', t.replace('\n', ' ')).strip().replace('|', '\\|')
    return t if len(t) <= n else t[:n - 1].rstrip() + '…'


def page(res):
    S, D = res['sentences'], res['definitions']
    fs = [x for x in S if x['status'] == 'FROZEN']
    fd = [x for x in D if x['status'] == 'FROZEN']
    ms = [x for x in S if x['status'] == 'MIDDLE']
    md = [x for x in D if x['status'] == 'MIDDLE']
    cur_key, cur_label = res['current']
    L = []
    L.append('# S108 Part A: the frozen set, the parts that are hard to vary')
    L.append('')
    L.append("*Claude's reading, not the owner's: the owner has not been asked to approve it (decision S52). Written by "
             "program, `tools/s108_frozen_set.py`, from the record, for Part A of decision S52; a Claude subagent "
             "(Opus 5.5) wrote the program and this page's frame, 28 September 2026. Nothing in the theory's text, its "
             "maths or any earlier record was changed. \"Model\" here means only a small structure the program builds, "
             "never a candidate (S43).*")
    L.append('')
    L.append('## 1. The criterion, as applied')
    L.append('')
    L.append("Decision S52 asks to freeze \"all the parts that are hard to vary\". Claude's working reading, recorded "
             "in S52: the sentences and definitions that readers tried to vary across the rounds and that came through "
             "unchanged while the parts around them kept changing (the owner's own approach of S31). Applied to every "
             "sentence of the current text (`%s`, the state after %s) and every definition and encoding of the current "
             "formal core, an item is **FROZEN** when both hold:" % (dict((k, rel) for k, _, rel, _ in
                                                                        VERSIONS + [R4['version']])[cur_key], cur_label))
    L.append('')
    L.append('- **(a) put to the readers or checkers at least once (challenged or tested).** For a sentence, any of: a '
             'proposal the S98 ledger places on it before the review rounds, none applied (S100\'s count); one of the 29 '
             'put to both readers in round 1; quoted beside its maths in one of round 2\'s 17 parts; quoted as the '
             'source of a formal claim the program tests; or named by a finding whose line holds no other sentence. '
             'For a definition or encoding: put to both readers in round 2 (every definition of round 2\'s formal core '
             'was, challenged or not), or named by a finding of a later round.')
    L.append('- **(b) no round or step changed it.** For a sentence: untouched in substance through the ten versions '
             'the ledger follows (S100\'s test, which leaves out the scrub\'s word swaps of S95), and its exact words '
             'still a sentence of its line in every text after the ledger\'s: %s. A sentence changed and later '
             'restored (L13\'s " and criticism") counts as changed. For a definition: its body, without the change '
             'marks and invention references, the same in every formal core after round 2\'s: %s. A mark with no '
             'change of the body (a note, "no change", an invention registered) is not a change.'
             % ('; '.join(lab for _, lab in res['versions'][1:]), '; '.join(lab for _, lab in res['cores'][1:])))
    L.append('- **Everything else is the MIDDLE.** A sentence whose line alone was named by a finding, on a line '
             'holding other sentences, goes to the middle: the record cannot tell whether that sentence was put.')
    L.append('- A sentence and the definitions that formalize it are separate items. A frozen sentence whose '
             'definition is in the middle constrains that definition: any variant of it must still be a reading of '
             'the frozen words. A frozen definition whose sentence changed stands as the maths the words now point to.')
    L.append('')
    L.append('## 2. Counts')
    L.append('')
    L.append('| | frozen | middle | all |')
    L.append('|---|---|---|---|')
    L.append('| sentences of the text | %d | %d | %d |' % (len(fs), len(ms), len(S)))
    L.append('| definitions and encodings of the formal core | %d | %d | %d |' % (len(fd), len(md), len(D)))
    L.append('| all items | %d | %d | %d |' % (len(fs) + len(fd), len(ms) + len(md), len(S) + len(D)))
    L.append('')
    L.append('By Part of the text (a definition counts in the Part of the lines it formalizes):')
    L.append('')
    L.append('| Part | sentences frozen | sentences middle | definitions frozen | definitions middle | middle items |')
    L.append('|---|---|---|---|---|---|')
    for pt in PARTS:
        a = sum(1 for x in fs if x['part'] == pt)
        b = sum(1 for x in ms if x['part'] == pt)
        c = sum(1 for x in fd if x['part'] == pt)
        d = sum(1 for x in md if x['part'] == pt)
        if a + b + c + d:
            L.append('| %s | %d | %d | %d | %d | %d |' % (pt, a, b, c, d, b + d))
    L.append('')
    why = Counter()
    for x in ms:
        r = x['reason']
        if r.startswith('changed: '):
            ks = [c.split(' (')[0] for c in r[len('changed: '):].split('; ')]
            why['changed: ' + ' and '.join(dict.fromkeys(ks))] += 1
        elif r.startswith('its words are new'):
            why[r] += 1
        elif 'only its line' in r:
            why['unchanged; only its line named by a finding, the line holding other sentences'] += 1
        else:
            why[r] += 1
    L.append('Why the middle sentences are in the middle:')
    L.append('')
    L.append('| reason | sentences |')
    L.append('|---|---|')
    for k, v in sorted(why.items(), key=lambda kv: -kv[1]):
        L.append('| %s | %d |' % (k, v))
    L.append('')
    whyd = Counter(x['reason'] for x in md)
    L.append('Why the middle definitions are in the middle:')
    L.append('')
    L.append('| reason | definitions |')
    L.append('|---|---|')
    for k, v in sorted(whyd.items(), key=lambda kv: -kv[1]):
        L.append('| %s | %d |' % (k, v))
    L.append('')
    L.append('## 3. The frozen sentences')
    L.append('')
    L.append('Unit ids are the S98 ledger\'s (line and sentence of the latest text; every text since keeps its lines). '
             '"Formal" gives the definitions that quote the sentence (or, marked *line*, that quote its line) and the '
             'claims whose source it is.')
    L.append('')
    L.append('| id | line | Part | the sentence | formal | why frozen |')
    L.append('|---|---|---|---|---|---|')
    for x in fs:
        form = ', '.join(x['defs']) + (' (*line*)' if x.get('defs_by') == 'line' else '')
        if x['claims']:
            form += ('; ' if form else '') + ', '.join(x['claims'][:8]) + (' …' if len(x['claims']) > 8 else '')
        L.append('| %s | L%d%s | %s | %s | %s | %s |' % (x['id'], x['line'], ('–L%d' % x['line_end']) if x['line_end'] != x['line'] else '',
                                                       x['part'], short(x['text']), form or '—', short(x['reason'], 170)))
    L.append('')
    L.append('## 4. The frozen definitions and encodings')
    L.append('')
    L.append('| id | section of the core | lines it formalizes | Part | why frozen |')
    L.append('|---|---|---|---|---|')
    for x in fd:
        L.append('| %s | %s | %s | %s | %s |' % (x['id'], short(x['section'], 40), ', '.join('L%d' % n for n in x['lines']) or '—',
                                              x['part'], short(x['reason'], 170)))
    L.append('')
    L.append('## 5. The middle definitions and encodings')
    L.append('')
    L.append('| id | lines | Part | why middle |')
    L.append('|---|---|---|---|')
    for x in md:
        L.append('| %s | %s | %s | %s |' % (x['id'], ', '.join('L%d' % n for n in x['lines']) or '—', x['part'], short(x['reason'], 170)))
    L.append('')
    L.append('The %d middle sentences, each with its reason, are in the `.json` beside this page (`sentences`, '
             '`status` "MIDDLE").' % len(ms))
    L.append('')
    L.append('## 6. The strong candidates of S100 and S101, now')
    L.append('')
    L.append('| unit | S100 list | now | reason |')
    L.append('|---|---|---|---|')
    have = {x['unit']: x for x in S if x.get('unit')}
    s100 = {r['unit_id']: r for r in csv.DictReader(open(p(S100_CSV), encoding='utf-8'))}
    for uid, r in s100.items():
        if r['strong_candidate_list']:
            x = have.get(uid)
            if x:
                L.append('| %s | %s | %s | %s |' % (uid, r['strong_candidate_list'], x['status'], short(x['reason'], 150)))
            else:
                L.append('| %s | %s | MIDDLE (its words are gone) | changed by a later round or step; the sentence at '
                         'L%s now is in the middle |' % (uid, r['strong_candidate_list'], r['line']))
    L.append('')
    L.append('## 7. What the program cannot tell, and choices it made')
    L.append('')
    for s in UNSURE:
        L.append('- ' + s)
    L.append('')
    L.append('## 8. Inputs')
    L.append('')
    L.append('| file | md5 |')
    L.append('|---|---|')
    for rel, h in res['inputs'].items():
        L.append('| `%s` | %s |' % (rel, h))
    L.append('')
    return '\n'.join(L) + '\n'


UNSURE = [
    "Before the review rounds, \"challenged\" and \"changed\" are S100's counts from the S98 ledger: a record placed "
    "on a whole paragraph counts on each of its sentences, so a sentence may count as challenged by a proposal aimed "
    "at its neighbour. The scrub's word swaps (S95) are not counted as changes, as S100 did not count them; the "
    "changes of S99 (references to provenance, history and versions removed) are counted.",
    "A sentence is followed by its exact words on its line: a change of one character makes it changed. A sentence "
    "restored after a change counts as changed.",
    "Quotations are matched to sentences by text (a fragment inside the sentence, or a common stretch of at least 30 "
    "characters, or four fifths of the shorter); a loose quotation could reach a neighbour.",
    "Findings of rounds 2 to 4 name lines, not sentences; they count for (a) only on a line holding one sentence.",
    "A definition's history is read from its body in each formal core; the core after round 2 was written by round 2's "
    "reading, its second check and the owner's answers step, and which of them changed a definition is read from its "
    "marks.",
    "Silence is not agreement: a frozen item held under the attempts made; nothing shows it holds beyond them (S28).",
    "What hard to vary covers in general stays parked (S33, S34); this set is a working reading for Part A only.",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', choices=['s106', 'r4'], required=True)
    ap.add_argument('--out-dir', help='with --state s106: where to write (never the repository\'s result names)')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    res = analyse(a.state)
    js = json.dumps({'about': {'what': "S108 Part A: the frozen set (Claude's reading of decision S52, not approved "
                                       "by the owner)", 'state': res['current'][1], 'criterion': '(a) put to the '
                               'readers or checkers at least once; (b) no round or step changed it',
                               'counts': {'sentences': Counter(x['status'] for x in res['sentences']),
                                          'definitions': Counter(x['status'] for x in res['definitions'])},
                               'gone_definitions': res['gone_definitions'], 'inputs': res['inputs'],
                               'program': 'tools/s108_frozen_set.py'},
                     'sentences': res['sentences'], 'definitions': res['definitions']},
                    ensure_ascii=False, indent=1) + '\n'
    md = page(res)
    if a.state == 's106':
        need(a.out_dir, '--out-dir is needed with --state s106')
        os.makedirs(a.out_dir, exist_ok=True)
        for name, text in (('frozen set, after S106.json', js), ('frozen set, after S106.md', md)):
            with open(os.path.join(a.out_dir, name), 'w', encoding='utf-8') as f:
                f.write(text)
    else:
        for rel, text in ((OUT_JSON, js), (OUT_MD, md)):
            if a.check:
                need(os.path.exists(p(rel)) and read(rel) == text, '%s differs from the build' % rel)
                continue
            if os.path.exists(p(rel)):
                need(read(rel) == text, '%s exists with other content; nothing overwritten' % rel)
                print('same    ' + rel)
            else:
                with open(p(rel), 'x', encoding='utf-8') as f:
                    f.write(text)
                print('wrote   ' + rel)
    S, D = res['sentences'], res['definitions']
    print('sentences: %s; definitions: %s' % (dict(Counter(x['status'] for x in S)), dict(Counter(x['status'] for x in D))))


if __name__ == '__main__':
    main()
