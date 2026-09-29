# S108 Part A, section 4 (rule 5 of "S108 Part A - how the replies will be read, written before sending.md"): the eight
# variants of the reply for section 4 (V4.1-V4.8), each a reading the program can switch on. "none" = the program after
# round 4, byte for byte. Nothing here changes the theory (rule 11); this folder is a copy.
#   S108_S4_VARIANT   none | V4.1 | V4.2 | V4.3 | V4.4 | V4.5 | V4.6 | V4.7 | V4.8   (the environment; default none)
# Sub-choices, each recorded as an invention of this computation (S36, S108-4-In in the results file):
#   S108_S4_V41_SUFF  kept (default: the variant as written; D16.XV's (Suff) shape unchanged) | covaried ((Suff)'s
#                     antecedent gains ¬Slot with being an explanation)                                     [S108-4-I1]
#   S108_S4_V41_Q     every (default: the reply's reading of D6.3) | some | some-exempt | some-exempt-set       [S108-4-I1]
#   S108_S4_V42_SUFF  rule (default: only the rule Acc ∧ Dec ⇒ ¬Expl deleted; (Suff)'s shapes as D16.XV writes them) |
#                     L17 (L17's antecedent follows being an explanation, now Acc; L536 keeps ¬Dec: the reply's trace) |
#                     both (L17 and L536 lose ¬Dec)                                                          [S108-4-I2]
#   S108_S4_V43_READ  holding (default: Sel(t) ∨ CT(t) read at the holding, on its own history, D12.1, D12.2) |
#                     prov (read through D12.3's inherited provenance: then V4.3 is the current reading)     [S108-4-I3]
import os

VARIANTS = ("none", "V4.1", "V4.2", "V4.3", "V4.4", "V4.5", "V4.6", "V4.7", "V4.8")
VARIANT = os.environ.get("S108_S4_VARIANT", "none")
assert VARIANT in VARIANTS, VARIANT
V41_SUFF = os.environ.get("S108_S4_V41_SUFF", "kept")
assert V41_SUFF in ("kept", "covaried")
V41_Q = os.environ.get("S108_S4_V41_Q", "every")
V42_SUFF = os.environ.get("S108_S4_V42_SUFF", "rule")
assert V42_SUFF in ("rule", "L17", "both")
V43_READ = os.environ.get("S108_S4_V43_READ", "holding")
assert V43_READ in ("holding", "prov")


def has_slot(cand, quantifier=None):
    """Slot_C(ℰ) (D6.3): some component of E is a slot (¬NC1; boundary coordinates are components here, I79)."""
    from . import core
    return any(core.slot(cand, k, quantifier=quantifier or V41_Q) for k in cand.E.comps)


def expl(acc, dec, slot=False, selct=None, variant=None):
    """Being an explanation (D16.XV; L17, L49, L69) under the variant. slot: Slot_C(ℰ) (V4.1 reads it); selct: Sel(t) ∨ CT(t)
    at the holding, read as S108_S4_V43_READ says (V4.3 reads it; None: ¬Dec, a holding not reached by a transfer)."""
    v = variant or VARIANT
    if v == "V4.1":
        return bool(acc and not dec and not slot)
    if v == "V4.2":
        return bool(acc)
    if v == "V4.3":
        sc = (not dec) if (selct is None or V43_READ == "prov") else selct
        return bool(acc and not dec and sc)
    return bool(acc and not dec)


def suff_antecedent(acc, dec, reading, slot=False, selct=None, variant=None):
    """The antecedent of (Suff)'s defeat set at L536 and at L17 as S41 writes it (D16.XV), under the variant; the reading
    'L17 as text 104 words it' is a fixed historical reading and does not move."""
    v = variant or VARIANT
    if reading == "L17 as text 104 words it":
        return bool(acc)
    if v == "V4.1" and V41_SUFF == "covaried":
        return bool(acc and not dec and not slot)
    if v == "V4.2" and (V42_SUFF == "both" or (V42_SUFF == "L17" and reading == "L17 (S41)")):
        return bool(acc)
    if v == "V4.3":
        sc = (not dec) if (selct is None or V43_READ == "prov") else selct
        return bool(acc and not dec and sc)
    return bool(acc and not dec)


def suff_conjecture(acc, dec, slot=False, selct=None, variant=None):
    """(Suff) as conjectured (FC30.new1 (c)): its antecedent (at L536) ⇒ Expl."""
    return suff_antecedent(acc, dec, "L536", slot, selct, variant)


def uses_reading():
    """'an argument not using (E)' (D16.XV, I196): V4.4 reads it at the instance."""
    return "instance" if VARIANT == "V4.4" else "symbol"


def dep_patch(DEP):
    """D18.1's graph (the program's DEP) co-varies with the definition the variant changes: each edge set is the symbols
    the varied right-hand side uses."""
    d = {k: list(v) for k, v in DEP.items()}
    if VARIANT == "V4.1":
        d["DefeatConds"] = d["DefeatConds"] + ["Slot"]
    elif VARIANT == "V4.2" and V42_SUFF == "both":
        d["DefeatConds"] = [x for x in d["DefeatConds"] if x != "Dec"]
    elif VARIANT == "V4.3" and V43_READ == "holding":
        d["DefeatConds"] = d["DefeatConds"] + ["CT"]
    elif VARIANT == "V4.7":
        d["Enable"] = [x for x in d["Enable"] if x not in ("(R)", "β")]
    elif VARIANT == "V4.8":
        d["Underdet"] = [x for x in d["Underdet"] if x != "surv"]
    return d


def underdet_members(pop, H, faithful_on):
    """The members of 𝒯 D12.9's Underdet reads: those surviving on H (now); every member (V4.8)."""
    if VARIANT == "V4.8":
        return list(pop)
    return [c for c in pop if faithful_on(c, H)]
