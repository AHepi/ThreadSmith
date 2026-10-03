# S108 Part A, section 3: the eight variants of section 3 as readings the program can switch on and off.
# S108_S3_VARIANT in the environment (or s108s3.VARIANT set by a script): "none" (default) = the program after round 4.
#   V3.1  D9.7  RO(α, φ) :⟺ Incons(φ, concl(α))                 (the block deleted: no leaf with ¬φ, no record made from ¬φ)
#   V3.2  D9.4  Live_j(d; u) :⟺ d ∈ Accepted_j(ξ)                 (the disjunct through a step below u deleted)
#   V3.3  D9.6  Usable_j(α) :⟺ ∀u ∈ steps(α) Usable_j(u)          (the premise-alone clause deleted: a bare claim usable by all)
#   V3.4  D13.3 ExplUse(o, c) :⟺ UsesClaim(o, 'Acc(ℰ)') ∧ Acc(ℰ)   (the claim must hold)
#   V3.5  D13.8 Episode(h') :⟺ h' ⊆ h is a subhistory              (the record clause deleted)
#   V3.6  D15.8 𝒯 := {t : Θ admits t}                              (the parts clause deleted)
#   V3.7  D11.4 ActRoute without ∃(x,x') ∈ K: val_r(…[i:=x]) ≠ val_r(…[i:=x'])
#   V3.8  D14.7 CreateEx without CreativeCriticalEpisode(s, Δ, h, e)
# S108_S3_CT (V3.4 only): "prepares" (default) = D12.2 as written: CT reads Prepares(h', o, ·), no ExplUse (the program's
#   DEP: CT → h, Prepares, BindingConstruction); "build" = the reply's reading (invention S108-3-I2): the construction trace
#   Con asks for is a Build subhistory, so CT also asks ExplUse at its output.
# Nothing here changes the theory (rule 11). Standard library only.
import os

VARIANTS = ("none", "V3.1", "V3.2", "V3.3", "V3.4", "V3.5", "V3.6", "V3.7", "V3.8")
VARIANT = os.environ.get("S108_S3_VARIANT", "none")
if VARIANT not in VARIANTS:
    raise ValueError("S108_S3_VARIANT must be one of %s" % (VARIANTS,))
CT_READINGS = ("prepares", "build")
CT_READING = os.environ.get("S108_S3_CT", "prepares")
if CT_READING not in CT_READINGS:
    raise ValueError("S108_S3_CT must be one of %s" % (CT_READINGS,))


def on(v):
    return VARIANT == v


def set_variant(v, ct=None):
    global VARIANT, CT_READING
    if v not in VARIANTS:
        raise ValueError(v)
    VARIANT = v
    if ct is not None:
        CT_READING = ct


# ---- D13.3 ExplUse under V3.4 ------------------------------------------------------------------------------------------

def expl_use(uses_claim=True, acc=None):
    """ExplUse(o, c) given UsesClaim(o, 'Acc(ℰ)') (Θ, I90) and acc = Acc(ℰ) computed (None: not computed, the case builds
    no ℰ). none: UsesClaim alone, the claim need not hold (I178). V3.4: UsesClaim ∧ Acc(ℰ); where acc is None the value is
    not computed and the Θ-set value (I56: ExplUse set to hold) is kept, recorded as S108-3-I1."""
    if not uses_claim:
        return False
    if on("V3.4") and acc is not None:
        return bool(acc)
    return True


def ct_reads_expluse():
    """Whether CT (D12.2) asks ExplUse at the trace's output: only under V3.4 with the reply's reading (S108-3-I2)."""
    return on("V3.4") and CT_READING == "build"


# ---- D15.8 the population under V3.6 -----------------------------------------------------------------------------------

def in_population(admitted, parts=None, stated=None):
    """t ∈ 𝒯 (D15.8): Θ admits t ∧ parts(t) ⊆ the parts of the stated construction (I158). parts, stated: sets, or None
    where the case states no construction (the program's default: the clause read through Θ as met, S108-3-I3). V3.6: Θ's
    admission alone."""
    if not admitted:
        return False
    if on("V3.6") or parts is None or stated is None:
        return True
    return set(parts) <= set(stated)


# ---- D14.7 CreateEx under V3.8 -----------------------------------------------------------------------------------------

def create_ex(cce, origin, rest):
    """CreateEx = CreativeCriticalEpisode ∧ Origin-and-the-rest (D14.7). origin: Attempt ∧ New ∧ Build; rest: Repair, O_ex,
    Deploy, ProducesVia, Acc, c ∈ Result, e_c ⪯ e. V3.8: the CCE conjunct deleted."""
    if on("V3.8"):
        return bool(origin and rest)
    return bool(cce and origin and rest)
