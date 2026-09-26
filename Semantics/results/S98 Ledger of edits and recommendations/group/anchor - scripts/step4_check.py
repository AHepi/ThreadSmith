"""Step 4a: checks on the anchored ledger, by program."""
import json, sys, os, re
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import *

orig = []
for c in 'ABCDEF':  # F: the finishing agent's records (S98 finishing fixes)
    orig += [json.loads(l) for l in open(COLLECT + '/collector %s.jsonl' % c, encoding='utf-8')]
anch = [json.loads(l) for l in open(GROUP + '/anchored.jsonl', encoding='utf-8')]
idx = {json.loads(l)['id']: json.loads(l) for l in open(GROUP + '/sentence index of the latest text.jsonl', encoding='utf-8')}
latest = read(VPATH['latest'])
latest_n = re.sub(r'\s+', ' ', norm(latest))
faults = Counter()
notes = []

# 1. the collectors' fields are kept byte for byte, in order
if len(orig) != len(anch):
    faults['record count'] += 1
for o, a in zip(orig, anch):
    for k, v in o.items():
        if a.get(k) != v:
            faults['field changed'] += 1
            notes.append('field %s changed in %s' % (k, o['rid']))
# 2. anchors exist; statuses agree with anchors
ALLOWED = {'anchored', 'removed', 'never applied', 'not locatable'}
for a in anch:
    if a['latest_status'] not in ALLOWED:
        faults['status word'] += 1
    for x in a['latest_sentences']:
        if x not in idx:
            faults['unknown sentence id'] += 1
    if (a['latest_status'] == 'anchored') != bool(a['latest_sentences']):
        faults['status and anchors disagree'] += 1
    if a['latest_status'] != 'anchored' and not a.get('latest_reason'):
        faults['no reason for an empty anchor'] += 1
    if a['latest_sentences'] and a['latest_part'] != idx[a['latest_sentences'][0]]['part']:
        faults['part disagrees with first sentence'] += 1
# 3. where the new wording is said to be in the latest text, it is there
yes = 0
for a in anch:
    if a['new_in_latest'] == 'yes':
        yes += 1
        cand = [s for s in (a['new_sentence'], a['new']) if s and not s.startswith('[no wording given]')]
        if not any(re.sub(r'\s+', ' ', norm(s)).strip() in latest_n for s in cand):
            faults['new said present, not found'] += 1
            notes.append('new not found: ' + a['rid'])
        # and the anchored sentences hold it (or part of it, where it spans sentences)
        texts = ' '.join(idx[x]['text'] for x in a['latest_sentences'])
        tn = re.sub(r'\s+', ' ', norm(texts))
        ok = any(re.sub(r'\s+', ' ', norm(s)).strip() in tn or tn in re.sub(r'\s+', ' ', norm(s)) for s in cand)
        if not ok:
            faults['anchored sentences do not hold the new wording'] += 1
            notes.append('anchor text: ' + a['rid'])
# 4. change groups: every member names the same members
groups = {}
for a in anch:
    groups.setdefault(a['change_id'], set()).add(a['rid'])
for a in anch:
    if set(a['change_members']) != groups[a['change_id']]:
        faults['change members disagree'] += 1
# 5. the words of decision S23 in this step's own prose (method, reason, note fields and the summary)
S23 = re.compile(r'\b(fits|supports?|supported|verif\w*|corroborat\w*|proves?|proved|disproves?|disproved|belie\w*|'
                 r'better than|worse than|true|established|authority|foundation\w*|derived|justif\w*|rank\w*|best|score\w*|top)\b', re.I)
own = []
for a in anch:
    for k in ('anchor_method', 'latest_reason'):
        if a.get(k):
            own.append((a['rid'] + ' ' + k, a[k]))
    if a.get('latest_nearest'):
        own.append((a['rid'] + ' latest_nearest', a['latest_nearest']['note']))
summ = GROUP + '/anchoring summary.md'
if os.path.exists(summ):
    for i, l in enumerate(open(summ, encoding='utf-8'), 1):
        # quoted material (backticks, quotation marks) is data, not prose
        l2 = re.sub(r'`[^`]*`', '', l)
        l2 = re.sub(r'"[^"]*"', '', l2)
        own.append(('summary line %d' % i, l2))
hits = [(w, m.group(0)) for w, t in own for m in [S23.search(t)] if m]
faults['S23 words in own prose'] += len(hits)
print('records', len(anch), 'new_in_latest yes', yes)
print('faults', dict((k, v) for k, v in faults.items() if v) or 'none')
for n in notes[:20]:
    print('  ', n)
for h in hits[:20]:
    print('  S23:', h)
