# S108 Part A round 2, section 3: the round-2 variants of section 3 as readings the program can switch on and off.
# S108R2_S3_VARIANT in the environment (or set_variant from a script): "none" (default) = the program after round 4, with round 1's
# switches (s108s3) as they are. Round 1's S108_S3_VARIANT must be "none" when a round-2 variant is on.
#   R2V3.1  S108-3-I2 and I5's other choice: CT is a Build subhistory (CT asks ExplUse at its output) and ExplUse asks Acc(ℰ′) of the
#           ℰ′ whose claim the output uses (round 1's V3.4 with S108_S3_CT=build); which ℰ′ is data (S108R2_S3_CLAIM, read by the
#           scripts: own, widest, designation (R2-3-I1), gamma, port); in the program's functions R2V3.1 is V3.4 + build
#   R2V3.2  D13.8's record key: the program keys a record by the change (a flag per change, claims_b.episode; I174), which is the
#           variant's new form; S108R2_S3_RECKEY=contract gives the formal core's words (Rec_h'(ρ_{q(o')}), any record of the new
#           contract in h'), the variant's old form. Default "change" = the program as it is
#   R2V3.3  the trace's extent and the tag encoding: no function of the program reads either (Prepares is a label at one occurrence,
#           I56; Held at an output is set by each claim, I90): computed in the scripts only (s108r2_s3_*.py)
#   R2V3.4  D15.8's parts(t) read as the ports of t's codomain E with their bindings π(v) (R2-3-I4); S108R2_S3_PARTS: components
#           (default, S108-3-I4 = I158 as registered), ports, edits (τ's image with its source; the reply's other choice)
#   R2V3.5  D15.8 with no construction stated: 𝒯 = ∅ (R2-3-I5), where the program reads Θ's admission alone (S108-3-I3)
#   R2V3.6  I90's other choice: provenance_of (the hand-set histories 'Dec', 'Con', 'Sel') builds a chain and computes Rep
#           (prov_fixed_points, cut T′, the least fixed point; H one occurring pair; a trace per occurrence) (R2-3-I6)
#   R2V3.7  D11.3: ⪯_h := the reflexive closure of ≺_h (≺_h the covering steps of a chain), not ≺_h* (R2-3-I7): Con's witness
#           (D12.2) at o_t or an immediate predecessor in h'; under K (strict) an immediate predecessor only
#   R2V3.8  D9.2: every argument has at least one step (args.ARG_READING := "I88"); departs from S41 Q23
#   R2V3.9  D9.1 without 'Ans_p(a,b) = y': a formula with an answer atom is no claim; an argument with such a node is no argument;
#           X_j(ψ) = ∅ for ψ no claim (R2-3-I8: a record leaf of a test stays a claim; S108R2_S3_I8=dropped: records too)
#   R2V3.10 D15.5 without the construction disjunct: Can := owned RetReal; D18.1's Can loses Ω (read only by that disjunct)
# Nothing here changes the theory (rule 11). Standard library only.
import os

from . import s108s3

VARIANTS = ("none", "R2V3.1", "R2V3.2", "R2V3.3", "R2V3.4", "R2V3.5", "R2V3.6", "R2V3.7", "R2V3.8", "R2V3.9", "R2V3.10")
VARIANT = os.environ.get("S108R2_S3_VARIANT", "none")
if VARIANT not in VARIANTS:
    raise ValueError("S108R2_S3_VARIANT must be one of %s" % (VARIANTS,))
RECKEYS = ("change", "contract")
RECKEY = os.environ.get("S108R2_S3_RECKEY", "change")
if RECKEY not in RECKEYS:
    raise ValueError("S108R2_S3_RECKEY must be one of %s" % (RECKEYS,))
PARTS_READINGS = ("components", "ports", "edits")
PARTS = os.environ.get("S108R2_S3_PARTS", "components")
if PARTS not in PARTS_READINGS:
    raise ValueError("S108R2_S3_PARTS must be one of %s" % (PARTS_READINGS,))
I8S = ("kept", "dropped")
I8 = os.environ.get("S108R2_S3_I8", "kept")
if I8 not in I8S:
    raise ValueError("S108R2_S3_I8 must be one of %s" % (I8S,))
if VARIANT != "none" and s108s3.VARIANT != "none":
    raise ValueError("a round-2 variant of section 3 runs with round 1's S108_S3_VARIANT none")


def _apply():
    """R2V3.1 is round 1's V3.4 with CT reading ExplUse (S108-3-I2); R2V3.4 reads parts as ports unless another reading is set."""
    global PARTS
    if VARIANT == "R2V3.1":
        s108s3.set_variant("V3.4", "build")
    if VARIANT == "R2V3.4" and PARTS == "components" and "S108R2_S3_PARTS" not in os.environ:
        PARTS = "ports"


_apply()


def on(v):
    return VARIANT == v


def set_variant(v, reckey=None, parts=None, i8=None):
    """For the scripts: set the round-2 variant and the sub-readings. R2V3.1 also sets round 1's switch to V3.4 with CT reading
    ExplUse, and leaving R2V3.1 resets it; round 1's switch is otherwise the script's own (s108s3.set_variant)."""
    global VARIANT, RECKEY, PARTS, I8
    if v not in VARIANTS:
        raise ValueError(v)
    was = VARIANT
    VARIANT = v
    RECKEY = reckey or "change"
    PARTS = parts or ("ports" if v == "R2V3.4" else "components")
    I8 = i8 or "kept"
    if v == "R2V3.1":
        s108s3.set_variant("V3.4", "build")
    elif was == "R2V3.1":
        s108s3.set_variant("none", "prepares")


# ---- R2V3.2: D13.8's record key -----------------------------------------------------------------------------------------

def changes_recorded(qs, recs):
    """Every change of contract in the chain qs carries its record. recs[i]: a record made at o_i of ρ_{q(o_i)} (the program's flag
    for the change into o_i). 'change' (the program, I174; R2V3.2's new form): the change into o_i needs recs[i]. 'contract' (the
    formal core's words): it needs some record of ρ_{q(o_i)} in h' (any o_j of the chain with recs[j] and q(o_j) = q(o_i))."""
    chg = [i for i in range(1, len(qs)) if qs[i] != qs[i - 1]] if qs else []
    if RECKEY == "contract":
        return all(any(recs and recs[j] and qs[j] == qs[i] for j in range(len(qs))) for i in chg)
    return all(recs and recs[i] for i in chg)


# ---- R2V3.4, R2V3.5: D15.8's population ------------------------------------------------------------------------------------

def parts_read(cand, comps):
    """parts of the transport made of the named components of cand.E, under the reading PARTS. components: the names themselves
    (I158 as registered, S108-3-I4); ports: the ports of cand.E in their footprints, each with its binding π(v) (R2-3-I4); edits:
    the edits of cand.E that τ reaches, each with its source (the construction's settings)."""
    if comps is None:
        return None
    if PARTS == "components":
        return set(comps)
    if PARTS == "ports":
        out = set()
        for k in comps:
            for v in cand.E.foot[k]:
                tr = cand.pi.get(v)
                out.add((v, getattr(tr, "name", repr(tr)), tuple(getattr(tr, "dports", ()))))
        return out
    return set((e2, e) for e, e2 in cand.tau.items())


def no_construction_admits():
    """Whether a history that states no construction meets D15.8's parts clause: yes (S108-3-I3, the program's) or, under R2V3.5,
    no (𝒯 = ∅, R2-3-I5)."""
    return not on("R2V3.5")


# ---- R2V3.7: ⪯_h in a chain ----------------------------------------------------------------------------------------------

def witnesses(i, o, strict=False):
    """The positions x of the sub-chain o_i … o_o with x ⪯ o (strict: x ≺ o), for Con's witness (D12.2). Default: every x from i
    (⪯ = ≺*); R2V3.7: o itself and its immediate predecessor (the reflexive closure of the covering steps)."""
    xs = range(i, o) if strict else range(i, o + 1)
    if on("R2V3.7"):
        xs = [x for x in xs if x >= o - 1]
    return list(xs)


# ---- R2V3.9: which formulas are claims -------------------------------------------------------------------------------------

ANSWER_PREFIXES = ("ans", "Ans", "E_ans")


def is_answer_atom(a):
    return isinstance(a, str) and a.startswith(ANSWER_PREFIXES)


def is_claim(f, atoms_fn):
    """D9.1 under R2V3.9: a formula with an answer atom ('Ans_p(a,b) = y'; the program's atoms named ans…, Ans…, E_ans…) is no
    claim. Every formula is a claim otherwise."""
    if not on("R2V3.9"):
        return True
    return not any(is_answer_atom(a) for a in atoms_fn(f))
