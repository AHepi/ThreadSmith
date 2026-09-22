"""DRIVER. The stage-B adapter: the 96 marked reports of the record, in the rig's shape.

  python3 record_adapter.py                      # writes <rig>/runs/record96/<run>.json
  python3 record_adapter.py --check              # counts and prints, writes nothing
  python3 record_adapter.py --rig DIR --reader record96 --out DIR

Why it exists (fault 0 of the stage-A review). W10 stage B re-marks "the 96 marked reports in
hand" and is the gate for stage C: "No field carries an arm difference in stage C unless it
agreed here." first_marker.py reads <rig>/runs/<reader>/*.json and needs run_id, document and
report; the record's files carry source, mode, repeat and reply, and nothing in the rig adapted
them, so stage B could not start.

The 96, as W3 section 5 names them ("the 48 close-marked of plan 52 and the 48 repeat reports of
H57, H59 and H62"):

  p52     the 48 named in marking/secret_mapping.json, read from runs/<source>-m<mode>.json
  rep     runs_repeat/          12   DeepSeek, file 30
  rep31   runs_repeat_31/       12   DeepSeek, file 31
  son     runs_sonnet5/         12   Sonnet, file 30, the subagent transport
  son31   runs_sonnet5_31/      12   Sonnet, file 31, the subagent transport

Nothing in the record is edited or moved: this reads it and writes a new file per report in the
rig's own runs folder. Run ids are `<set>_<the record's own file stem>` — an underscore, so no
adapted id can be mistaken for this round's `<document>-<arm>-r<repeat>`. These are the
record's runs and not this round's: `agreement.py runs` is about this round's arms and its
(a)-to-(a) baseline, and is not run over them. What stage B needs of them is
`first_marker.py prompts`, `second_marker.py prep` and `agreement.py markers`.

What the adapted record carries, and how each value is known:

  document                 the record's `source`                                     (seen)
  report                   the record's `reply`, as it came                          (seen)
  modules_served           the record's `modules_opened`                             (seen)
  requests                 the record's `api_calls`; absent on the subagent runs     (seen)
  steps                    1. Every run of the record is one pass of the whole
                           procedure in one call, with the tool loop inside it   (worked out)
  tool_loop_requests       api_calls - 1. The old rig made one request and then one
                           more per round of the tool loop (plan 49 rig, run.py), so
                           every request after the first is a continuation. Worked
                           out, not recorded, and the record says so            (worked out)

The four fields whose source is the run record are filled from these by
`first_marker.py collect`, not by a marker (fault 2). On these 96, `request_text_saved` reads
"missing" for every one: the old rig kept no request text, which is what a compliance count is
for (A4's criterion for the field says the same).
"""
import os, sys, json, argparse

import rig
from rig import RUNS, write_json, read_json, stamp

RECORD = os.path.join(rig.REPO, "HV Skill", "rigs",
                      "plan 49 rig - DeepSeek on outside papers")
READER = "record96"

# set tag -> (folder, how it was run)
REPEAT_SETS = {
    "rep":   ("runs_repeat",      "DeepSeek V3.2, skill file 30"),
    "rep31": ("runs_repeat_31",   "DeepSeek V3.2, skill file 31"),
    "son":   ("runs_sonnet5",     "Sonnet 5, the Claude Code subagent transport, skill file 30"),
    "son31": ("runs_sonnet5_31",  "Sonnet 5, the Claude Code subagent transport, skill file 31"),
}
CLOSE_MARKED = os.path.join("marking", "secret_mapping.json")
EXPECTED = 96


def one(set_tag, folder, stem, record_dir):
    p = os.path.join(record_dir, folder, stem + ".json")
    if not os.path.exists(p):
        raise SystemExit(f"the record has no {p}. Nothing written.")
    d = read_json(p)
    api = d.get("api_calls")
    rec = {
        "run_id": f"{set_tag}_{stem}",
        "reader": READER,
        "set": set_tag,
        "document": d.get("source"),
        "report": d.get("reply") or "",
        "arm": set_tag,
        "arm_title": "a run of the record, not an arm of this round",
        "repeat": d.get("repeat"),
        "mode": d.get("mode"),
        "skill_file": d.get("skill_file"),
        "model": d.get("model"),
        "transport": d.get("transport"),
        "effort": d.get("effort"),
        "modules_served": list(d.get("modules_opened") or []),
        "modules_served_by": ("the record's modules_opened. On the subagent runs the old rig "
                              "flagged this field modules_self_reported true, which is the "
                              "fault W8 part C4 names; it is the only trace the record has"),
        "requests": api,
        "steps": 1,
        "steps_are": ("1: every run of the record is one pass of the whole procedure in one "
                      "call, with the tool loop inside it. Worked out, not recorded"),
        "tool_loop_requests": (None if api is None else max(0, api - 1)),
        "tool_loop_requests_are": ("api_calls - 1: the old rig made one request and then one "
                                   "more per round of the tool loop (plan 49 rig, run.py), so "
                                   "every request after the first is a continuation. Worked "
                                   "out, not recorded"),
        "tool_calls_in_the_record": d.get("tool_calls"),
        "calls": [],
        "calls_are": ("empty: the old rig kept no request text. request_text_saved therefore "
                      "reads missing on all 96, which is what a compliance count is for"),
        "usage_total": d.get("usage_total"),
        "from_the_record": os.path.relpath(p, rig.REPO),
        "adapted_at": stamp(),
        "adapted_by": "code/record_adapter.py; the record itself is not edited or moved",
        "not_a_run_of_this_round": ("a report of the record, adapted for stage B only. "
                                    "agreement.py runs is about this round's arms and its "
                                    "(a)-to-(a) baseline and is not read over these"),
    }
    if not rec["document"]:
        raise SystemExit(f"{p}: no 'source' to read as the document. Nothing written.")
    if not rec["report"].strip():
        raise SystemExit(f"{p}: no 'reply' to read as the report. Nothing written.")
    return rec


def collect(record_dir):
    out = []
    mp = os.path.join(record_dir, CLOSE_MARKED)
    mapping = read_json(mp, "the close-marking mapping of plan 52")
    stems = sorted(set(mapping.values()))
    for stem in stems:
        out.append(one("p52", "runs", stem, record_dir))
    for tag, (folder, _) in REPEAT_SETS.items():
        d = os.path.join(record_dir, folder)
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".json"):
                out.append(one(tag, folder, fn[:-5], record_dir))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--record", default=RECORD)
    p.add_argument("--reader", default=READER)
    p.add_argument("--out", default="")
    p.add_argument("--check", action="store_true")
    o = p.parse_args()
    recs = collect(o.record)
    ids = [r["run_id"] for r in recs]
    if len(set(ids)) != len(ids):
        raise SystemExit("two adapted runs share an id; the set tags do not separate the folders.")
    if len(recs) != EXPECTED:
        raise SystemExit(f"{len(recs)} reports adapted, not {EXPECTED}. W3 section 5 names "
                         f"'the 48 close-marked of plan 52 and the 48 repeat reports'. "
                         f"Nothing written.")
    by = {}
    for r in recs:
        by[r["set"]] = by.get(r["set"], 0) + 1
    print(f"{len(recs)} reports: " + ", ".join(f"{k} {v}" for k, v in sorted(by.items())))
    print(f"  documents: {len(sorted({r['document'] for r in recs}))} distinct")
    print(f"  with a modules trace: {len([r for r in recs if r['modules_served']])}")
    print(f"  with a request count: {len([r for r in recs if r['requests'] is not None])}")
    if o.check:
        print("check only: nothing written.")
        return
    base = o.out or os.path.join(RUNS, o.reader)
    for r in recs:
        write_json(os.path.join(base, r["run_id"] + ".json"), r)
    print(f"written under {base}. Now: first_marker.py prompts --reader {o.reader}, "
          f"second_marker.py prep --reader {o.reader}, agreement.py markers --reader {o.reader}")


if __name__ == "__main__":
    main()
