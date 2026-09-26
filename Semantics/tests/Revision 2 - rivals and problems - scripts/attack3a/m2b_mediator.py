"""03a: the owner's example with a change that sets the mediating state on its own admitted (outside the
Greek contract). 'Demeter grieves' translates it as setting her grief; 'Persephone is underground' (as the
cause, with no grief) has nothing it could set, so its transport leaves the edit out."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from engine import Cand, key, conflict, fits
from seasons import D, PAIRS, GREEK, myth3, myth2, tilt
def confB(c1, c2, x, space='functional'):
    if c1.ans(x) != c2.ans(x):
        return True
    c, a, b, n = conflict(c1, c2, x, D, space)
    return c and a and b
q = 'p_greek'
d = myth3('dem', q); u = myth2('und', q)
# dem with a transport that carries 'set the warmth received' to 'set her grief'
dem = Cand('dem+', d.org, d.q, lambda x: dict({'half': x['half']}, **({'grief': x['ins']} if 'ins' in x else {})),
           d.pi, d.anchors, d.gamma, q)
MED = [dict(x, ins=i) for x in PAIRS for i in (1, 0, -1)]
ADM = PAIRS + MED
EG = {key(x): ('ans', D.ans(x)) for x in GREEK}
print('dem+ Account on Greek C:', dem.account(GREEK, GREEK[0], D), '| und:', u.account(GREEK, GREEK[0], D))
print('fits Greek-era answers: dem+', fits(dem, EG, D), 'und', fits(u, EG, D))
cf = [x for x in ADM if confB(dem, u, x)]
inC = [x for x in cf if any(key(x) == key(y) for y in GREEK)]
print('conflict pairs: %d, of which in the Greek contract: %d; e.g. %s' % (len(cf), len(inC), cf[:3]))
print('VERDICT:', 'rivals, kind (%s)' % ('i' if inC else 'ii') if cf else 'not rivals')
# the same two candidates with the mediating change NOT admitted
cf0 = [x for x in PAIRS if confB(dem, u, x)]
print('without the mediating change admitted: conflict pairs', len(cf0), '->', 'rivals' if cf0 else 'not rivals')
