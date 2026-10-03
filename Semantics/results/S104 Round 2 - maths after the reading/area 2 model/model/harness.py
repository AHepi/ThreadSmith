# S104 round 2 (maths): the search harness. Each claim's test returns a list of parts; each part is
# a universal statement searched for a counterexample, an existential one searched for a witness, a
# computation on one of the text's worked cases, or a note that it was not tested and why.
import random
import time

HOLDS = "HOLDS ON ALL MODELS TRIED"
CEX = "COUNTEREXAMPLE FOUND"
NOT = "NOT TESTED"

REG = {}
VAC = "__hypothesis not met__"  # returned by a check when the model does not meet the claim's hypothesis


def claim(cid, inventions=()):
    """Register a test. `inventions`: the inventions of this program the test itself uses (the claim's
    own inventions are read from formal claims.json)."""
    def deco(fn):
        REG[cid] = (fn, list(inventions))
        return fn
    return deco


class Settings:
    def __init__(self, scale=1.0, time_cap=20.0, verbose=False):
        self.scale, self.time_cap, self.verbose = scale, time_cap, verbose


def seed_for(cid, k):
    return 104000 + int(cid[2:]) * 10 + k


def _space(sizes, per_size, families, note):
    return dict(sizes_from=repr(sizes[0]) if sizes else None, sizes_to=repr(sizes[-1]) if sizes else None,
                n_sizes=len(sizes), per_size=per_size, families=families, note=note)


def forall(S, cid, k, label, statement, gen, check, sizes, per_size, families, inventions=(), note=""):
    """Search for a counterexample to `statement`. gen(rng, size) -> model or None; check(model) -> None
    when the statement holds of the model, else a full written-out counterexample. Sizes are tried in
    ascending order, so the first counterexample found is the smallest found."""
    seed = seed_for(cid, k)
    rng = random.Random(seed)
    per = max(1, int(per_size * S.scale))
    t0 = time.time()
    n = 0
    vac = 0
    stopped = None
    for size in sizes:
        for i in range(per):
            m = gen(rng, size)
            if m is None:
                continue
            n += 1
            r = check(m)
            if r == VAC:
                vac += 1
                r = None
            if r:
                return dict(label=label, kind="for all", statement=statement, status="counterexample found",
                            seed=seed, models_tried=n, hypothesis_met=n - vac, smallest_size=repr(size), counterexample=r,
                            space=_space(sizes, per, families, note), inventions=list(inventions), seconds=round(time.time() - t0, 2))
            if time.time() - t0 > S.time_cap:
                stopped = "time cap %.0f s reached at size %r" % (S.time_cap, size)
                break
        if stopped:
            break
    return dict(label=label, kind="for all", statement=statement, status="holds on all models tried", seed=seed,
                models_tried=n, hypothesis_met=n - vac, stopped=stopped, space=_space(sizes, per, families, note), inventions=list(inventions),
                seconds=round(time.time() - t0, 2))


def exists(S, cid, k, label, statement, gen, check, sizes, per_size, families, inventions=(), note=""):
    """Search for a witness. check(model) -> None when the model is no witness, else the written-out
    witness."""
    seed = seed_for(cid, k)
    rng = random.Random(seed)
    per = max(1, int(per_size * S.scale))
    t0 = time.time()
    n = 0
    stopped = None
    for size in sizes:
        for i in range(per):
            m = gen(rng, size)
            if m is None:
                continue
            n += 1
            r = check(m)
            if r == VAC:
                r = None
            if r:
                return dict(label=label, kind="there is", statement=statement, status="witness found", seed=seed,
                            models_tried=n, smallest_size=repr(size), witness=r, space=_space(sizes, per, families, note),
                            inventions=list(inventions), seconds=round(time.time() - t0, 2))
            if time.time() - t0 > S.time_cap:
                stopped = "time cap %.0f s reached at size %r" % (S.time_cap, size)
                break
        if stopped:
            break
    return dict(label=label, kind="there is", statement=statement, status="no witness found", seed=seed,
                models_tried=n, stopped=stopped, space=_space(sizes, per, families, note), inventions=list(inventions),
                seconds=round(time.time() - t0, 2))


def exhaustive(cid, label, statement, items, check, space_note, inventions=(), kind="for all"):
    """Every member of a finite space. For 'for all', check -> None or counterexample; for 'there is',
    check -> None or witness."""
    t0 = time.time()
    n = 0
    vac = 0
    for m in items:
        n += 1
        r = check(m)
        if r == VAC:
            vac += 1
            r = None
        if r:
            if kind == "for all":
                return dict(label=label, kind=kind, statement=statement, status="counterexample found", exhaustive=True,
                            models_tried=n, counterexample=r, space=dict(note=space_note), inventions=list(inventions),
                            seconds=round(time.time() - t0, 2))
            return dict(label=label, kind=kind, statement=statement, status="witness found", exhaustive=True,
                        models_tried=n, witness=r, space=dict(note=space_note), inventions=list(inventions),
                        seconds=round(time.time() - t0, 2))
    return dict(label=label, kind=kind, statement=statement,
                status="holds on all models tried" if kind == "for all" else "no witness found", exhaustive=True,
                models_tried=n, hypothesis_met=n - vac, space=dict(note=space_note), inventions=list(inventions), seconds=round(time.time() - t0, 2))


def computed(label, statement, as_claimed, text, inventions=(), note=""):
    """A computation on one of the text's worked cases (or on a model built for the claim)."""
    return dict(label=label, kind="computation", statement=statement,
                status="computed: as claimed" if as_claimed else "computed: not as claimed",
                result=text, inventions=list(inventions), note=note)


def construction(label, statement, holds, text, inventions=(), note=""):
    """A statement that holds of the model by the way the code is written: reported, not counted as a
    search."""
    return dict(label=label, kind="by construction", statement=statement,
                status="holds by construction" if holds else "fails by construction", result=text,
                inventions=list(inventions), note=note)


def look(label, statement, confirmed, text, inventions=(), note=""):
    """A formal claim's 'Look' (a first reading of where a counterexample might lie), checked. Not the
    claim itself: its outcome never makes the claim's status."""
    return dict(label=label, kind="look", statement=statement,
                status="look: as expected" if confirmed else "look: not as expected", result=text,
                inventions=list(inventions), note=note)


def not_tested(label, statement, why):
    return dict(label=label, kind="not tested", statement=statement, status="not tested", why=why, inventions=[])


def overall(parts):
    sts = [p["status"] for p in parts]
    if any(s in ("counterexample found", "computed: not as claimed", "fails by construction") for s in sts):
        return CEX
    if all(s == "not tested" for s in sts):
        return NOT
    return HOLDS
