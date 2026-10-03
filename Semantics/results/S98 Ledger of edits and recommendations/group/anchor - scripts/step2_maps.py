"""Step 2: line maps between the versions, composed to the latest text."""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import *

L = {k: lines_of(k) for k in CHAIN}
out = {'about': 'Line maps between the theory texts. Each map sends a line of the earlier text to a line of the later '
                 'text or to null. kind: equal (same line), changed (paired by similarity inside a changed block), moved '
                 '(paired by similarity across the text), removed (no partner). Lines are 1-based. Blank lines and rules '
                 'are mapped too.',
       'versions': {k: {'label': VLABEL[k], 'path': VPATH[k], 'md5': md5(VPATH[k]), 'lines': len(L[k]) - (1 if L[k][-1] == '' else 0)}
                    for k in CHAIN},
       'pairs': {}, 'to_latest': {}, 'f10_f11_sentences': [], 'change_list_file11_lines': []}

LINE_FOR_LINE = {('d5', 'scrubbed'), ('scrubbed', 'repaired'), ('repaired', 'latest')}
maps = {}
for a, b in zip(CHAIN, CHAIN[1:]):
    if (a, b) in LINE_FOR_LINE:
        assert len(L[a]) == len(L[b]), (a, b)
        m = {i + 1: (i + 1, 'equal' if L[a][i] == L[b][i] else 'changed', 1.0 if L[a][i] == L[b][i] else
                     round(difflib.SequenceMatcher(None, L[a][i], L[b][i], autojunk=False).ratio(), 3))
             for i in range(len(L[a]))}
        method = 'line for line (the texts keep the same lines)'
    else:
        m = line_map(L[a], L[b])
        method = 'difflib at line level; changed blocks paired by similarity (ratio >= 0.3), then unpaired lines paired across the text (ratio >= 0.6) as moved'
    maps[(a, b)] = m
    inserted = sorted(set(range(1, len(L[b]) + 1)) - {v[0] for v in m.values() if v[0]})
    from collections import Counter
    out['pairs']['%s->%s' % (a, b)] = {
        'method': method,
        'counts': dict(Counter(v[1] for v in m.values())),
        'inserted_lines_in_later': inserted,
        'map': {str(k): [v[0], v[1], v[2]] for k, v in sorted(m.items())}}

# sentence-level map, file 10 -> file 11
i10, i11 = Indexed('f10'), Indexed('f11')
s11 = [u for u in i11.units]
n11 = {}
for j, u in enumerate(s11):
    n11.setdefault(norm(u['text']), []).append(j)
m1011 = maps[('f10', 'f11')]
for u in i10.units:
    t = norm(u['text'])
    hit = None
    if t in n11:
        hit = (s11[n11[t][0]], 1.0, 'same')
    else:
        tgt = m1011.get(u['line'], (None,))[0]
        cands = []
        if tgt:
            for ln in range(tgt - 2, tgt + 3):
                cands += [s11[j] for j in i11.by_line.get(ln, [])]
        best, bu = 0.0, None
        for c in cands:
            r = ratio(u['text'], c['text'])
            if r > best:
                best, bu = r, c
        if best < 0.6:
            # search the whole of file 11
            for c in s11:
                if difflib.SequenceMatcher(None, loose(u['text']), loose(c['text'])).real_quick_ratio() < 0.6:
                    continue
                r = ratio(u['text'], c['text'])
                if r > best:
                    best, bu = r, c
        if bu is not None and best >= 0.6:
            hit = (bu, round(best, 3), 'changed')
    out['f10_f11_sentences'].append({'f10': u['id'], 'f11': hit[0]['id'] if hit else None,
                                     'kind': hit[2] if hit else 'removed', 'ratio': hit[1] if hit else 0.0})


# lines of file 10 that the line map loses but whose sentences the sentence map finds in file 11
sid11 = {u['id']: u for u in i11.units}
repaired_lines = []
for u10line in sorted({u['line'] for u in i10.units}):
    v = maps[('f10', 'f11')].get(u10line)
    if v and v[0] is None:
        hits = [x for x in out['f10_f11_sentences'] if x['f10'].startswith('L%d.' % u10line) and x['f11']]
        if hits:
            best = max(hits, key=lambda x: x['ratio'])
            ln = sid11[best['f11']]['line']
            maps[('f10', 'f11')][u10line] = (ln, 'moved (sentence level)', best['ratio'])
            repaired_lines.append([u10line, ln, best['ratio']])
out['pairs']['f10->f11']['map'] = {str(k): [v[0], v[1], v[2]] for k, v in sorted(maps[('f10', 'f11')].items())}
out['pairs']['f10->f11']['counts'] = dict(Counter(v[1] for v in maps[('f10', 'f11')].values()))
out['pairs']['f10->f11']['lines_placed_by_the_sentence_map'] = repaired_lines
out['pairs']['f10->f11']['inserted_lines_in_later'] = sorted(set(range(1, len(L['f11']) + 1)) - {v[0] for v in maps[('f10', 'f11')].values() if v[0]})
out['pairs']['f10->f11']['method'] += '; lines still unpaired then placed by the sentence-level map (the file-11 line of their most similar sentence)'

# composed map to the latest text
for k in CHAIN:
    comp = {}
    i = CHAIN.index(k)
    for ln in range(1, len(L[k]) + 1):
        cur, lost, kinds = ln, None, []
        for a, b in zip(CHAIN[i:], CHAIN[i + 1:]):
            v = maps[(a, b)][cur]
            kinds.append(v[1])
            if v[0] is None:
                lost = a
                cur = None
                break
            cur = v[0]
        comp[str(ln)] = {'latest': cur, 'last_present_in': lost if lost else 'latest',
                         'unchanged': all(x == 'equal' for x in kinds)}
    out['to_latest'][k] = comp

# the change list's FILE-11 LINE fields against the difflib maps
cl = read('tests/Revision 2 - change list, draft of 23 September.md').split('\n')
entries = []
cur = None
i = 0
while i < len(cl):
    l = cl[i]
    mo = re.match(r'### (W[0-9]+[a-z]?(?:\([a-z]\))?\.[0-9]+) — (.*)', l)
    if mo:
        cur = {'entry': mo.group(1), 'file11_line': None, 'status': None, 'new_first': None}
        entries.append(cur)
    elif cur is not None:
        mo = re.match(r'- \*\*FILE-11 LINE:\*\* (.*)', l)
        if mo:
            cur['file11_line'] = mo.group(1).strip()
        mo = re.match(r'- \*\*STATUS:\*\* (.*)', l)
        if mo:
            cur['status'] = mo.group(1).strip()
        if l.startswith('- **NEW:**') and cur['new_first'] is None:
            j = i + 1
            if cl[j].startswith('````'):
                j += 1
                block = []
                while not cl[j].startswith('````'):
                    block.append(cl[j]); j += 1
                good = [b for b in block if b.strip() and not b.startswith('<!--') and len(b.strip()) > 30]
                cur['new_first'] = good[0] if good else ''
    i += 1
for e in entries:
    rec = {'entry': e['entry'], 'status': e['status'], 'file11_line_field': e['file11_line']}
    mo = re.match(r'(\d+)', e['file11_line'] or '')
    f11 = int(mo.group(1)) if mo else None
    rec['file11_line'] = f11
    # where the composed difflib map sends that file-11 line in each draft
    guess = {}
    if f11:
        cur = f11
        for a, b in zip(CHAIN[1:6], CHAIN[2:7]):
            cur = maps[(a, b)][cur][0] if cur else None
            guess[b] = cur
    for d in ('d1', 'd2', 'd3', 'd4', 'd5'):
        found = None
        if e['new_first']:
            probe = e['new_first']
            occ = [k for k, l in enumerate(L[d], 1) if probe in l]
            if not occ:
                occ = [k for k, l in enumerate(L[d], 1) if probe[:80] in l]
            if occ:
                g = guess.get(d) or f11 or 0
                found = min(occ, key=lambda k: abs(k - g))
        rec['new_line_in_' + d] = found
    if f11:
        cur = f11
        for a, b in zip(CHAIN[1:6], CHAIN[2:7]):
            v = maps[(a, b)][cur]
            cur = v[0]
            if cur is None:
                break
        rec['difflib_file11_to_d5'] = cur
        rec['agree'] = (cur == rec['new_line_in_d5']) if rec['new_line_in_d5'] and cur else None
    out['change_list_file11_lines'].append(rec)

with open(GROUP + '/line maps.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=0)
for k, v in out['pairs'].items():
    print(k, v['counts'], 'inserted', len(v['inserted_lines_in_later']))
from collections import Counter
print('f10->f11 sentences', Counter(x['kind'] for x in out['f10_f11_sentences']))
print('change list entries', len(entries), Counter(str(r.get('agree')) for r in out['change_list_file11_lines']))
for r in out['change_list_file11_lines']:
    if r.get('agree') is False:
        print('  disagree', r)
for k in CHAIN:
    c = Counter(v['last_present_in'] for v in out['to_latest'][k].values())
    print('to latest', k, dict(c))
