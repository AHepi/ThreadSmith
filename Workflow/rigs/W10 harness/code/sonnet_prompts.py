"""DRIVER. The prompt files for the Sonnet subagent transport, one file per call, with a JSON
"next step" interface a workflow script can drive.

  python3 sonnet_prompts.py plan   --scratch DIR --arms all --docs W01 --repeats 1,2,3 --texts DIR
  python3 sonnet_prompts.py next   --scratch DIR --run W01-b-r1        # prints one JSON line
  python3 sonnet_prompts.py status --scratch DIR
  python3 sonnet_prompts.py plan --dry --arms all --docs DRY1 --texts code/fixtures/dryrun \
        --sources code/fixtures/sources.example.json                    # sends nothing, writes every prompt

How a workflow script uses it. `plan` writes <scratch>/w10/plan.json and copies the skill.
Then, per run, in a loop: call `next`; if `done` is false, start one Sonnet subagent whose whole
instruction is the file at `prompt` and which writes its answer to `reply` with Write, once;
then write the transport's own record of that subagent's tool calls to `meta` as
{"tool_calls": [...], "modules_read": [...], "requests": n}; then call `next` again. The rig
never asks the reader what it opened: W8 part C4 says the reader's own list is the reader's
report, and P4.9 compares the two. `modules_read` must come from the session's record of tool
calls; what the reader says in its answer is A4's marked field, filled by a marker.

Every run also gets a plan record at `<scratch>/w10/plan/<run>.json`, written whenever `plan` or
`next` builds the run: the question identity, the question as sent, the change-list flag, arm
(x)'s exchange record and arm (k)'s skill variant, which `wrap_sonnet.py` copies into the run
record (fault 13 of the stage-A review; W10 section 4 requires the question-identity field on
every run, and PA.3 needs the exchange counts).

What the Sonnet transport cannot do, said plainly:
 - It cannot prefill an emission. Arm (e) here is the control W10 section 10 names: the skeleton
   is placed in the context and the reader is told to fill it, which W8 part B10 says is naming
   a list and not setting a port. The run record says `port_set: false`.
 - It cannot show how many requests one subagent made. `requests` in the run record is the
   number of calls this rig served, and PA.1's count of requests per step is not readable on
   this transport; it is readable on DeepSeek. wrap_sonnet.py records that in every run.
 - Arm (a) here is one subagent working through the five steps in order inside one session,
   so it differs from arm (b) in the carriage only, as nearly as this transport allows; it can
   still revise an earlier step, which arm (b) cannot. That difference is named and not removed.
"""
import os, sys, json, shutil, argparse
import rig, skillcheck, corpus, question, arms, summariser, carryover, partition, exchange
from rig import RIG, write_json, write_text, read_json, run_id, stamp
from steps import STEP_ORDER, TEST_IDS

READER = "sonnet"


def base(scratch):
    return os.path.join(scratch, "w10")


class SonnetRun:
    def __init__(self, row, text, arm, repeat, opts):
        self.row, self.arm, self.repeat, self.opts = row, arm, repeat, opts
        self.doc = row["id"]
        self.rid = run_id(self.doc, arm, repeat)
        self.cfg = arms.ARMS[arm]
        self.b = base(opts.scratch) if not opts.dry else os.path.join(RIG, "dry", READER)
        self.prompts = os.path.join(self.b, "prompts", self.rid)
        self.replies = os.path.join(self.b, "replies", self.rid)
        self.meta = os.path.join(self.b, "meta", self.rid)
        self.refs = os.path.join(self.b, "hard-to-vary", "references")
        self.exchange_rec = None
        if self.cfg["document"] == "exchanged":
            text, self.exchange_rec = exchange.for_document(row, text)
            if self.exchange_rec["void"]:
                raise SystemExit(f"{self.rid}: arm (x) replaced one of the two names zero times.")
        self.text = text
        # arm (x): the frozen question quotes the document the reader was handed (fault 8)
        self.q = question.for_document(row, exchanged=(self.cfg["document"] == "exchanged"))
        self.with_cl = self.cfg["question"] != "no_change_list"
        self.qblock = question.render(self.q, self.with_cl)
        skill_md = skillcheck.skill_main()
        self.removed = {"table_rows": [], "graph_lines": [], "sentences": []}
        if self.cfg["skill_variant"]:
            skill_md, self.removed = arms.skill_variant(skill_md, self.cfg["skill_variant"])
        self.sys = arms.system_message(arm, "sonnet", skill_md, refs_dir=self.refs)
        if not self.with_cl:
            question.check_withheld(self.sys + self.text, self.q)
        self.skeleton = arms.fixture("report_skeleton.md") if self.cfg["prefix"] else None

    # ---------- the ordered calls of this run, as far as they are known ----------
    def reply_of(self, call):
        p = os.path.join(self.replies, call + ".md")
        if self.opts.dry:
            from run_deepseek import dry_reply
            return dry_reply(call.split("-", 1)[1].split("-")[0])
        return open(p, encoding="utf-8").read() if os.path.exists(p) else None

    def call_list(self):
        if not self.cfg["partition"]:
            return [f"{i:02d}-{s}" for i, s in enumerate(arms.steps_for(self.arm, "sonnet"), 1)]
        got = self.reply_of("01-S1234")
        if got is None:
            return ["01-S1234"]
        # a parts pass carrying cross-step material stops this run (fault 10)
        partition.gate(partition.leak_check(got), self.rid)
        parts = partition.parse_parts(got)
        plan = partition.calls(parts, TEST_IDS, g=self.opts.groups, mode=self.opts.split)
        out = ["01-S1234"] + [f"{i:02d}-SONE-{t}-g{gi}" for i, (t, gi, _) in enumerate(plan, 2)]
        return out + [f"{len(plan) + 2:02d}-SASM"]

    # ---------- one prompt ----------
    def build(self, call):
        step = call.split("-", 1)[1]
        done = {}
        for c in self.call_list():
            if c == call:
                break
            r = self.reply_of(c)
            if r is not None:
                done[c] = r
        carrier, extra = None, {}
        if self.cfg["carrier"] == "transcript" and done:
            carrier = "\n\n".join(f"### {c}\n{t}" for c, t in done.items())
        elif self.cfg["carrier"] in ("summary", "summary_control") and done:
            byst = {c.split("-", 1)[1]: t for c, t in done.items()}
            (full, rf), (ctl, rc) = summariser.pair(byst)
            carrier = full if self.cfg["carrier"] == "summary" else ctl
            extra["summary_record"] = rf if self.cfg["carrier"] == "summary" else rc
        elif self.cfg["carrier"] == "carryover" and done:
            last = list(done.values())[-1]
            note, nrec = carryover.extract(last)
            carrier, extra["carry_over_note"] = note, nrec
        test = group_text = pile_text = None
        ustep = step
        if step.startswith("SONE"):
            ustep = "SONE"
            test = step.split("-")[1]
            gi = int(step.split("-g")[1])
            parts = partition.parse_parts(self.reply_of("01-S1234") or "")
            group_text = partition.render_group(partition.groups(parts, self.opts.groups)[gi])
        elif step == "SASM":
            answers = []
            for c, t in done.items():
                if "SONE" in c:
                    tt = c.split("-")[2]
                    gi = int(c.split("-g")[1])
                    parts = partition.parse_parts(self.reply_of("01-S1234") or "")
                    answers.append((tt, gi, partition.groups(parts, self.opts.groups)[gi], t))
            pile_text = partition.pile(answers)
        user = arms.user_message(self.arm, ustep, self.text, self.qblock, carrier_text=carrier,
                                 test=test, group_text=group_text, pile_text=pile_text,
                                 skeleton=self.skeleton if ustep in ("ALL", "S67") else None)
        reply_path = os.path.join(self.replies, call + ".md")
        body = (self.sys + "\n\n" + user +
                f"\n\nOutput path for your answer (use Write, once, your answer only): {reply_path}\n")
        if not self.with_cl:
            question.check_withheld(body, self.q)
        prompt_path = os.path.join(self.prompts, call + ".txt")
        write_text(prompt_path, body)
        rec = {"run": self.rid, "arm": self.arm, "document": self.doc, "repeat": self.repeat,
               "call": call, "step": step, "prompt": prompt_path, "reply": reply_path,
               "meta": os.path.join(self.meta, call + ".json"), "words": len(body.split()),
               "carrier": self.cfg["carrier"], "built_at": stamp(), "done": False}
        rec.update(extra)
        return rec

    def plan_record(self):
        """What wrap_sonnet.py copies into the run record (fault 13). The Sonnet run record
        carried none of these five, and without them the Sonnet half of stage C cannot show
        that every arm was handed the same question, nor how large arm (x)'s edit was."""
        return {"run": self.rid, "arm": self.arm, "document": self.doc, "repeat": self.repeat,
                "question": question.identity(self.q, self.with_cl),
                "question_as_sent": self.qblock,
                "change_list_withheld": not self.with_cl,
                "exchange": self.exchange_rec,
                "skill_variant": ({"kind": self.cfg["skill_variant"], "removed": self.removed,
                                   "removed_lines": (self.removed["table_rows"]
                                                     + self.removed["graph_lines"]
                                                     + self.removed["sentences"])}
                                  if self.cfg["skill_variant"] else None),
                "derivation3_qualification_sent": rig.DERIVATION3_QUALIFICATION_SENT,
                "derivation3_qualification_reason": rig.DERIVATION3_REASON,
                "written_at": stamp()}

    def write_plan_record(self):
        return write_json(os.path.join(self.b, "plan", self.rid + ".json"), self.plan_record())

    def next_call(self):
        self.write_plan_record()
        for c in self.call_list():
            if self.opts.dry or self.reply_of(c) is None:
                if not self.opts.dry:
                    return self.build(c)
                self.build(c)
        if self.opts.dry:
            return {"run": self.rid, "done": True, "dry": True, "calls": len(self.call_list())}
        last = self.call_list()[-1]
        return {"run": self.rid, "done": True, "report": os.path.join(self.replies, last + ".md")}


def setup(opts, rows):
    b = base(opts.scratch) if not opts.dry else os.path.join(RIG, "dry", READER)
    for d in ("prompts", "replies", "meta", "plan"):
        os.makedirs(os.path.join(b, d), exist_ok=True)
    dst = os.path.join(b, "hard-to-vary")
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(rig.SKILL_COPY, dst)
    return b


def jobs(opts, rows):
    from run_deepseek import jobs as _j
    return _j(opts, rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["plan", "next", "status"])
    p.add_argument("--scratch", default=os.environ.get("W10_SCRATCH", ""))
    p.add_argument("--run", default="")
    p.add_argument("--arms", default="all")
    p.add_argument("--docs", default="")
    p.add_argument("--repeats", default="1,2,3")
    p.add_argument("--texts", default=None)
    p.add_argument("--sources", default=None)
    p.add_argument("--split-file", dest="split_file", default=None)
    p.add_argument("--groups", type=int, default=2)
    p.add_argument("--split", default="cross", choices=["cross", "rotate"])
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    o.arms = [a.strip() for a in o.arms.split(",") if a.strip()]
    o.docs = [d.strip() for d in o.docs.split(",") if d.strip()]
    o.repeats = [int(k) for k in o.repeats.split(",") if k.strip()]
    if not o.scratch and not o.dry:
        raise SystemExit("--scratch DIR (or W10_SCRATCH) is needed: the prompts and replies live "
                         "outside the repository. Nothing written.")
    skillcheck.check()
    rows = corpus.manifest(o.sources)
    if o.cmd == "status":
        b = base(o.scratch)
        for rid in sorted(os.listdir(os.path.join(b, "prompts"))):
            rd = os.path.join(b, "replies", rid)
            got = len(os.listdir(rd)) if os.path.isdir(rd) else 0
            want = len(os.listdir(os.path.join(b, "prompts", rid)))
            print(f"  {rid}: {got}/{want} replies")
        return
    tdir = corpus.texts_dir(sys.argv)
    setup(o, rows)
    if o.cmd in ("plan",):
        js = jobs(o, rows)
        plan = []
        for doc, arm, k in js:
            r = SonnetRun(rows[doc], corpus.document(doc, tdir, rows[doc])[0], arm, k, o)
            res = r.next_call()
            plan.append({"run": r.rid, "arm": arm, "document": doc, "repeat": k,
                         "calls_known": r.call_list(), "first": res})
            print(f"  {r.rid}: {len(r.call_list())} call(s) known"
                  + (" [dry: every prompt written]" if o.dry else ""))
        out = os.path.join(base(o.scratch) if not o.dry else os.path.join(RIG, "dry", READER), "plan.json")
        write_json(out, {"made_at": stamp(), "reader": READER, "dry": o.dry,
                         "skill_digests": skillcheck.check(), "runs": plan})
        print(f"plan written to {out}" + ("  (dry: nothing sent)" if o.dry else ""))
        return
    if o.cmd == "next":
        doc, arm, k = rig.parse_run_id(o.run)
        r = SonnetRun(rows[doc], corpus.document(doc, tdir, rows[doc])[0], arm, k, o)
        print(json.dumps(r.next_call(), ensure_ascii=False))
        return


if __name__ == "__main__":
    main()
