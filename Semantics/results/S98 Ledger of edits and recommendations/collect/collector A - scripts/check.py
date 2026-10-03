import json, sys, collections
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

OUT = os.environ.get('COLLECTOR_A_OUT', ROOT + '/results/S98 Ledger of edits and recommendations/collect/collector A.jsonl')
R = [json.loads(l) for l in open(OUT, encoding='utf-8')]
f10 = read(F10)
f11 = read(F11)
KEYS = ['rid', 'round', 'source_file', 'source_ref', 'kind', 'status', 'applied_in', 'target_text', 'target_line',
        'target_part', 'old', 'new', 'old_sentence', 'new_sentence', 'scope', 'same_as']
KIND = {'edit', 'recommendation'}
STATUS = {'applied', 'not applied', 'declined', 'superseded', 'open for the owner', 'unknown'}
SCOPE = {'sentence', 'span', 'term', 'paragraph', 'whole text'}
problems = []
rids = [r['rid'] for r in R]
if len(rids) != len(set(rids)):
    problems.append('duplicate rids')
rs = set(rids)
for r in R:
    if list(r.keys()) != KEYS:
        problems.append('%s keys %s' % (r['rid'], list(r.keys())))
    if r['kind'] not in KIND or r['status'] not in STATUS or r['scope'] not in SCOPE:
        problems.append('%s bad enum' % r['rid'])
    for t in r['same_as']:
        if t not in rs:
            problems.append('%s same_as %s missing' % (r['rid'], t))

res = collections.OrderedDict()
# 1. every old recorded against file 10 is found verbatim in file 10
old_rows = [r for r in R if r['old'] and r['target_text'].startswith('file 10')]
res['old found verbatim in file 10 (all records with an old)'] = (sum(r['old'] in f10 for r in old_rows), len(old_rows),
                                                                   [r['rid'] for r in old_rows if r['old'] not in f10])
app = [r for r in old_rows if r['status'] == 'applied']
res['old found verbatim in file 10 (records with status applied)'] = (sum(r['old'] in f10 for r in app), len(app),
                                                                       [r['rid'] for r in app if r['old'] not in f10])
# 1b. target_line points at a line of file 10 that holds the old
tl = [r for r in old_rows if r['target_line']]
lines10 = f10.split('\n')
res['old found on its target_line of file 10'] = (sum(r['old'] in lines10[r['target_line'] - 1] for r in tl), len(tl),
                                                  [r['rid'] for r in tl if r['old'] not in lines10[r['target_line'] - 1]])
# 2. old inside old_sentence, new inside new_sentence
os_ = [r for r in R if r['old'] and r['old_sentence']]
res['old inside old_sentence'] = (sum(r['old'] in r['old_sentence'] for r in os_), len(os_), [r['rid'] for r in os_ if r['old'] not in r['old_sentence']])
ns_ = [r for r in R if r['new'] and r['new_sentence'] and not r['new'].startswith('[no wording given]') and r['scope'] != 'span' or (r['scope'] == 'span' and r['new_sentence'] and not r['round'].startswith('Stage B'))]
ns_ = [r for r in ns_ if r['new'] and r['new_sentence']]
res['new inside new_sentence'] = (sum(r['new'] in r['new_sentence'] for r in ns_), len(ns_), [r['rid'] for r in ns_ if r['new'] not in r['new_sentence']])
sb = [r for r in R if r['round'].startswith('Stage B') and r['new_sentence']]
import re as _re
res['Stage B: every underlined phrase found in its R2 sentence(s) (tags stripped, quotes normalized)'] = (
    sum(all(norm(p) in norm(r['new_sentence']) or norm(p).lower() in norm(r['new_sentence']).lower() for p in _re.findall(r'<u>(.*?)</u>', r['new'])) for r in sb), len(sb),
    [r['rid'] for r in sb if not all(norm(p).lower() in norm(r['new_sentence']).lower() for p in _re.findall(r'<u>(.*?)</u>', r['new']))])
# 3. new copied byte for byte from its source file
def in_source(r):
    src = read(r['source_file'])
    n = r['new']
    if n in src:
        return True
    # a block quotation printed with '> ' prefixes, or a table cell with <br>
    if n.replace('\n', '\n> ') in src:
        return True
    # a multi-line block quotation: every non-blank line printed as '> line'
    ls = [x for x in n.split('\n') if x.strip()]
    if len(ls) > 1 and all(('> ' + x) in src for x in ls):
        return True
    return False
nw = [r for r in R if r['new'] and not r['new'].startswith('[no wording given]')]
res['new found verbatim in its source_file'] = (sum(in_source(r) for r in nw), len(nw), [r['rid'] for r in nw if not in_source(r)])
# 4. applied in file 11 in other wording: is the new also verbatim in file 11?
a11 = [r for r in R if r['status'] == 'applied' and 'file 11' in r['applied_in'] and not r['new'].startswith('[no wording given]')]
res['applied records whose new is verbatim in file 11 (expected none: other wording)'] = (sum(r['new'] in f11 for r in a11), len(a11), [r['rid'] for r in a11 if r['new'] in f11])
# 5. declined file 20 edits: is the old still verbatim in file 11?
d = [r for r in R if r['status'] == 'declined' and r['old']]
res['declined file 20 edits whose old is still verbatim in file 11'] = (sum(r['old'] in f11 for r in d), len(d), [])

for k, v in res.items():
    print('%-95s %s/%s  misses: %s' % (k, v[0], v[1], v[2]))
print('schema problems:', problems or 'none')
print('by kind:', dict(collections.Counter(r['kind'] for r in R)))
print('by status:', dict(collections.Counter(r['status'] for r in R)))
print('by kind and status:', dict(collections.Counter((r['kind'], r['status']) for r in R)))
print('by round:', dict(collections.Counter(r['round'] for r in R)))
print('by scope:', dict(collections.Counter(r['scope'] for r in R)))
json.dump({k: v for k, v in res.items()}, open(os.environ.get('COLLECTOR_A_CHECK', os.devnull), 'w'), ensure_ascii=False, indent=1)
