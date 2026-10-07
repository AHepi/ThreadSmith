"""Step 1: the sentence index of the latest text."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import *

ix = Indexed('latest')
out = GROUP + '/sentence index of the latest text.jsonl'
with open(out, 'w', encoding='utf-8') as f:
    for u in ix.units:
        rec = dict(id=u["id"], line=u["line"], line_end=u["line_end"], n=u["n"], kind=u['kind'],
                   part=u['part'], heading=u['heading'], label=u['label'],
                   text=u['text'], start=u['start'], end=u['end'])
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
from collections import Counter
print(len(ix.units), Counter(u['kind'] for u in ix.units))
print('source md5', md5(VPATH['latest']))
# check: every unit text is verbatim in its line
def span(u):
    seg = '\n'.join(ix.lines[u['line'] - 1:u['line_end']])
    return seg[u['start']:len(seg) - (len(ix.lines[u['line_end'] - 1]) - u['end'])]
bad = [u['id'] for u in ix.units if span(u) != u['text']]
print('offset misses', len(bad), bad[:10])
