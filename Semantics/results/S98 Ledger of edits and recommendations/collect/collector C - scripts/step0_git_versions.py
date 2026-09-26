"""Step 0: the five committed states of the change list, cut from git into the scratchpad (read only).
12e73da change list draft 1 (48 changes, three items held) -> file 13 draft 1 (as sent)
587eebf change list draft 2 (the held items drafted, 55 changes) -> file 13 draft 2 (as sent)
99e9cd0 change list draft 3 (the S90 rulings applied) -> file 13 draft 3
3f7c3ab change list draft 4 (group H) -> file 13 draft 4
8816fcf change list draft 5 (the S93 rulings applied) -> file 13 draft 5"""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib_c import SP, CL_VERSIONS, ROOT
os.makedirs(SP + '/cl', exist_ok=True)
for c, *_ in CL_VERSIONS:
    out = subprocess.run(['git', '-C', ROOT, 'show', '%s:Semantics/tests/Revision 2 - change list, draft of 23 September.md' % c],
                         capture_output=True, check=True).stdout
    open(SP + '/cl/%s.md' % c, 'wb').write(out)
    print(c, len(out))
