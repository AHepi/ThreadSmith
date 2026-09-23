#!/usr/bin/env python3
"""s80_table.py: completeness, adjudication inputs, and the tables of round S80 (plan S80, second version). It applies
the counting function and the decision rule frozen in that plan; nothing here is chosen after the results are seen.

  python Semantics/tools/s80_table.py check                        # every expected report present and complete?
  python Semantics/tools/s80_table.py adjudicate KEY_FILE          # write marks/adjudication_inputs/<rid>.md
  python Semantics/tools/s80_table.py tables KEY_FILE              # write TABLES.md and TABLES.json
(--test-key skips the key's SHA-256 check; it is refused on the real output root.)

Counting function (frozen). Key cell (report, error): FOUND if both markers say FOUND; NOT if both say NOT FOUND or
PARTIAL; otherwise the adjudicator's verdict decides (FOUND, or NOT for NOT FOUND and PARTIAL), and the cell is shown in
the adjudicated column. Report item: a false alarm if both markers say MISTAKEN; not one if neither does (an item a
marker credits to a key error, or does not list, is "not MISTAKEN"); otherwise the adjudicator decides. UNCLEAR (both
markers UNCLEAR) and PARTIAL (a NOT cell where a marker said PARTIAL) are their own columns. A report with one valid
mark (the other failed twice) is counted from that mark alone and flagged single-marked. A report with no valid mark,
or no report, is missing: left out of its cell's mean (the n is shown), never counted as zero. The adjudicator also
re-marks agreed cells chosen by s80_common.drift_selected (a hash rule fixed before the run, about 20%); those
re-marks are a drift check only and never change a count.

Decision rule (frozen), per API reader: skill effect = mean HV errors found per seeded report (of 4) under the skill
minus the same under the placebo, at the same thinking setting; 95% percentile bootstrap interval, reports resampled
with replacement within each condition, 10,000 resamples, seed fixed. "The skill adds something": at thinking on, the
interval's lower end is above zero on at least 2 of the 3 API readers, and on those readers the clean document's
false-alarm rate per item under the skill exceeds the placebo's by no more than 0.10. "Abandon": on no API reader at
either thinking setting is the lower end above zero for HV or for GEN. Otherwise "no decision at this size". The Opus
arm is reported and does not vote. Read only when every expected cell is marked and every dispute adjudicated;
otherwise the output says PROVISIONAL and the decision is not read.
"""
import json, math, os, random, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C

READERS_DIR = os.path.join(C.OUT, "readers")
MARKS_DIR = os.path.join(C.OUT, "marks")
ADJ_DIR = os.path.join(MARKS_DIR, "adjudication_inputs")
TAGPAT = r"(?:(?:atria|mimo|deepseek)_(?:ST|PT|NT|SO|PO|NO)_(?:seeded|clean)_r[1-5]|opus_[SPN]_(?:seeded|clean)_r[1-3])"
READER_FILE = re.compile(r"^(" + TAGPAT + r")\.(response\.txt|reasoning\.txt|request\.json|request\.md|receipt\.json|"
                         r"error\.txt|pass\d+\.(?:receipt\.json|error\.txt|truncated\.txt|void\.txt|"
                         r"a\d+\.truncated\.txt|a\d+\.reasoning\.txt)|pass\d+\.a\d+\.(?:truncated|reasoning)\.txt)$")
FA_RISE_LIMIT = 0.10


# ================================================================ completeness

def _json(p):
    try:
        return json.loads(C.read(p))
    except Exception:
        return None


def completeness(readers_dir=READERS_DIR):
    files = sorted(os.listdir(readers_dir)) if os.path.isdir(readers_dir) else []
    unexpected = [f for f in files if not READER_FILE.match(f)]
    tags = {}
    for t in C.expected_tags():
        p = lambda ext: os.path.join(readers_dir, t + ext)
        if os.path.exists(p(".response.txt")):
            tags[t] = "ok" if C.report_complete(C.read(p(".response.txt"))) else "response-without-sentinel"
            continue
        failed_passes = sum(1 for f in files if f.startswith(t + ".pass") and f.endswith(".receipt.json")
                            and (_json(os.path.join(readers_dir, f)) or {}).get("failed"))
        rc = _json(p(".receipt.json")) if os.path.exists(p(".receipt.json")) else None
        if rc and rc.get("failed"):
            failed_passes += 1
        if os.path.exists(p(".error.txt")) and not rc:
            failed_passes += 1      # a worker exception
        tags[t] = "missing" if failed_passes == 0 else ("failed" if failed_passes == 1 else "failed-twice")
    per_cell = defaultdict(lambda: defaultdict(int))
    for t, s in tags.items():
        i = C.parse_tag(t)
        per_cell["%s %s %s" % (i["reader"], i["cond"], i["doc"])][s] += 1
    return {"tags": tags, "unexpected": unexpected, "per_cell": {k: dict(v) for k, v in per_cell.items()}}


def print_failures(status):
    bad = {k: v for k, v in status["per_cell"].items() if set(v) != {"ok"}}
    print("expected reports: %d; ok: %d" % (len(status["tags"]), sum(s == "ok" for s in status["tags"].values())))
    for cell, v in sorted(bad.items()):
        print("  %-24s %s" % (cell, ", ".join("%s %d" % kv for kv in sorted(v.items()))))
    for t, s in sorted(status["tags"].items()):
        if s != "ok":
            print("    %s: %s" % (t, s))
    if status["unexpected"]:
        print("unexpected files:", status["unexpected"])


# ================================================================ marks

def load_marks(mp, key):
    """For every mapped report and every marker it should have: status ok / missing / failed / invalid / stale."""
    out = {}
    for rid, v in mp.items():
        info = C.parse_tag(v["tag"])
        if info is None:
            raise SystemExit("MAP.json holds a tag outside the design: %s" % v["tag"])
        ids = C.key_ids(info["doc"])
        rpath = os.path.join(READERS_DIR, v["tag"] + ".response.txt")
        cur = C.sha256(C.read(rpath)) if os.path.exists(rpath) else None
        rec = {}
        for m in C.MARKERS_FOR[info["reader"]]:
            f = os.path.join(MARKS_DIR, "%s_by_%s.response.txt" % (rid, m))
            e = {"status": "missing", "problems": [], "sha256": None}
            if cur != v["response_sha256"]:
                e["status"] = "stale"
                e["problems"] = ["the report's bytes differ from those mapped"]
            elif os.path.exists(f):
                txt = C.read(f)
                e["sha256"] = C.sha256(txt)
                meta = (_json(os.path.join(MARKS_DIR, "opus_inputs", rid + ".meta.json")) if m == "opus"
                        else (_json(os.path.join(MARKS_DIR, "%s_by_%s.receipt.json" % (rid, m))) or {}).get("extra"))
                if not meta or meta.get("report_sha256") != v["response_sha256"]:
                    e["status"], e["problems"] = "stale", ["the mark was made on other bytes (or has no record)"]
                else:
                    norm, probs = C.validate_mark(txt, ids)
                    e["status"], e["mark"], e["problems"] = ("ok", norm, []) if norm else ("invalid", None, probs)
            elif m != "opus" and os.path.exists(os.path.join(MARKS_DIR, "%s_by_%s.receipt.json" % (rid, m))):
                e["status"] = "failed"
            rec[m] = e
        out[rid] = rec
    return out


def item_labels(mark):
    lab = {n: o["verdict"] for n, o in mark["others"].items()}
    for k, kv in mark["key"].items():
        for n in kv["items"]:
            lab.setdefault(n, "KEY")
    return lab


def describe_item(mark, n):
    if n in mark["others"]:
        o = mark["others"][n]
        return "%s (%s)" % (o["verdict"], o["reason"][:300])
    ks = ["%s %s" % (k, kv["verdict"]) for k, kv in mark["key"].items() if n in kv["items"]]
    return "counted it toward the key (%s)" % ", ".join(ks) if ks else "did not list this item"


def cells_of(rid, tag, info, rec):
    """The per-report comparison of the two marks: disputed and agreed cells, and the drift sample."""
    marks = [(m, e["mark"]) for m, e in rec.items() if e["status"] == "ok"]
    ids = C.key_ids(info["doc"])
    res = {"valid_marks": [m for m, _ in marks], "disputed_keys": [], "disputed_items": [], "drift_keys": [],
           "drift_items": [], "agreed_key": {}, "agreed_item": {}}
    if len(marks) != 2:
        return res
    (m1, a), (m2, b) = marks
    for k in ids:
        fa, fb = a["key"][k]["verdict"] == "FOUND", b["key"][k]["verdict"] == "FOUND"
        if fa != fb:
            res["disputed_keys"].append(k)
        else:
            res["agreed_key"][k] = "FOUND" if fa else "NOT"
            if C.drift_selected(tag, k):
                res["drift_keys"].append(k)
    la, lb = item_labels(a), item_labels(b)
    n_items = max(a["report_items_total"], b["report_items_total"])
    for n in range(1, n_items + 1):
        ma, mb = la.get(n) == "MISTAKEN", lb.get(n) == "MISTAKEN"
        if ma != mb:
            res["disputed_items"].append(n)
        else:
            res["agreed_item"][n] = "MISTAKEN" if ma else "NOT"
            if ma or (la.get(n) in C.ITEM_VERDICTS and lb.get(n) in C.ITEM_VERDICTS):
                if C.drift_selected(tag, "item%d" % n):
                    res["drift_items"].append(n)
    return res


def adjudication_meta_now(rid, v, rec, cells):
    return {"rid": rid, "report_sha256": v["response_sha256"],
            "marks_sha256": {m: e["sha256"] for m, e in rec.items()},
            "disputed_keys": cells["disputed_keys"], "disputed_items": cells["disputed_items"],
            "drift_keys": cells["drift_keys"], "drift_items": cells["drift_items"]}


def load_adjudication(rid, meta_now):
    """Return (verdicts, status): status ok / none-needed / missing / invalid / stale."""
    if not (meta_now["disputed_keys"] or meta_now["disputed_items"] or meta_now["drift_keys"]
            or meta_now["drift_items"]):
        return None, "none-needed"
    meta = _json(os.path.join(ADJ_DIR, rid + ".meta.json"))
    f = os.path.join(MARKS_DIR, rid + "_by_adjudicator.response.txt")
    if meta is None:
        return None, "missing"
    if meta != meta_now:
        return None, "stale"
    if not os.path.exists(f):
        return None, "missing"
    adj, probs = C.validate_adjudication(C.read(f), meta["disputed_keys"] + meta["drift_keys"],
                                         meta["disputed_items"] + meta["drift_items"])
    return (adj, "ok") if adj else (probs, "invalid")


# ================================================================ adjudication inputs

def adjudicate(key):
    mp = C.load_map()
    marks = load_marks(mp, key)
    task = C.read(os.path.join(C.PR, "adjudicator task.md"))
    n_new = n_same = 0
    for rid, v in sorted(mp.items()):
        info = C.parse_tag(v["tag"])
        cells = cells_of(rid, v["tag"], info, marks[rid])
        if len(cells["valid_marks"]) != 2:
            continue
        meta = adjudication_meta_now(rid, v, marks[rid], cells)
        if not (meta["disputed_keys"] or meta["disputed_items"] or meta["drift_keys"] or meta["drift_items"]):
            continue
        old = _json(os.path.join(ADJ_DIR, rid + ".meta.json"))
        if old == meta:
            n_same += 1
            continue
        if old is not None:   # the marks changed: the old input and any answer to it are set aside
            sd = os.path.join(MARKS_DIR, "stale", "adjudication")
            os.makedirs(sd, exist_ok=True)
            for f in (os.path.join(ADJ_DIR, rid + ".md"), os.path.join(ADJ_DIR, rid + ".meta.json"),
                      os.path.join(MARKS_DIR, rid + "_by_adjudicator.response.txt")):
                if os.path.exists(f):
                    os.replace(f, os.path.join(sd, os.path.basename(f) + ".%d" % len(os.listdir(sd))))
        (m1, a), (m2, b) = [(m, marks[rid][m]["mark"]) for m in cells["valid_marks"]]
        lines = []
        for k in sorted(set(meta["disputed_keys"] + meta["drift_keys"]), key=C.KEY_IDS_SEEDED.index):
            if k in meta["disputed_keys"]:
                lines.append("- Key error %s, in dispute. One marker: %s, resting on items %s; evidence: \"%s\". "
                             "The other marker: %s, resting on items %s; evidence: \"%s\"."
                             % (k, a["key"][k]["verdict"], a["key"][k]["items"], a["key"][k]["evidence"][:600],
                                b["key"][k]["verdict"], b["key"][k]["items"], b["key"][k]["evidence"][:600]))
            else:
                lines.append("- Key error %s, to mark afresh." % k)
        for n in sorted(set(meta["disputed_items"] + meta["drift_items"])):
            if n in meta["disputed_items"]:
                lines.append("- Report item %d, in dispute. One marker: %s. The other marker: %s."
                             % (n, describe_item(a, n), describe_item(b, n)))
            else:
                lines.append("- Report item %d, to mark afresh." % n)
        import s80_run
        user = s80_run.marker_user_text(task, key, info["doc"], rid, C.read(os.path.join(READERS_DIR,
                                        v["tag"] + ".response.txt")))
        user += "\n(D) THE CELLS TO DECIDE\n=======================\n\n" + "\n".join(lines) + "\n"
        C.write(os.path.join(ADJ_DIR, rid + ".md"), user)
        C.write_atomic(os.path.join(ADJ_DIR, rid + ".meta.json"), json.dumps(meta, indent=1))
        n_new += 1
    print("adjudication inputs written: %d; unchanged: %d; folder: %s" % (n_new, n_same, ADJ_DIR))


# ================================================================ counting

def count_report(rid, v, rec, kinds):
    info = C.parse_tag(v["tag"])
    cells = cells_of(rid, v["tag"], info, rec)
    valid = cells["valid_marks"]
    r = dict(rid=rid, tag=v["tag"], **{k: info[k] for k in ("reader", "cond", "method", "thinking", "doc", "rep")},
             markers=list(rec), mark_status={m: e["status"] for m, e in rec.items()}, single_marked=len(valid) == 1,
             counted=len(valid) >= 1, adjudicated_cells=0, unresolved_cells=0, disagreements=[], drift=[],
             adjudication="none-needed")
    if not valid:
        return r
    ids = C.key_ids(info["doc"])
    per_marker = {}
    for m in valid:
        mk = rec[m]["mark"]
        lab = item_labels(mk)
        per_marker[m] = {"HV": sum(mk["key"][k]["verdict"] == "FOUND" for k in ids if kinds[k] == "HV"),
                         "GEN": sum(mk["key"][k]["verdict"] == "FOUND" for k in ids if kinds[k] == "GEN"),
                         "D3": int(mk["key"]["D3"]["verdict"] == "FOUND"),
                         "FA": sum(1 for x in lab.values() if x == "MISTAKEN"),
                         "items": mk["report_items_total"]}
    r["per_marker"] = per_marker
    final_key, final_item = {}, {}
    if len(valid) == 1:
        mk = rec[valid[0]]["mark"]
        for k in ids:
            final_key[k] = "FOUND" if mk["key"][k]["verdict"] == "FOUND" else "NOT"
        for n, x in item_labels(mk).items():
            final_item[n] = "MISTAKEN" if x == "MISTAKEN" else "NOT"
        n_items = mk["report_items_total"]
        partial = sum(mk["key"][k]["verdict"] == "PARTIAL" for k in ids)
        unclear = sum(1 for x in item_labels(mk).values() if x == "UNCLEAR")
    else:
        a, b = rec[valid[0]]["mark"], rec[valid[1]]["mark"]
        meta = adjudication_meta_now(rid, v, rec, cells)
        adj, status = load_adjudication(rid, meta)
        r["adjudication"] = status
        adj_ok = status == "ok"
        final_key.update(cells["agreed_key"])
        final_item.update(cells["agreed_item"])
        for k in cells["disputed_keys"]:
            d = {"cell": k, valid[0]: a["key"][k]["verdict"], valid[1]: b["key"][k]["verdict"]}
            if adj_ok:
                final_key[k] = "FOUND" if adj["key"][k] == "FOUND" else "NOT"
                d["adjudicator"] = adj["key"][k]
                r["adjudicated_cells"] += 1
            else:
                final_key[k] = "UNRESOLVED"
                r["unresolved_cells"] += 1
            r["disagreements"].append(d)
        la, lb = item_labels(a), item_labels(b)
        for n in cells["disputed_items"]:
            d = {"cell": "item %d" % n, valid[0]: la.get(n, "ABSENT"), valid[1]: lb.get(n, "ABSENT")}
            if adj_ok:
                final_item[n] = "MISTAKEN" if adj["items"][n] == "MISTAKEN" else "NOT"
                d["adjudicator"] = adj["items"][n]
                r["adjudicated_cells"] += 1
            else:
                final_item[n] = "UNRESOLVED"
                r["unresolved_cells"] += 1
            r["disagreements"].append(d)
        if adj_ok:
            for k in cells["drift_keys"]:
                r["drift"].append({"cell": k, "kind": kinds[k], "agreed": cells["agreed_key"][k],
                                   "adjudicator": "FOUND" if adj["key"][k] == "FOUND" else "NOT"})
            for n in cells["drift_items"]:
                r["drift"].append({"cell": "item %d" % n, "kind": "item", "agreed": cells["agreed_item"][n],
                                   "adjudicator": "MISTAKEN" if adj["items"][n] == "MISTAKEN" else "NOT"})
        elif status != "none-needed" and cells["drift_keys"] + cells["drift_items"] and \
                not (cells["disputed_keys"] or cells["disputed_items"]):
            r["drift_pending"] = True
        n_items = max(a["report_items_total"], b["report_items_total"])
        partial = sum(1 for k in ids if final_key.get(k) == "NOT" and "PARTIAL" in
                      (a["key"][k]["verdict"], b["key"][k]["verdict"]))
        unclear = sum(1 for n in range(1, n_items + 1) if la.get(n) == "UNCLEAR" and lb.get(n) == "UNCLEAR")
    r.update(HV=sum(final_key[k] == "FOUND" for k in ids if kinds[k] == "HV"),
             GEN=sum(final_key[k] == "FOUND" for k in ids if kinds[k] == "GEN"),
             D3=int(final_key["D3"] == "FOUND"),
             FA=sum(1 for x in final_item.values() if x == "MISTAKEN"), items=n_items,
             PARTIAL=partial, UNCLEAR=unclear, final_key=final_key)
    rc = _json(os.path.join(READERS_DIR, v["tag"] + ".receipt.json")) or {}
    usage = rc.get("usage") or {}
    r.update(completion_tokens=usage.get("completion_tokens"), seconds=rc.get("total_seconds"),
             reasoning_chars=rc.get("reasoning_chars"), response_chars=rc.get("response_chars"))
    return r


# ================================================================ statistics

def _mean(xs):
    return sum(xs) / len(xs) if xs else None


def _stat(sample, kind):
    if kind == "mean":
        return _mean(sample)
    den = sum(d for _, d in sample)
    return (sum(n for n, _ in sample) / den) if den else 0.0


def boot_diff(a, b, kind, name):
    """Difference of condition A minus condition B, with a 95% percentile bootstrap interval; reports resampled with
    replacement within each condition; the generator is seeded from BOOT_SEED and the contrast's name."""
    if not a or not b:
        return None
    est = _stat(a, kind) - _stat(b, kind)
    rng = random.Random("%d|%s" % (C.BOOT_SEED, name))
    ds = sorted(_stat([rng.choice(a) for _ in a], kind) - _stat([rng.choice(b) for _ in b], kind)
                for _ in range(C.BOOT_N))
    lo, hi = ds[int(0.025 * C.BOOT_N)], ds[int(0.975 * C.BOOT_N) - 1]
    return {"est": est, "lo": lo, "hi": hi, "nA": len(a), "nB": len(b)}


def samples(reports, reader, cond, doc, metric):
    rs = [r for r in reports if r["reader"] == reader and r["cond"] == cond and r["doc"] == doc and r["counted"]]
    if metric in ("HV", "GEN", "D3", "FA"):
        return [r[metric] for r in rs], "mean"
    if metric == "FA_per_item":
        return [(r["FA"], r["items"]) for r in rs], "ratio"
    raise ValueError(metric)


METRICS = [("HV", "seeded"), ("GEN", "seeded"), ("D3", "seeded"), ("D3", "clean"), ("FA", "clean"),
           ("FA_per_item", "clean"), ("FA", "seeded"), ("FA_per_item", "seeded")]


def contrasts(reports):
    out = []
    api = [("S-P", "ST", "PT", "on", "decision"), ("S-P", "SO", "PO", "off", "decision"),
           ("S-N", "ST", "NT", "on", "descriptive"), ("S-N", "SO", "NO", "off", "descriptive"),
           ("P-N", "PT", "NT", "on", "descriptive"), ("P-N", "PO", "NO", "off", "descriptive"),
           ("owner ST-NO", "ST", "NO", "-", "descriptive (skill and thinking changed together)"),
           ("thinking, skill", "ST", "SO", "-", "descriptive"), ("thinking, placebo", "PT", "PO", "-", "descriptive"),
           ("thinking, nothing", "NT", "NO", "-", "descriptive")]
    for reader in C.MODELS:
        for label, ca, cb, th, role in api:
            for metric, doc in METRICS:
                a, kind = samples(reports, reader, ca, doc, metric)
                b, _ = samples(reports, reader, cb, doc, metric)
                name = "%s|%s|%s|%s|%s" % (reader, ca, cb, metric, doc)
                out.append(dict(reader=reader, label=label, A=ca, B=cb, thinking=th, role=role, metric=metric,
                                doc=doc, result=boot_diff(a, b, kind, name)))
        # interaction, exploratory: (ST - PT) - (SO - PO) on HV, bootstrapped jointly
        cs = {c: samples(reports, reader, c, "seeded", "HV")[0] for c in ("ST", "PT", "SO", "PO")}
        res = None
        if all(cs.values()):
            rng = random.Random("%d|%s|interaction" % (C.BOOT_SEED, reader))
            f = lambda d: (_mean(d["ST"]) - _mean(d["PT"])) - (_mean(d["SO"]) - _mean(d["PO"]))
            ds = sorted(f({c: [rng.choice(x) for _ in x] for c, x in cs.items()}) for _ in range(C.BOOT_N))
            res = {"est": f(cs), "lo": ds[int(0.025 * C.BOOT_N)], "hi": ds[int(0.975 * C.BOOT_N) - 1]}
        out.append(dict(reader=reader, label="interaction (ST-PT)-(SO-PO)", A="", B="", thinking="-",
                        role="exploratory", metric="HV", doc="seeded", result=res))
    for label, ca, cb in (("S-P", "S", "P"), ("S-N", "S", "N"), ("P-N", "P", "N")):
        for metric, doc in METRICS:
            a, kind = samples(reports, "opus", ca, doc, metric)
            b, _ = samples(reports, "opus", cb, doc, metric)
            out.append(dict(reader="opus", label=label, A=ca, B=cb, thinking="as the agent runs",
                            role="non-voting", metric=metric, doc=doc,
                            result=boot_diff(a, b, kind, "opus|%s|%s|%s|%s" % (ca, cb, metric, doc))))
    return out


def find(cs, reader, A, B, metric, doc):
    for c in cs:
        if (c["reader"], c["A"], c["B"], c["metric"], c["doc"]) == (reader, A, B, metric, doc):
            return c["result"]
    return None


def decide(cs):
    favour_on, lines = [], []
    for r in C.MODELS:
        hv = find(cs, r, "ST", "PT", "HV", "seeded")
        fa = find(cs, r, "ST", "PT", "FA_per_item", "clean")
        fav = bool(hv and hv["lo"] > 0)
        fa_ok = bool(fa is not None and fa["est"] <= FA_RISE_LIMIT)
        lines.append("%s at thinking on: HV skill-placebo %s; clean false alarms per item skill-placebo %s -> %s"
                     % (r, fmt_ci(hv), fmt_ci(fa, 3), "counts for the skill" if fav and fa_ok else
                        ("interval above zero but false alarms rise more than 0.10" if fav else "does not count")))
        if fav and fa_ok:
            favour_on.append(r)
    any_fav = [(r, t, m) for r in C.MODELS for (a, b, t) in (("ST", "PT", "on"), ("SO", "PO", "off"))
               for m in ("HV", "GEN") if (lambda x: x and x["lo"] > 0)(find(cs, r, a, b, m, "seeded"))]
    if len(favour_on) >= 2:
        verdict = "THE SKILL ADDS SOMETHING (readers: %s)" % ", ".join(favour_on)
    elif not any_fav:
        verdict = "ABANDON"
    else:
        verdict = "NO DECISION AT THIS SIZE"
    size = []
    for r in C.MODELS:
        hv = find(cs, r, "ST", "PT", "HV", "seeded")
        if not hv:
            continue
        if hv["est"] <= 0:
            size.append("%s: estimate %.2f is not in the skill's favour; no size decides for the skill at it" % (r, hv["est"]))
        elif hv["lo"] <= 0:
            n = math.ceil(C.REPS * ((hv["est"] - hv["lo"]) / hv["est"]) ** 2) + 1
            size.append("%s: about %d repetitions per cell would put the lower end above zero if the estimate %.2f "
                        "held (half-width scaled by 1/sqrt(n))" % (r, n, hv["est"]))
    return {"verdict": verdict, "readers_counting": favour_on, "favourable_intervals_anywhere": any_fav,
            "lines": lines, "size": size}


# ================================================================ output

def fmt(x, nd=2):
    return "-" if x is None else ("%.*f" % (nd, x))


def fmt_ci(c, nd=2):
    return "n/a" if not c else "%s [%s, %s]" % (fmt(c["est"], nd), fmt(c["lo"], nd), fmt(c["hi"], nd))


def cell_rows(reports):
    rows = []
    conds = [(m, c) for m in C.MODELS for c in C.CONDS] + [("opus", c) for c in C.OPUS_CONDS]
    for reader, cond in conds:
        rs = [r for r in reports if r["reader"] == reader and r["cond"] == cond and r["counted"]]
        sd = [r for r in rs if r["doc"] == "seeded"]
        cl = [r for r in rs if r["doc"] == "clean"]
        ratio = lambda xs: (sum(r["FA"] for r in xs) / sum(r["items"] for r in xs)) if sum(r["items"] for r in xs) else None
        rows.append(dict(reader=reader, cond=cond, n_seeded=len(sd), n_clean=len(cl),
                         HV=_mean([r["HV"] for r in sd]), GEN=_mean([r["GEN"] for r in sd]),
                         D3_seeded=sum(r["D3"] for r in sd), D3_clean=sum(r["D3"] for r in cl),
                         FA_clean=_mean([r["FA"] for r in cl]), FA_item_clean=ratio(cl),
                         FA_seeded=_mean([r["FA"] for r in sd]), FA_item_seeded=ratio(sd),
                         items=_mean([r["items"] for r in rs]), UNCLEAR=sum(r["UNCLEAR"] for r in rs),
                         PARTIAL=sum(r["PARTIAL"] for r in rs), adjudicated=sum(r["adjudicated_cells"] for r in rs),
                         unresolved=sum(r["unresolved_cells"] for r in rs),
                         single=sum(r["single_marked"] for r in rs),
                         tokens=_mean([r["completion_tokens"] for r in rs if r.get("completion_tokens") is not None]),
                         seconds=_mean([r["seconds"] for r in rs if r.get("seconds") is not None])))
    return rows


def tables(key):
    status = completeness()
    mp = C.load_map()
    if not mp:
        raise SystemExit("no MAP.json: nothing has been marked")
    marks = load_marks(mp, key)
    kinds = key["kinds"]
    reports = [count_report(rid, v, marks[rid], kinds) for rid, v in sorted(mp.items())]
    mapped = {v["tag"] for v in mp.values()}
    missing_reports = sorted(t for t in C.expected_tags() if t not in mapped)
    not_counted = [r["tag"] for r in reports if not r["counted"]]
    unresolved = sum(r["unresolved_cells"] for r in reports)
    mark_problems = [(r["rid"], m, e["status"], e.get("problems", [])[:3]) for r in reports
                     for m, e in marks[r["rid"]].items() if e["status"] != "ok"]
    drift_pending = [r["rid"] for r in reports if r.get("drift_pending")]
    # Final when nothing is waiting: no disputed cell unresolved, no drift re-mark pending, no mark missing or stale.
    # A mark that failed or stayed invalid after its one retry leaves its report single-marked (shown), not pending.
    final = unresolved == 0 and not drift_pending and not [p for p in mark_problems if p[2] in ("missing", "stale")]
    cs = contrasts(reports)
    dec = decide(cs)
    rows = cell_rows(reports)

    L = ["# S80 Skill test - tables", ""]
    L.append("Written by `tools/s80_table.py` from the marks, the map and the readers' receipts, under the counting "
             "function and decision rule frozen in plan S80, second version. %s" %
             ("FINAL: every mapped report is marked and every dispute is adjudicated." if final else
              "**PROVISIONAL: %d disputed cells unresolved, %d marks missing or stale, %d reports awaiting a drift "
              "re-mark. The decision is not read from a provisional table.**"
              % (unresolved, len([p for p in mark_problems if p[2] in ("missing", "stale")]), len(drift_pending))))
    L += ["", "## Completeness", "",
          "Expected reports %d; present and complete %d; not mapped for marking %d; mapped but with no valid mark %d."
          % (len(status["tags"]), sum(s == "ok" for s in status["tags"].values()), len(missing_reports),
             len(not_counted)), ""]
    bad = {k: v for k, v in status["per_cell"].items() if set(v) != {"ok"}}
    if bad:
        L += ["| cell | reports |", "|---|---|"] + ["| %s | %s |" % (c, ", ".join("%s %d" % kv for kv in sorted(v.items())))
                                                   for c, v in sorted(bad.items())] + [""]
    if missing_reports:
        L += ["Not in the map (missing or failed): " + ", ".join(missing_reports), ""]
    if mark_problems:
        L += ["Marks not usable:", ""] + ["- %s by %s: %s %s" % (rid, m, s, "; ".join(p)) for rid, m, s, p in mark_problems] + [""]

    L += ["## Agreed table", "",
          "Means per report. HV and GEN: of 4, seeded document. D3: count of reports finding it (seeded, clean). FA: "
          "false alarms (both markers MISTAKEN, or the adjudicator) per report, and per numbered item. UNCLEAR, PARTIAL, "
          "adjudicated, unresolved: counts of cells over the cell's reports. single: reports counted from one mark.", "",
          "| reader | cond | n seeded | n clean | HV | GEN | D3 s | D3 c | FA/report clean | FA/item clean | "
          "FA/report seeded | FA/item seeded | items | UNCLEAR | PARTIAL | adjudicated | unresolved | single | "
          "tokens | seconds |", "|" + "---|" * 20]
    for w in rows:
        L.append("| %s | %s | %d | %d | %s | %s | %d | %d | %s | %s | %s | %s | %s | %d | %d | %d | %d | %d | %s | %s |"
                 % (w["reader"], w["cond"], w["n_seeded"], w["n_clean"], fmt(w["HV"]), fmt(w["GEN"]), w["D3_seeded"],
                    w["D3_clean"], fmt(w["FA_clean"]), fmt(w["FA_item_clean"], 3), fmt(w["FA_seeded"]),
                    fmt(w["FA_item_seeded"], 3), fmt(w["items"], 1), w["UNCLEAR"], w["PARTIAL"], w["adjudicated"],
                    w["unresolved"], w["single"], fmt(w["tokens"], 0), fmt(w["seconds"], 0)))

    L += ["", "## Contrasts, with 95% bootstrap intervals", "",
          "Difference A minus B in the per-report mean (per-item rates: pooled ratio), reports resampled within each "
          "condition, %d resamples. With five reports per condition a percentile interval is narrower than it should be; "
          "read it as a screen, not a test." % C.BOOT_N, "",
          "| reader | contrast | A | B | role | HV | GEN | D3 seeded | FA/report clean | FA/item clean | FA/report seeded | "
          "FA/item seeded |", "|" + "---|" * 12]
    seen = []
    for c in cs:
        k = (c["reader"], c["label"], c["A"], c["B"])
        if k in seen:
            continue
        seen.append(k)
        same = [x for x in cs if (x["reader"], x["label"], x["A"], x["B"]) == k]
        g = lambda m, d, nd=2: fmt_ci(next((x["result"] for x in same if x["metric"] == m and x["doc"] == d), None), nd)
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
                 % (c["reader"], c["label"], c["A"], c["B"], c["role"], g("HV", "seeded"), g("GEN", "seeded"),
                    g("D3", "seeded"), g("FA", "clean"), g("FA_per_item", "clean", 3), g("FA", "seeded"),
                    g("FA_per_item", "seeded", 3)))

    L += ["", "## Decision", "", "**%s**%s" % (dec["verdict"], "" if final else " (provisional: not to be read)"), ""]
    L += ["- " + x for x in dec["lines"]]
    L += ["- favourable intervals anywhere (reader, thinking, kind): %s" % (dec["favourable_intervals_anywhere"] or "none")]
    if dec["size"]:
        L += ["", "What size would decide:", ""] + ["- " + x for x in dec["size"]]
    L += ["", "Scope: these eight planted kinds and one natural error, on this document, for auditing. The HV plants and "
          "the found-rules are the skill author's. The Opus arm does not vote."]

    L += ["", "## Per marker", "", "Each marker's own counts, before agreement (means per report; FA = items the "
          "marker judged MISTAKEN).", "", "| reader | cond | marker | n | HV | GEN | D3 | FA/report clean | FA/report seeded |",
          "|---|---|---|---|---|---|---|---|---|"]
    for reader, cond in [(m, c) for m in C.MODELS for c in C.CONDS] + [("opus", c) for c in C.OPUS_CONDS]:
        for mk in C.MARKERS_FOR[reader]:
            rs = [r for r in reports if r["reader"] == reader and r["cond"] == cond and mk in r.get("per_marker", {})]
            sd = [r["per_marker"][mk] for r in rs if r["doc"] == "seeded"]
            cl = [r["per_marker"][mk] for r in rs if r["doc"] == "clean"]
            L.append("| %s | %s | %s | %d | %s | %s | %d | %s | %s |"
                     % (reader, cond, mk, len(rs), fmt(_mean([x["HV"] for x in sd])), fmt(_mean([x["GEN"] for x in sd])),
                        sum(x["D3"] for x in sd + cl), fmt(_mean([x["FA"] for x in cl])), fmt(_mean([x["FA"] for x in sd]))))

    L += ["", "## Disagreements", "", "| rid | tag | cell | marks | adjudicator |", "|---|---|---|---|---|"]
    for r in reports:
        for d in r["disagreements"]:
            ms = ", ".join("%s %s" % (k, v) for k, v in d.items() if k not in ("cell", "adjudicator"))
            L.append("| %s | %s | %s | %s | %s |" % (r["rid"], r["tag"], d["cell"], ms, d.get("adjudicator", "pending")))

    drift = [dict(d, method=r["method"], reader=r["reader"]) for r in reports for d in r["drift"]]
    L += ["", "## Drift check", "", "The adjudicator's fresh verdicts on agreed cells chosen by the fixed hash rule. "
          "Counts are not changed by it.", ""]
    if drift:
        L += ["| method | kind | cells | adjudicator agrees |", "|---|---|---|---|"]
        for meth in ("S", "P", "N"):
            for kind in ("HV", "GEN", "REAL", "item"):
                ds = [d for d in drift if d["method"] == meth and d["kind"] == kind]
                if ds:
                    L.append("| %s | %s | %d | %.2f |" % (meth, kind, len(ds),
                                                         sum(d["agreed"] == d["adjudicator"] for d in ds) / len(ds)))
    else:
        L.append("No drift re-marks yet.")

    L += ["", "## Per repetition", "", "| tag | rid | markers | HV | GEN | D3 | FA | items | UNCLEAR | PARTIAL | "
          "adjudicated | unresolved |", "|" + "---|" * 12]
    for r in sorted(reports, key=lambda r: r["tag"]):
        if not r["counted"]:
            L.append("| %s | %s | %s | not counted | | | | | | | | |" % (r["tag"], r["rid"], r["mark_status"]))
            continue
        L.append("| %s | %s | %s%s | %d | %d | %d | %d | %d | %d | %d | %d | %d |"
                 % (r["tag"], r["rid"], "+".join(r["markers"]), " (single)" if r["single_marked"] else "",
                    r["HV"], r["GEN"], r["D3"], r["FA"], r["items"], r["UNCLEAR"], r["PARTIAL"],
                    r["adjudicated_cells"], r["unresolved_cells"]))

    C.write_atomic(os.path.join(C.OUT, "TABLES.md"), "\n".join(L) + "\n")
    C.write_atomic(os.path.join(C.OUT, "TABLES.json"), json.dumps(
        {"final": final, "decision": dec, "cells": rows, "contrasts": cs, "completeness": status,
         "missing_reports": missing_reports, "mark_problems": mark_problems,
         "reports": [{k: v for k, v in r.items()} for r in reports]}, indent=1, default=str))
    print("wrote", os.path.join(C.OUT, "TABLES.md"), "(FINAL)" if final else "(PROVISIONAL)", "-", dec["verdict"])


def main(a):
    if not a:
        raise SystemExit(__doc__)
    test_key = "--test-key" in a
    if test_key and os.path.abspath(C.OUT) == os.path.abspath(C.REAL_OUT):
        raise SystemExit("--test-key is for a synthetic output root only")
    if a[0] == "check":
        st = completeness()
        print_failures(st)
        raise SystemExit(0 if all(s == "ok" for s in st["tags"].values()) and not st["unexpected"] else 1)
    key = C.load_key(a[1], check_sha=not test_key)
    if a[0] == "adjudicate":
        adjudicate(key)
    elif a[0] == "tables":
        tables(key)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
