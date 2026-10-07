# Settlement of the GLM cross-examination, Xc1's part r2e3.18b (R2V3.8 moves X:(Nec), not computed in round 2): the mirror of
# section 3's part D "(Suff) by a premise alone" for (Nec). Run from the section-3 round-2 copy's folder; imports only; writes nothing.
import os, sys
sys.path.insert(0, os.getcwd())
from s108r2_s3_common import set_state, reset
from model.core import ONE, account, faithful
from model.args import Not, And, Imp, Leaf, Assessor, X, enumerate_args
from model.claims_b import fwd_pole_cand
from model.claims_s41 import not_using_E, provenance_of
e = "Expl_E"
for name, kw in (("none", {}), ("R2V3.8", dict(r2="R2V3.8"))):
    set_state(**kw)
    p_, c_ = fwd_pole_cand()
    acc, pres = bool(account(c_)), bool(faithful(c_))
    for kind in ("Con", "Sel", "Dec"):
        s0, k0, dec = provenance_of(c_, kind, [(ONE, "b1_45")])
        for prem_name, prem in (("ψ' = r ∧ (r → Expl(ℰ))", [And("r", Imp("r", e))]), ("r, r → Expl(ℰ)", ["r", Imp("r", e)])):
            for forms in (("MP", "AndE"), ("MP",)):
                jx = Assessor(list(forms), prem)
                xs = [a for a in X(jx, Not(e), enumerate_args(prem, forms=forms, depth=2)) if not_using_E(a, "E")]
                outn = bool(xs)
                print("%-7s %-4s j accepts %-24s forms %-7s: arguments not using (E) ruling out ¬Expl(ℰ) %d (premise alone %d); "
                      "(Nec) defeated as L538 states it (out ∧ ¬Faithful_C(t)) %s; as L61's 'their' reads (out ∧ ¬(Acc ∧ ¬Dec)) %s"
                      % (name, kind, prem_name, "/".join(forms), len(xs), sum(1 for a in xs if isinstance(a, Leaf)),
                         outn and not pres, outn and not (acc and not dec)))
    reset()
