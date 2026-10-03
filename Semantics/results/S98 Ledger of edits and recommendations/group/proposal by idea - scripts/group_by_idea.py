# S98 "by idea" proposal: place every change of anchored.jsonl in the idea its sentences carry.
# run(version) returns the assignment; version "v1" is the lens as first tried, "v2" after the one adjustment.
import json, os, sys, collections, importlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
GROUP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import ideas

IDX = [json.loads(l) for l in open(os.path.join(GROUP, "sentence index of the latest text.jsonl"))]
U = {u["id"]: u for u in IDX}
R = [json.loads(l) for l in open(os.path.join(GROUP, "anchored.jsonl"))]
NOWORD = "[no wording given] "

def strip(s):
    s = s or ""
    return s[len(NOWORD):] if s.startswith(NOWORD) else s

def norm(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()} if s else {}

def add(acc, d, w=1.0):
    for k, v in d.items():
        acc[k] = acc.get(k, 0) + w * v

def mean(ds):
    ds = [d for d in ds if d]
    acc = {}
    for d in ds:
        add(acc, d, 1.0 / len(ds))
    return acc

def corpus():
    out, seen = [], set()
    for t in [u["text"] for u in IDX] + [t for r in R for t in ((r["old_sentence"], r["new_sentence"])
                                          if (r["old_sentence"] or r["new_sentence"]) else (r["old"], r["new"]))]:
        if t and t not in seen:
            seen.add(t); out.append(t)
    return out

def run(version):
    X = importlib.reload(ideas)
    if version == "v2":
        import ideas_v2
        importlib.reload(ideas_v2).apply(X, corpus())

    def cue_raw(text):
        d = collections.Counter()
        if text:
            for k, cues in X.COMPILED.items():
                for rx, w in cues:
                    if rx.search(text):
                        d[k] += w
        return d

    SENT = {}
    for u in IDX:
        raw = cue_raw(u["text"] if u["kind"] != "heading" else u["text"].lstrip("# "))
        for k, w in X.home(u["part"], u["heading"], u["label"]):
            raw[k] += w
        SENT[u["id"]] = norm(raw)

    def classify(cid, ms):
        rec_texts, own_texts, lat, near, parts = [], [], [], [], []
        for r in ms:
            o, n = strip(r["old"]), strip(r["new"])
            for t in (o, n):
                if t and t not in own_texts:
                    own_texts.append(t)
            cand = [o, n] if r["scope"] == "term" else ([t for t in (r["old_sentence"], r["new_sentence"]) if t] or [o, n])
            for t in cand:
                if t and t not in rec_texts:
                    rec_texts.append(t)
            for s in r["latest_sentences"]:
                if s not in lat:
                    lat.append(s)
            if r.get("latest_nearest"):
                near.append(r["latest_nearest"]["sentence"])
            for p in r.get("latest_parts") or [r.get("latest_part")]:
                if p and p not in parts:
                    parts.append(p)
        P_rec = mean([norm(cue_raw(t)) for t in rec_texts])
        P_own = norm(cue_raw(" \n ".join(own_texts)))
        if lat:
            P_lat, place = mean([SENT[s] for s in lat]), "latest sentences"
        else:
            pdef = [X.PART_DEFAULT[X.part_key(p)] for p in parts if X.part_key(p)]
            P_part = mean([{k: 1.0} for k in pdef])
            P_near = mean([SENT[s] for s in near if s in SENT])
            if P_near and P_part:
                P_lat = {}; add(P_lat, P_near, 0.5); add(P_lat, P_part, 0.5)
            else:
                P_lat = P_near or P_part
            place = "nearest sentence and Part named" if P_near else ("Part named" if P_part else "none")
        is_term = all(r["scope"] == "term" for r in ms)
        final = {}
        if is_term:
            add(final, P_own, 1.5); add(final, P_lat, 0.5)
        else:
            add(final, P_rec, 1.0); add(final, P_lat, 1.0); add(final, P_own, 0.5)
        placed_by = "its wording and its place" if (P_rec or P_own) and P_lat else (
            "its wording only" if (P_rec or P_own) else ("its place only" if P_lat else "nothing"))
        tot = sum(final.values())
        if not tot:
            final, tot = {"frame": 1.0}, 1.0
        sh = sorted(((v / tot, k) for k, v in final.items()), reverse=True)
        top_share, top = sh[0]
        cue_top = top
        also = [k for s, k in sh[1:] if s >= 0.5 * top_share and s >= 0.15]
        near_tie = [k for s, k in sh[1:] if s >= 0.75 * top_share]
        rule = "most weight"
        dom = None
        if getattr(X, "DOMINANT_HOME", None):
            hs = ({X.DOMINANT_HOME(U[s]["part"], U[s]["heading"], U[s]["label"]) for s in lat} if lat
                  else ({X.DOMINANT_HOME(p, "", "") for p in parts} if parts else {None}))
            if len(hs) == 1 and None not in hs:
                dom = hs.pop()
        if dom and dom != top:
            also, near_tie, top, rule = [top] + [k for k in also if k != dom], [], dom, "place that speaks of the ideas as a whole"
        if getattr(X, "form_only", None) and all(X.form_only(r) for r in ms):
            also, near_tie, top, rule = [top], [], "form", "form only"
        lat_parts = []
        for s in lat:
            pk = X.part_key(U[s]["part"])
            if pk and pk not in lat_parts:
                lat_parts.append(pk)
        named = [X.part_key(p) for p in parts if X.part_key(p)]
        return {"change_id": cid, "group": top, "also": also, "near_tie": near_tie, "rule": rule, "cue_top": cue_top,
                "share": round(top_share, 3), "shares": {k: round(s, 3) for s, k in sh[:4]},
                "records": [r["rid"] for r in ms], "placed_by": placed_by, "place": place, "is_term": is_term,
                "latest_sentences": lat, "parts": [p.strip() for p in (lat_parts or named)],
                "first_part": (lat_parts or named or [None])[0], "statuses": sorted({r["status"] for r in ms}),
                "kinds": sorted({r["kind"] for r in ms}), "terms": sorted({t for r in ms for t in r["terms"]})}

    changes = collections.OrderedDict()
    for r in R:
        changes.setdefault(r["change_id"], []).append(r)
    out = [classify(cid, ms) for cid, ms in changes.items()]
    per_record = {r["rid"]: classify(r["rid"], [r])["group"] for r in R}
    return out, per_record, X

def measure(out, per_record, X):
    m = {}
    m["changes"] = len(out)
    m["records"] = sum(len(o["records"]) for o in out)
    m["placed_by"] = dict(collections.Counter(o["placed_by"] for o in out))
    m["place"] = dict(collections.Counter(o["place"] for o in out))
    m["rule"] = dict(collections.Counter(o["rule"] for o in out))
    m["also_changes"] = sum(1 for o in out if o["also"] and o["group"] != "form")
    m["also_records"] = sum(len(o["records"]) for o in out if o["also"] and o["group"] != "form")
    m["near_tie_changes"] = sum(1 for o in out if o["near_tie"])
    m["weak_changes"] = sum(1 for o in out if o["share"] < 0.30 and o["rule"] == "most weight")
    multi = [o for o in out if len(o["records"]) > 1]
    split = [o for o in multi if len({per_record[r] for r in o["records"]}) > 1]
    m["multi_record_changes"] = len(multi)
    m["split_changes"] = len(split)
    m["split_records_off"] = sum(sum(1 for r in o["records"] if per_record[r] != o["group"]) for o in split)
    groups = {}
    for k in X.KEYS:
        g = [o for o in out if o["group"] == k]
        pc = collections.Counter((o["first_part"] or "no Part").strip() for o in g)
        tc = collections.Counter(t for o in g for t in o["terms"])
        groups[k] = {"changes": len(g), "records": sum(len(o["records"]) for o in g),
                     "also": sum(1 for o in g if o["also"] and k != "form"), "near_tie": sum(1 for o in g if o["near_tie"]),
                     "mean_share": round(sum(o["share"] for o in g) / len(g), 2) if g else 0,
                     "parts": pc.most_common(), "terms": tc.most_common(6)}
    m["groups"] = groups
    return m

if __name__ == "__main__":
    for v in sys.argv[1:] or ["v1", "v2"]:
        out, pr, X = run(v)
        m = measure(out, pr, X)
        print(v, {k: m[k] for k in m if k != "groups"})
        for k, g in m["groups"].items():
            print(f"  {k:14} {g['changes']:4} {g['records']:4} also {g['also']:3} tie {g['near_tie']:3} share {g['mean_share']:.2f}  " +
                  ", ".join(f"{p}:{c}" for p, c in g["parts"][:4]))
