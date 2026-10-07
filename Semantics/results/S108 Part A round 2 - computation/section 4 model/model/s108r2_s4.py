# S108 Part A round 2, section 4 (rule 5 of "S108 Part A round 2 - how the replies will be read, written before sending.md"):
# the round-2 variants of section 4 that change code the claim suite runs, each a reading the program can switch on.
# "none" = round 1's copy of section 4 (itself the program after round 4 under every round-1 switch off), byte for byte.
# Nothing here changes the theory (rule 11); this folder is a copy. Round 1's switch (s108_s4, S108_S4_*) is kept, so
# R2V4.1 is round 1's V4.1 with S108_S4_V41_Q in {some, some-exempt, some-exempt-set} and S108_S4_V41_SUFF=covaried.
#   S108R2_S4_VARIANT  none | R2V4.5 | R2V4.7
#     R2V4.5  E9's question reads Q_id, the set query (x1_3, x2_3): which thing ends where (R2-4-I5), in place of the
#             occupancy port o1_3; C, t1, S0, t0 unchanged.
#     R2V4.7  L522.s1's clause on the assessor's declared inputs struck: nothing j admits, accepts or scopes is a declared
#             input, so no step is by a declared form and no premise is accepted: usable_j(α) is false for every α
#             (S108r2-4-I2, the nearest statable reading of "not statable").
import os

VARIANTS = ("none", "R2V4.5", "R2V4.7")
VARIANT = os.environ.get("S108R2_S4_VARIANT", "none")
assert VARIANT in VARIANTS, VARIANT


def q_id():
    from .core import FnQuery, BOT

    def f(org, a, b, delta):
        i1, i2 = org.ports.index("x1_3"), org.ports.index("x2_3")
        vals = set((z[i1], z[i2]) for z in org.sol(a, b))
        return next(iter(vals)) if len(vals) == 1 else BOT
    return FnQuery(f, "Q_id (the set query (x1_3, x2_3), R2-4-I5)")
