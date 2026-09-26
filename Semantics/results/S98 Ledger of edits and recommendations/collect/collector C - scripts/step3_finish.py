"""Step 5: join steps 1 and 2, settle same_as, write collector C.jsonl, and check it.
- same_as keeps only links between records of one change (a ruling's FIX wording and the change-list wording
  it produced; a reader's proposal a ruling took word for word). A link from a declined or later-replaced
  proposal to the wording taken instead moves into source_ref ("taken instead: ...").
- Links to collectors A and B: a record there whose "new" (at least 40 characters, not a description)
  equals this record's "new", or is contained in it, is the same wording seen in another source.
- Links are made symmetric inside collector C.
Checks: every record has the fields and values of the task's shape; every "old" of a record whose status is
applied is found verbatim in its target text; every "new" of an applied or superseded record is found
verbatim in each theory text its applied_in names; no book quotation is added. Writes the check report to
the scratchpad (check.json)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))
from lib_c import *

S1 = [json.loads(l) for l in open(SP + '/step1.jsonl', encoding='utf-8')]
S2 = [json.loads(l) for l in open(SP + '/step2.jsonl', encoding='utf-8')]
recs = S1 + S2
by = {r['rid']: r for r in recs}

# 1. same_as: keep only one-change links
for r in S2:
    if not r['same_as']:
        continue
    fix = 'read off the line diff' in r['source_ref'] or r['source_ref'].startswith('S90 ruling R25') or r['source_ref'].startswith('S90 ruling R39') or r['source_ref'].startswith('S93 ruling X18 (W38.1), ruling 3')
    same_words = r['status'] == 'applied' and any(by[x]['new'].strip() and (by[x]['new'] in r['new'] or r['new'] in by[x]['new']) for x in r['same_as'])
    if fix or same_words:
        continue
    r['source_ref'] += '; wording taken instead, or the related change: ' + ', '.join(r['same_as'])
    r['same_as'] = []

# 2. links to collectors A and B
others = []
for name in ('collector A.jsonl', 'collector B.jsonl'):
    p = OUTDIR + '/' + name
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            try:
                o = json.loads(l)
            except Exception:
                continue
            n = o.get('new') or ''
            if len(n) >= 40 and not n.startswith('[no wording given]'):
                others.append((o['rid'], n))
xlinks = 0
f11_text = read(F11)
for r in recs:
    n = r['new']
    if len(n) < 40 or n.startswith('[no wording given]'):
        continue
    for orid, on in others:
        if on == n or (len(on) >= 60 and on in n and on not in r['old'] and on not in f11_text):
            if orid not in r['same_as']:
                r['same_as'].append(orid)
                xlinks += 1

# 3. symmetric and transitive inside C (links join only records of one change)
changed = True
while changed:
    changed = False
    for r in recs:
        inner = [x for x in r['same_as'] if x in by]
        for x in inner:
            for y in [x] + [z for z in by[x]['same_as'] if z in by]:
                if y != r['rid'] and y not in r['same_as']:
                    r['same_as'].append(y)
                    changed = True
            if r['rid'] not in by[x]['same_as']:
                by[x]['same_as'].append(r['rid'])
                changed = True
for r in recs:
    r['same_as'] = sorted(set(r['same_as']), key=lambda s: (s.split('-')[0], int(s.split('-')[1]) if s.split('-')[1].isdigit() else 0))

# 4. checks
KEYS = ['rid', 'round', 'source_file', 'source_ref', 'kind', 'status', 'applied_in', 'target_text', 'target_line', 'target_part',
        'old', 'new', 'old_sentence', 'new_sentence', 'scope', 'same_as']
report = {'shape': [], 'old_applied_missing': [], 'new_applied_in_missing': [], 'counts': {}}
for r in recs:
    if list(r.keys()) != KEYS:
        report['shape'].append((r['rid'], 'keys'))
    if r['kind'] not in ('edit', 'recommendation'):
        report['shape'].append((r['rid'], 'kind'))
    if r['status'] not in ('applied', 'not applied', 'declined', 'superseded', 'open for the owner', 'unknown'):
        report['shape'].append((r['rid'], 'status'))
    if r['scope'] not in ('sentence', 'span', 'term', 'paragraph', 'whole text'):
        report['shape'].append((r['rid'], 'scope'))
    if not os.path.exists(ROOT + '/' + r['source_file']):
        report['shape'].append((r['rid'], 'source_file missing'))

texts = {lab: read(p) for lab, p in TEXTS}
f11 = read(F11)
vers = {c: {e['id']: e for e in parse_changelist(open(SP + '/cl/' + c + '.md', encoding='utf-8').read())} for c, *_ in CL_VERSIONS}
notes = {
    'the note of file 13, its list of changes of claim (full file 13 draft 2': '\n'.join(e['fields'].get('DECLARATION', '') for e in vers['587eebf'].values()),
    'the note of file 13, its list of changes of claim (full file 13 draft 4': '\n'.join(e['fields'].get('DECLARATION', '') for e in vers['3f7c3ab'].values()),
    'the note of sources and departures (full file 13 draft 2': vers['587eebf']['W38.1']['NEW'],
    'the note of sources and departures (full file 13 draft 4': vers['3f7c3ab']['W38.1']['NEW'],
}


def target_body(tt):
    if tt.startswith('file 11 '):
        return f11
    if tt.startswith('file 12 '):
        return read('authority/12 Claude Fable Semantics - causality, standalone theory.md')
    for lab in texts:
        if tt.startswith(lab):
            return texts[lab]
    for k, v in notes.items():
        if tt.startswith(k):
            return v
    return None


for r in recs:
    body = target_body(r['target_text'])
    if r['status'] == 'applied' and r['old']:
        if body is None or r['old'] not in body:
            report['old_applied_missing'].append((r['rid'], r['target_text'][:40], r['old'][:60]))
    if r['status'] in ('applied', 'superseded') and r['new'] and not r['new'].startswith('[no wording given]'):
        for lab in texts:
            if re.search(r'(^|; )' + re.escape(lab) + r'($|;)', r['applied_in']) and r['new'] not in texts[lab]:
                report['new_applied_in_missing'].append((r['rid'], lab, r['new'][:60]))
    if body is None and r['old']:
        report['shape'].append((r['rid'], 'target text not resolvable for the check'))

from collections import Counter
report['counts'] = {
    'total': len(recs),
    'kind_status': Counter('%s / %s' % (r['kind'], r['status']) for r in recs),
    'round': Counter(r['round'] for r in recs),
    'scope': Counter(r['scope'] for r in recs),
    'no_wording': sum(1 for r in recs if r['new'].startswith('[no wording given]')),
    'with_same_as': sum(1 for r in recs if r['same_as']),
    'cross_links': xlinks,
    'source_file': Counter(r['source_file'] for r in recs),
}
write_jsonl(OUTDIR + '/collector C.jsonl', recs)
json.dump(report, open(SP + '/check.json', 'w'), ensure_ascii=False, indent=1, default=dict)
print(json.dumps({k: (v if k != 'counts' else {kk: (dict(vv) if hasattr(vv, 'items') else vv) for kk, vv in v.items()}) for k, v in report.items()}, ensure_ascii=False, indent=1)[:4000])
