# Settlement of the GLM cross-examination, rule 5's check: e2.14b (V2.5 moves (Suff)'s defeat set, claimed only since correction
# O2, never computed): (Suff) L536's defeat set on the worked accounts, 'nothing tried' history, off and under V2.5, j with an
# argument not using (E) that rules out Expl(ℰ) (r, r → ¬Expl(ℰ), MP). Run from the section-2 round-2 copy's folder; writes nothing.
import os, sys
sys.path.insert(0, os.getcwd())
import s108r2_s2_cases as M
from model.core import account
from model.claims_s41 import suff_defeats, expl_ruled_out, SUFF_READINGS
from model.args import Assessor, Imp, Not
rows = [(lab, c) for lab, where, c in M.worked_cases()]
H = "nothing tried, H=∅"
assert H in M.HISTORIES, M.HISTORIES
for s in ("off", "V2.5 (C7)", "V2.5 (C7) × R2V2.3a"):
    with M.setting(**M.SETTINGS[s]):
        n = 0; ins = {r: 0 for r in SUFF_READINGS}
        for lab, c in rows:
            acc = bool(account(c))
            if not acc:
                continue
            n += 1
            ex = M.expl_row(c)[H]            # Account ∧ ¬Dec(t) on the history
            dec = not ex
            j = Assessor(["MP"], ["r", Imp("r", Not("Expl_E"))])
            out, _ = expl_ruled_out(j, "E")
            for r in SUFF_READINGS:
                ins[r] += bool(suff_defeats(acc, dec, out, r))
        print("%-22s accounts %d; history '%s'; in (Suff)'s defeat set: %s" % (s, n, H, "; ".join("%s %d" % kv for kv in ins.items())))
