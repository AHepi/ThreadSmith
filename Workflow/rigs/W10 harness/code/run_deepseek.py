"""DRIVER. Runs the arms of W10 section 4 on DeepSeek V4.1 Flash.

  DEEPSEEK_API_KEY=... python3 run_deepseek.py --arms a,b --docs W01 --repeats 1,2,3 --texts DIR
  python3 run_deepseek.py --dry --arms all --docs W01 --texts code/fixtures/dryrun   # sends nothing

What a dry run checks (W10 prediction W10.1): that every arm named can be built on the document
named, from the manifest to the last call; that the skill copy is file 33 exactly; that the
frozen question renders and, for arm (f), that no sentence of the withheld change list is
anywhere in the prompt; that arm (x)'s two names were both really exchanged; that arm (d)'s
parts pass yields a parts list that can be split and does not leak cross-step material; that
every request body is well formed and carries no key. It writes every request it would have
sent under <rig>/dry/deepseek/<run>/ and sends nothing.

Run naming: <document>-<arm>-r<repeat>.json under <rig>/runs/deepseek/, with one folder of
calls per run under <rig>/calls/deepseek/<run>/, each call saved twice: NN-step.request.json
(the body as sent, PA.1) and NN-step.reply.json (the reply as returned). Resumable: a run whose
file exists is skipped; inside a run, a call whose reply file exists is reused and not resent.

Every module the tool loop serves is recorded by the rig (`modules_served`), never by the
reader; the reader's own mention of modules is kept apart as `modules_self_reported`
(W8 part C4, prediction P4.9).
"""
import os, sys, json, time, argparse, concurrent.futures as cf

import rig, skillcheck, corpus, question, arms, summariser, carryover, partition, exchange
import deepseek_transport as T
from rig import RUNS, CALLS, RIG, MODULES, write_json, write_text, read_json, run_id, stamp
from steps import STEP_ORDER, TEST_IDS

READER = "deepseek"
DRY_REPLIES = None


def dry_reply(step):
    global DRY_REPLIES
    if DRY_REPLIES is None:
        DRY_REPLIES = read_json(os.path.join(rig.FIXTURES, "dry_replies.json"))
    return DRY_REPLIES.get(step, "(dry run: no reply)")


def self_reported_modules(text):
    low = (text or "").lower()
    return [m for m in MODULES if m in low]


class Run:
    def __init__(self, row, text, arm, repeat, opts):
        self.row, self.arm, self.repeat, self.opts = row, arm, repeat, opts
        self.doc = row["id"]
        self.rid = run_id(self.doc, arm, repeat)
        self.cfg = arms.ARMS[arm]
        self.dir = os.path.join(CALLS, READER, self.rid)
        self.out = os.path.join(RUNS, READER, self.rid + ".json")
        if opts.dry:
            self.dir = os.path.join(RIG, "dry", READER, self.rid)
        self.exchange_rec = None
        if self.cfg["document"] == "exchanged":
            text, self.exchange_rec = exchange.for_document(row, text)
            if self.exchange_rec["void"]:
                raise SystemExit(f"{self.rid}: arm (x) replaced one of the two names zero times. Nothing sent.")
        self.text = text
        self.q = question.for_document(row)
        self.with_cl = self.cfg["question"] != "no_change_list"
        self.qblock = question.render(self.q, self.with_cl)
        self.skill_md = skillcheck.skill_main()
        self.removed = []
        if self.cfg["skill_variant"]:
            self.skill_md, self.removed = arms.skill_variant(self.skill_md, self.cfg["skill_variant"])
        self.sys = arms.system_message(arm, "deepseek", self.skill_md)
        if not self.with_cl:
            question.check_withheld(self.sys + self.text, self.q)
        self.skeleton = None
        if self.cfg["prefix"]:
            self.skeleton = arms.fixture("report_skeleton.md")
        self.calls, self.usages, self.modules, self.replies = [], [], [], {}
        self.requests = 0
        self.tool_loop_requests = 0

    # ---------- one request, saved as sent and as returned ----------
    def one(self, n, step, messages, prefix_text=None, label=""):
        digests = skillcheck.check()          # before every call, not once a batch (Lesson 44)
        msgs = list(messages)
        if prefix_text is not None:
            msgs = msgs + [{"role": "assistant", "content": prefix_text, "prefix": True}]
        body = T.body_for(msgs, tools=(arms.TOOL if self.opts.router else None),
                          prefix=bool(prefix_text), max_tokens=self.opts.max_tokens,
                          effort=self.opts.effort, model=self.opts.model,
                          stream=self.opts.stream)
        base = os.path.join(self.dir, f"{n:02d}-{step}{label}")
        if not self.opts.dry and os.path.exists(base + ".reply.json"):
            # a call already made: the saved request is the one that was sent and is not rewritten
            saved = read_json(base + ".reply.json")
            self.calls.append({"n": n, "step": step, "request": base + ".request.json",
                               "reply": base + ".reply.json", "reused": True,
                               "tool_loop": bool(label)})
            self.usages.append(saved.get("usage") or {})
            self.requests += 1
            return saved["message"], saved.get("finish"), saved.get("usage") or {}
        req = {"run": self.rid, "arm": self.arm, "step": step, "n": n,
               "endpoint": body["_endpoint"], "client": T.CLIENT,
               "skill_digests": digests, "sent_at": stamp(), "body": T._strip(body)}
        write_json(base + ".request.json", req)
        if self.opts.dry:
            rep = {"dry": True, "reply": dry_reply(step)}
            write_json(base + ".reply.json", rep)
            self.requests += 1
            self.calls.append({"n": n, "step": step, "request": base + ".request.json",
                               "reply": base + ".reply.json", "dry": True,
                               "tool_loop": bool(label)})
            return {"content": rep["reply"], "reasoning_content": "", "tool_calls": None}, "stop", {}
        msg, finish, usage, http = T.send(body, self.opts.key, tag=f"{self.rid}:{step}",
                                          stream_path=(base + ".stream.txt") if self.opts.stream else None)
        write_json(base + ".reply.json", {"run": self.rid, "step": step, "returned_at": stamp(),
                                          "message": msg, "finish": finish, "usage": usage,
                                          "http": http if isinstance(http, dict) else str(http)})
        self.usages.append(usage or {})
        self.requests += 1
        self.calls.append({"n": n, "step": step, "request": base + ".request.json",
                           "reply": base + ".reply.json", "finish": finish,
                           "usage": usage, "endpoint": body["_endpoint"],
                           "tool_loop": bool(label)})
        return msg, finish, usage

    def turn(self, n, step, messages, prefix_text=None):
        """One step: the request, then the tool loop the rig serves, then the text."""
        msg, finish, _ = self.one(n, step, messages, prefix_text)
        served, i = 0, 0
        while self.opts.router and (msg.get("tool_calls") or []) and served < self.opts.max_tools:
            messages = list(messages) + [{"role": "assistant", "content": msg.get("content") or "",
                                          "tool_calls": msg["tool_calls"]}]
            for tc in msg["tool_calls"]:
                served += 1
                try:
                    name = json.loads(tc["function"]["arguments"]).get("name", "")
                except Exception:
                    name = ""
                self.modules.append(name or "?")
                messages.append({"role": "tool", "tool_call_id": tc["id"],
                                 "content": skillcheck.module_text(name)})
            i += 1
            self.tool_loop_requests += 1
            msg, finish, _ = self.one(n, step, messages, prefix_text, label=f"-t{i}")
        text = msg.get("content") or ""
        if prefix_text is not None:
            text = prefix_text + text
        return text, messages, finish

    # ---------- the arms ----------
    def go(self):
        t0 = time.time()
        cfg, rec_extra = self.cfg, {}
        if cfg["partition"]:
            rec_extra = self.arm_d()
        elif cfg["carrier"] == "own":
            rec_extra = self.arm_own()
        else:
            rec_extra = self.arm_carried()
        report = self.replies.get("S67") or self.replies.get("SASM") or self.replies.get("ALL") or ""
        rec = {"run_id": self.rid, "reader": READER, "arm": self.arm, "arm_title": cfg["title"],
               "document": self.doc, "repeat": self.repeat, "dry": self.opts.dry,
               "model": self.opts.model, "effort": self.opts.effort, "stream": self.opts.stream,
               "max_tokens": self.opts.max_tokens, "client": T.CLIENT,
               "skill_file": rig.SKILL_FILE, "skill_digests": skillcheck.check(),
               "skill_variant": ({"kind": cfg["skill_variant"], "removed_lines": self.removed}
                                 if cfg["skill_variant"] else None),
               "question": question.identity(self.q, self.with_cl), "question_as_sent": self.qblock,
               "change_list_withheld": not self.with_cl,
               "router_live": self.opts.router, "modules_served": self.modules,
               "modules_served_by": "the rig's tool loop, not the reader",
               "modules_self_reported": self_reported_modules(report),
               "modules_self_reported_by": "module names found in the reader's own report text",
               "requests": self.requests, "tool_loop_requests": self.tool_loop_requests,
               "steps": len([c for c in self.calls if not c.get("tool_loop")]),
               "calls": self.calls, "step_replies": self.replies, "report": report,
               "prefix_used": bool(self.skeleton), "prefix_text": self.skeleton,
               "reply_includes_prefix": bool(self.skeleton),
               "exchange": self.exchange_rec,
               "usage_total": {k: sum(u.get(k, 0) for u in self.usages)
                               for k in ("prompt_tokens", "completion_tokens",
                                         "prompt_cache_hit_tokens", "prompt_cache_miss_tokens",
                                         "total_tokens")},
               "seconds": round(time.time() - t0, 1), "finished_at": stamp()}
        rec.update(rec_extra)
        rec["pa1_requests_minus_tool_loop"] = self.requests - self.tool_loop_requests
        write_json(self.out if not self.opts.dry else os.path.join(self.dir, "run.json"), rec)
        return rec

    def arm_own(self):
        """Arms a, e, f, r, x, k: one conversation, the five steps as five turns."""
        messages = [{"role": "system", "content": self.sys}]
        for n, step in enumerate(STEP_ORDER, 1):
            pre = self.skeleton if (self.cfg["prefix"] and step == "S67") else None
            user = arms.user_message(self.arm, step, self.text, self.qblock)
            messages = messages + [{"role": "user", "content": user}]
            text, messages, _ = self.turn(n, step, messages, pre)
            self.replies[step] = text
            messages = messages + [{"role": "assistant", "content": text}]
        return {}

    def arm_carried(self):
        """Arms b, c, cctl, cprime: a fresh conversation per step, with a carrier."""
        notes, sums = [], []
        for n, step in enumerate(STEP_ORDER, 1):
            carrier = None
            if self.cfg["carrier"] == "transcript" and self.replies:
                carrier = "\n\n".join(f"### {s}\n{self.replies[s]}" for s in STEP_ORDER if s in self.replies)
            elif self.cfg["carrier"] in ("summary", "summary_control") and self.replies:
                (full, rf), (ctl, rc) = summariser.pair(self.replies)
                carrier = full if self.cfg["carrier"] == "summary" else ctl
                sums.append({"step": step, "record": rf if self.cfg["carrier"] == "summary" else rc,
                             "text": carrier})
            elif self.cfg["carrier"] == "carryover" and self.replies:
                carrier = notes[-1]["note"] if notes and notes[-1]["note"] else None
            user = arms.user_message(self.arm, step, self.text, self.qblock, carrier_text=carrier)
            messages = [{"role": "system", "content": self.sys}, {"role": "user", "content": user}]
            text, _, _ = self.turn(n, step, messages)
            if self.cfg["carrier"] == "carryover" and step != STEP_ORDER[-1]:
                note, nrec = carryover.extract(text)      # no note is asked at the last step
                nrec.update({"step": step, "note": note})
                notes.append(nrec)
                self.replies[step] = carryover.strip_note(text)
            else:
                self.replies[step] = text
        out = {}
        if sums:
            out["summaries"] = sums
        if notes:
            out["carry_over_notes"] = notes
        return out

    def arm_d(self):
        """Arm (d): the parts pass, then one call per test per group, then the assembler."""
        user = arms.user_message(self.arm, "S1234", self.text, self.qblock)
        text, _, _ = self.turn(1, "S1234", [{"role": "system", "content": self.sys},
                                            {"role": "user", "content": user}])
        self.replies["S1234"] = text
        leaks = partition.leak_check(text)
        parts = partition.parse_parts(text)
        plan = partition.calls(parts, TEST_IDS, g=self.opts.groups, mode=self.opts.split)
        answers = []
        for n, (test, gi, grp) in enumerate(plan, 2):
            user = arms.user_message(self.arm, "SONE", self.text, self.qblock,
                                     test=test, group_text=partition.render_group(grp))
            t, _, _ = self.turn(n, f"SONE-{test}-g{gi}", [{"role": "system", "content": self.sys},
                                                          {"role": "user", "content": user}])
            answers.append((test, gi, grp, t))
        user = arms.user_message(self.arm, "SASM", self.text, self.qblock,
                                 pile_text=partition.pile(answers))
        t, _, _ = self.turn(len(plan) + 2, "SASM", [{"role": "system", "content": self.sys},
                                                    {"role": "user", "content": user}])
        self.replies["SASM"] = t
        return {"partition": {"parts": parts, "n_parts": len(parts), "groups": self.opts.groups,
                              "split_mode": self.opts.split, "test_calls": len(plan),
                              "parts_pass_leaks": leaks,
                              "leak_gauge": "lines of the parts pass carrying cross-step material; "
                                            "a run with any is reported, never silently counted"}}


def jobs(opts, rows):
    if opts.docs:
        docs = opts.docs
    else:
        sp = corpus.split(opts.split_file, rows)
        print(f"  the split comes from {sp['from']}: {len(sp['arms'])} for the arms, "
              f"{len(sp['reserve'])} in reserve")
        docs = sp["arms"]
    armlist = arms.ARM_IDS if opts.arms == ["all"] else opts.arms
    for a in armlist:
        if a not in arms.ARMS:
            raise SystemExit(f"unknown arm {a!r}; the arms are {', '.join(arms.ARM_IDS)}")
    out = []
    for d in docs:
        if d not in rows:
            raise SystemExit(f"{d} is not in the manifest. Nothing sent.")
        for a in armlist:
            if a == "x" and not corpus.names(rows[d]):
                print(f"  {d}: no two names in the manifest; arm (x) skipped", file=sys.stderr)
                continue
            for k in opts.repeats:
                out.append((d, a, k))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--arms", default="all")
    p.add_argument("--docs", default="")
    p.add_argument("--repeats", default="1,2,3")
    p.add_argument("--texts", default=None)
    p.add_argument("--sources", default=None)
    p.add_argument("--split-file", dest="split_file", default=None)
    p.add_argument("--groups", type=int, default=2)
    p.add_argument("--split", default="cross", choices=["cross", "rotate"])
    p.add_argument("--workers", type=int, default=5)
    p.add_argument("--max-tokens", dest="max_tokens", type=int, default=T.MAX_TOKENS)
    p.add_argument("--max-tools", dest="max_tools", type=int, default=12)
    p.add_argument("--model", default=T.MODEL)
    p.add_argument("--effort", default=T.EFFORT)
    p.add_argument("--no-router", dest="router", action="store_false", default=True)
    p.add_argument("--no-stream", dest="stream", action="store_false", default=True)
    p.add_argument("--dry", action="store_true")
    p.add_argument("--force", action="store_true")
    o = p.parse_args()
    o.arms = [a.strip() for a in o.arms.split(",") if a.strip()]
    o.docs = [d.strip() for d in o.docs.split(",") if d.strip()]
    o.repeats = [int(k) for k in o.repeats.split(",") if k.strip()]
    o.key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not o.key and not o.dry:
        raise SystemExit("DEEPSEEK_API_KEY not set. Nothing sent.")
    tdir = corpus.texts_dir(sys.argv)
    rows = corpus.manifest(o.sources)
    d = skillcheck.check()
    print(f"skill copy checked against HV file {rig.SKILL_FILE}: {len(d)} files identical")
    js = jobs(o, rows)
    print(f"{len(js)} runs; model {o.model}, effort {o.effort}, client {T.CLIENT}, "
          f"{'DRY - nothing will be sent' if o.dry else f'{o.workers} threads'}")

    def one(doc, arm, k):
        r = Run(rows[doc], corpus.document(doc, tdir, rows[doc])[0], arm, k, o)
        if not o.dry and os.path.exists(r.out) and not o.force:
            return "skip"
        rec = r.go()
        return (f"{rec['requests']} requests ({rec['tool_loop_requests']} of them tool-loop), "
                f"{len(rec['report'].split())} words, modules {rec['modules_served']}")

    if o.dry:
        for doc, arm, k in js:
            print(f"  {run_id(doc, arm, k)}: {one(doc, arm, k)}")
        print("dry run: nothing sent. The requests that would have been sent are under "
              f"{os.path.join(RIG, 'dry', READER)}")
        return
    done = 0
    with cf.ThreadPoolExecutor(max_workers=o.workers) as ex:
        futs = {ex.submit(one, d_, a_, k_): (d_, a_, k_) for d_, a_, k_ in js}
        for f in cf.as_completed(futs):
            d_, a_, k_ = futs[f]
            done += 1
            print(f"  [{done}/{len(js)}] {run_id(d_, a_, k_)}: {f.result()}", flush=True)
    us = []
    for fn in sorted(os.listdir(os.path.join(RUNS, READER))):
        if fn.endswith(".json"):
            us.append(read_json(os.path.join(RUNS, READER, fn)).get("usage_total", {}))
    h, mi, ot, usd = T.cost(us)
    print(f"\ntokens: cache-hit {h:,}, cache-miss {mi:,}, out {ot:,} -> about ${usd:.2f} at the old rig's off-peak prices")


if __name__ == "__main__":
    main()
