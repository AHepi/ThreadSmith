#!/usr/bin/env python3
"""Cross-check against the checkers' own in-memory builds: W35.5 alone (X04 ruling: theory md5
5f7888dba8be366f5caed39672bdd096) and the X17 fix alone (X17 ruling: theory md5 f7fb94d3ad26c089c6abbf60b83baf67),
each applied to the draft-4 list (HEAD)."""
import hashlib, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s93_lib import CHANGE_LIST_REL, entry_span, fence_after, git_show, one, ruling, TOOL, REPO
head = git_show(CHANGE_LIST_REL)
done = (HERE / 'cl_entries.md').read_text(encoding='utf-8')
# W35.5 alone
s, e = entry_span(done, 'W35.5'); w355 = done[s:e]
s, e = entry_span(head, 'W35.4'); only_w355 = head[:e] + w355 + head[e:]
# X17 alone: W7.5 section of the final list in place of the draft-4 one
s, e = entry_span(done, 'W7.5'); w75 = done[s:e]
s2, e2 = entry_span(head, 'W7.5'); only_x17 = head[:s2] + w75 + head[e2:]
for name, text, want in (('W35.5 alone', only_w355, '5f7888dba8be366f5caed39672bdd096'),
                         ('X17 alone', only_x17, 'f7fb94d3ad26c089c6abbf60b83baf67')):
    cl = HERE / ('single_%s.md' % name.split()[0]); cl.write_text(text, encoding='utf-8')
    th = HERE / ('single_%s_theory.md' % name.split()[0])
    run = subprocess.run([sys.executable, str(TOOL), str(HERE / 'single_full.md'), '--change-list', str(cl),
                          '--theory-output', str(th)], capture_output=True, text=True, cwd=str(REPO),
                         env={'PYTHONDONTWRITEBYTECODE': '1', 'PATH': '/usr/bin:/bin'})
    if run.returncode: print(run.stdout); sys.exit('refused')
    got = hashlib.md5(th.read_bytes()).hexdigest()
    print(name, got, 'matches the checker' if got == want else 'DIFFERS from the checker (%s)' % want)
