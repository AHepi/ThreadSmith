"""DRIVER. Wraps the Sonnet transport's replies into run records of the same shape as the
DeepSeek ones, so that one marker and one agreement program read both.

  python3 wrap_sonnet.py --scratch DIR [--runs W01-b-r1,...] [--dry]

It sends nothing and calls no model. It reads, per call:
  <scratch>/w10/replies/<run>/<call>.md    the reader's answer
  <scratch>/w10/meta/<run>/<call>.json     the transport's own record of that call, written by
                                           the workflow script, not by the reader:
                                           {"tool_calls": [...], "modules_read": [...],
                                            "requests": n, "model": "...", "seconds": n}
  <scratch>/w10/plan/<run>.json            the run's plan record, written by sonnet_prompts.py:
                                           the question identity, the question as sent, the
                                           change-list flag, arm (x)'s exchange and arm (k)'s
                                           skill variant. Copied into the run record here
                                           (fault 13); a run with no plan record says so in
                                           plan_record_missing and carries none of the five.
A missing meta file is not filled in: the run record says `meta_missing` for that call and the
modules-served list for the run is marked incomplete. W8 part C4: "in the transport phase 4 will
use, the modules-opened field is the reader's own report"; this rig keeps the two apart and
P4.9 is the count of runs where they differ. What the reader says it opened is A4's marked field
`modules_self_reported`; this file writes no field of that name, only the raw aid
`modules_named_in_report` (fault 11).
"""
import os, sys, json, argparse, re
import rig, skillcheck, partition
from rig import RIG, RUNS, MODULES, write_json, read_json, stamp
import arms

READER = "sonnet"

PLAN_FIELDS = ["question", "question_as_sent", "change_list_withheld", "exchange", "skill_variant"]


def modules_named_in_report(text):
    """A raw aid, not a field: a substring sweep that fires on ordinary English. See
    run_deepseek.modules_named_in_report."""
    low = (text or "").lower()
    return [m for m in MODULES if m in low]


def wrap_one(b, rid):
    pdir, rdir, mdir = (os.path.join(b, d, rid) for d in ("prompts", "replies", "meta"))
    calls = sorted(f[:-4] for f in os.listdir(pdir) if f.endswith(".txt"))
    doc, arm, k = rig.parse_run_id(rid)
    cfg = arms.ARMS[arm]
    recs, replies, served, missing, requests = [], {}, [], [], 0
    for c in calls:
        rp, mp = os.path.join(rdir, c + ".md"), os.path.join(mdir, c + ".json")
        text = open(rp, encoding="utf-8").read() if os.path.exists(rp) else None
        meta = read_json(mp) if os.path.exists(mp) else None
        if meta is None:
            missing.append(c)
        else:
            served += list(meta.get("modules_read") or [])
            requests += int(meta.get("requests") or 1)
        recs.append({"call": c, "step": c.split("-", 1)[1], "prompt": os.path.join(pdir, c + ".txt"),
                     "reply": rp, "reply_missing": text is None,
                     "meta": mp if meta else None, "meta_missing": meta is None,
                     "tool_calls": (meta or {}).get("tool_calls"),
                     "requests": (meta or {}).get("requests")})
        if text is not None:
            replies[c] = text
    last = calls[-1] if calls else None
    report = replies.get(last, "")
    rec = {"run_id": rid, "reader": READER, "arm": arm, "arm_title": cfg["title"],
           "document": doc, "repeat": k,
           "model": "sonnet (Claude Code subagent transport; the model is the workflow's, not verified here)",
           "transport": "claude-code-subagent", "effort": "high",
           "skill_file": rig.SKILL_FILE, "skill_digests": skillcheck.check(),
           "router_live": True,
           "modules_served": served, "modules_served_by": "the transport's record of tool calls (meta)",
           "modules_served_incomplete": bool(missing), "meta_missing_for": missing,
           "modules_named_in_report": modules_named_in_report(report),
           "modules_named_in_report_by": ("a substring sweep of the answer text for the seven file "
                                          "names; a raw aid, not a field. It fires on ordinary "
                                          "English. A4's marked modules_self_reported is the "
                                          "field, and P4.9 is read over that"),
           "derivation3_qualification_sent": rig.DERIVATION3_QUALIFICATION_SENT,
           "derivation3_qualification_reason": rig.DERIVATION3_REASON,
           "calls": recs, "step_replies": replies, "report": report,
           "requests": requests or len(calls),
           "requests_are": ("calls this rig served. A request the subagent made inside a call is "
                            "not observable from outside it: the tool loop inside a call was not "
                            "observed, and this count does not include it. So PA.1's count of "
                            "requests per step is not readable on this transport and is readable "
                            "on DeepSeek, and the arm (a) half of PA.1 is not reached here "
                            "(W11 decision D2)"),
           "tool_loop_requests": None,
           "tool_loop_requests_are": ("not observed on this transport; None, never zero, so no "
                                      "count reads a request that was not seen as a request that "
                                      "was not made"),
           "steps": len(calls),
           "prefix_used": False,
           "port_set": False if cfg["prefix"] else None,
           "port_note": ("arm (e) on this transport is the control: the skeleton is named in the "
                         "context and sets no emission port (W8 part B10, W10 section 10)"
                         if cfg["prefix"] else None),
           "finished_at": stamp()}
    pr = os.path.join(b, "plan", rid + ".json")
    plan = read_json(pr) if os.path.exists(pr) else None
    rec["plan_record"] = pr if plan else None
    rec["plan_record_missing"] = plan is None
    for f in PLAN_FIELDS:
        rec[f] = (plan or {}).get(f)
    if cfg["partition"]:
        pp = replies.get("01-S1234", "")
        parts = partition.parse_parts(pp)
        leaks = partition.leak_check(pp)
        rec["partition"] = {"parts": parts, "n_parts": len(parts),
                            "test_calls": len([c for c in calls if "SONE" in c]),
                            "parts_pass_leaks": leaks}
        partition.gate(leaks, rid)      # a leaking parts pass is not counted (fault 10)
    return rec


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scratch", default=os.environ.get("W10_SCRATCH", ""))
    p.add_argument("--runs", default="")
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    b = os.path.join(o.scratch, "w10") if not o.dry else os.path.join(RIG, "dry", READER)
    pdir = os.path.join(b, "prompts")
    if not os.path.isdir(pdir):
        raise SystemExit(f"no prompts at {pdir}; run sonnet_prompts.py plan first.")
    rids = [r.strip() for r in o.runs.split(",") if r.strip()] or sorted(os.listdir(pdir))
    written, stopped = 0, []
    for rid in rids:
        try:
            rec = wrap_one(b, rid)
        except partition.Leak as e:
            # no run record is written, so nothing marks it; what was flagged is written beside it
            write_json(os.path.join(b, "stopped", rid + ".json"),
                       {"run_id": rid, "reader": READER, "stopped_because": str(e),
                        "stopped_at": stamp()})
            stopped.append(rid)
            print(f"  {rid}: STOPPED: {e}")
            continue
        out = os.path.join(RUNS, READER, rid + ".json") if not o.dry else os.path.join(b, "runs", rid + ".json")
        write_json(out, rec)
        written += 1
        print(f"  {rid}: {len(rec['calls'])} calls, {len(rec['report'].split())} words in the last answer, "
              f"modules served {rec['modules_served']}"
              + (", NO PLAN RECORD" if rec["plan_record_missing"] else "")
              + (f", meta missing for {len(rec['meta_missing_for'])} call(s)" if rec["meta_missing_for"] else ""))
    print(f"{written} run record(s) written" + (" (dry)" if o.dry else "")
          + (f"; {len(stopped)} run(s) stopped and not counted: {stopped}" if stopped else ""))


if __name__ == "__main__":
    main()
