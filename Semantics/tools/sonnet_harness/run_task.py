#!/usr/bin/env python3
"""Run one task spec of the Sonnet harness: check its inputs, run its commands, apply its pass/fail checks.

  python3 -B run_task.py SPEC.json [--phase validate|run|check|all] [--as-verifier]

A task spec (format: specs/TASK SPEC FORMAT.md; example specs in specs/) names ONE job: its inputs with their md5s,
the exact commands to run before the agent's part ("steps") and after it ("check_steps"), the agent's part if any
(the one file it writes and that file's JSON schema), and the checks that decide pass or fail. Placeholders in
strings: {PY} this Python, {H} the harness folder, {SEM} Semantics/, {REPO} the repository, {OUT} the spec's out_dir,
{TEST_ROOT} the harness's test folder in the scratchpad, {RUN} the run label given by --run (default "manual"), so that
a second run of the same spec writes to a fresh folder (the appliers never write over a file).

Phases:
  brief     print what a Workflow gives the agent: the exact commands and the agent's part (nothing is run).
  validate  the spec's form; every input present with its md5; out_dir writable (the scratchpad only).
  run       validate, then each command of "steps" in order (argv lists, no shell, a deadline each); each command's
            stdout JSON is saved to {OUT}/<save>.
  check     validate, then the agent's file against its schema (if the spec has an agent part), then each command of
            "check_steps", then the checks.
  all       run, then check (a job with no agent part).
It prints one JSON object: every command's exit and time, every check with what was found and what was wanted, ok,
escalate (true whenever ok is false), and a digest of the checks, so a second run by another agent can be compared
with the first by the Workflow script. With --as-verifier the result goes to result.<phase>.verifier.json, so the
worker's own files are never written over.
--background starts the phase detached and returns at once; --wait N then waits up to N seconds for its result (a
long run, such as the whole claim suite, outlives the agent's own command deadline; lesson S14).
It never decides anything a check does not state.
"""
import argparse
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402

SPEC_TAG = "sonnet-harness task v1"
KINDS = ("mechanical", "extraction", "records")
OPS = ("equals", "in", "lte", "gte", "empty", "nonempty", "length_equals")


def subst(x, m):
    if isinstance(x, str):
        for k, v in m.items():
            x = x.replace("{%s}" % k, v)
        return x
    if isinstance(x, list):
        return [subst(v, m) for v in x]
    if isinstance(x, dict):
        return {k: subst(v, m) for k, v in x.items()}
    return x


def get(obj, path):
    for p in path.split(".") if path else []:
        if isinstance(obj, list):
            obj = obj[int(p)]
        elif isinstance(obj, dict):
            if p not in obj:
                raise KeyError(path)
            obj = obj[p]
        else:
            raise KeyError(path)
    return obj


def validate_schema(obj, schema, where="$"):
    """A small JSON-schema check (type, required, properties, items, enum, minItems): enough for the agents' files."""
    errs = []
    t = schema.get("type")
    types = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool,
             "null": type(None)}
    if t:
        ts = t if isinstance(t, list) else [t]
        if not any(isinstance(obj, types[x]) and not (x in ("integer", "number") and isinstance(obj, bool)) for x in ts):
            return ["%s: not %s" % (where, t)]
    if "enum" in schema and obj not in schema["enum"]:
        errs.append("%s: %r not in %s" % (where, obj, schema["enum"]))
    if isinstance(obj, dict):
        for r in schema.get("required", []):
            if r not in obj:
                errs.append("%s: missing %s" % (where, r))
        for k, s in schema.get("properties", {}).items():
            if k in obj:
                errs += validate_schema(obj[k], s, "%s.%s" % (where, k))
    if isinstance(obj, list):
        if len(obj) < schema.get("minItems", 0):
            errs.append("%s: fewer than %d items" % (where, schema["minItems"]))
        if "items" in schema:
            for i, v in enumerate(obj):
                errs += validate_schema(v, schema["items"], "%s[%d]" % (where, i))
    return errs


def load_spec(path, run_label):
    spec = H.load_json(path)
    probs = []
    if spec.get("spec") != SPEC_TAG:
        probs.append("'spec' is not %r" % SPEC_TAG)
    for k in ("id", "job", "kind", "purpose", "out_dir", "inputs", "checks"):
        if k not in spec:
            probs.append("missing %r" % k)
    if spec.get("kind") not in KINDS:
        probs.append("kind must be one of %s" % (KINDS,))
    if spec.get("kind") in ("extraction", "records") and not spec.get("agent"):
        probs.append("an %s job needs an 'agent' part" % spec.get("kind"))
    for c in spec.get("checks", []):
        if not any(op in c for op in OPS) or "file" not in c or "name" not in c:
            probs.append("check %r needs name, file and one of %s" % (c.get("name"), OPS))
    if probs:
        H.refuse("the spec is not well formed", problems=probs)
    if not run_label or not all(ch.isalnum() or ch in "-_." for ch in run_label):
        H.refuse("the run label may hold only letters, digits, '-', '_' and '.'")
    m = dict(PY=sys.executable, H=H.HERE, SEM=H.SEM, REPO=H.REPO, TEST_ROOT=H.TEST_ROOT, RUN=run_label)
    m["OUT"] = subst(spec["out_dir"], m)
    return subst(spec, m), m


def run_cmds(cmds, out_dir):
    rows = []
    for c in cmds:
        argv, save = c["argv"], c.get("save")
        for x in argv:
            if H.KEYLIKE.search(x):
                H.refuse("a command names a key-like path; refused")
        r = H.run(argv, cwd=c.get("cwd", H.REPO), timeout=int(c.get("timeout_s", 600)))
        row = dict(name=c.get("name", argv[1] if len(argv) > 1 else argv[0]), exit=r["exit"], seconds=r["seconds"],
                   timed_out=r["timed_out"])
        allowed = c.get("exit_ok", [0, 1])
        row["ran"] = (not r["timed_out"]) and r["exit"] in allowed
        if save:
            try:
                obj = json.loads(r["stdout"])
                H.write_json(os.path.join(out_dir, save), obj)
                row["saved"] = save
                row["reported_ok"] = obj.get("ok") if isinstance(obj, dict) else None
            except ValueError:
                H.write_text(os.path.join(out_dir, save + ".stdout.txt"), r["stdout"])
                row["ran"] = False
                row["why"] = "stdout is not one JSON object"
        if r["stderr"].strip():
            H.write_text(os.path.join(out_dir, (save or "step") + ".stderr.txt"), r["stderr"])
        rows.append(row)
        if not row["ran"]:
            break
    return rows


def eval_checks(checks, out_dir):
    rows = []
    for c in checks:
        row = dict(name=c["name"], file=c["file"], path=c.get("path", ""))
        try:
            obj = H.load_json(os.path.join(out_dir, c["file"]))
            got = get(obj, c.get("path", ""))
        except (KeyError, IndexError, ValueError, SystemExit) as e:
            row.update(ok=False, got=None, why="not found: %s" % e)
            rows.append(row)
            continue
        if "equals" in c:
            ok, want = got == c["equals"], c["equals"]
        elif "in" in c:
            ok, want = got in c["in"], c["in"]
        elif "lte" in c:
            ok, want = isinstance(got, (int, float)) and got <= c["lte"], "<= %s" % c["lte"]
        elif "gte" in c:
            ok, want = isinstance(got, (int, float)) and got >= c["gte"], ">= %s" % c["gte"]
        elif "empty" in c:
            ok, want = hasattr(got, "__len__") and len(got) == 0, "empty"
        elif "nonempty" in c:
            ok, want = hasattr(got, "__len__") and len(got) > 0, "nonempty"
        else:
            ok, want = hasattr(got, "__len__") and len(got) == c["length_equals"], "length %s" % c["length_equals"]
        short = got if not isinstance(got, (list, dict)) or len(json.dumps(got)) < 400 else "(%d entries)" % len(got)
        row.update(ok=bool(ok), got=short, wanted=want)
        rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--phase", default="all", choices=["brief", "validate", "run", "check", "all"])
    ap.add_argument("--as-verifier", action="store_true")
    ap.add_argument("--run", default="manual")
    ap.add_argument("--background", action="store_true",
                    help="start this phase detached (it outlives the agent's command) and return at once")
    ap.add_argument("--wait", type=int, default=0,
                    help="wait up to this many seconds for a phase started with --background, then print its result")
    a = ap.parse_args()
    spec, m = load_spec(a.spec, a.run)
    out_dir = m["OUT"]
    H.guard_write(os.path.join(out_dir, "x"))
    os.makedirs(out_dir, exist_ok=True)
    tail = ".verifier" if a.as_verifier else ""
    result_file = os.path.join(out_dir, "result.%s%s.json" % (a.phase, tail))
    started_file = os.path.join(out_dir, "started.%s%s.json" % (a.phase, tail))
    me = [sys.executable, "-B", os.path.abspath(__file__), os.path.abspath(a.spec), "--phase", a.phase, "--run", a.run]
    if a.as_verifier:
        me.append("--as-verifier")
    if a.phase == "brief":
        H.emit(brief(spec, m, a))
    if a.background:
        if os.path.exists(started_file) and not os.path.exists(result_file):
            H.emit(dict(ok=False, running=True, escalate=False, why="this phase is already started; use --wait"))
        with open(os.path.join(out_dir, "background.%s%s.log" % (a.phase, tail)), "w") as log:
            p = subprocess.Popen(me, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                 start_new_session=True, cwd=H.REPO)
        if os.path.exists(result_file):
            os.replace(result_file, result_file + ".earlier")
        H.write_json(started_file, dict(pid=p.pid, command=me[1:], started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
        H.emit(dict(ok=True, started=True, pid=p.pid, then="run the same command with --wait 540 in place of --background"))
    if a.wait:
        t0 = time.time()
        while time.time() - t0 < a.wait:
            if os.path.exists(result_file):
                H.emit(H.load_json(result_file))
            time.sleep(5)
        H.emit(dict(ok=False, running=True, escalate=False, why="not finished after %d s; run the same --wait again" % a.wait))
    res = dict(spec=H.rel(a.spec), id=spec["id"], job=spec["job"], kind=spec["kind"], phase=a.phase, run=a.run,
               out_dir=out_dir)
    ins = []
    for i in spec["inputs"]:
        p = i["path"] if os.path.isabs(i["path"]) else os.path.join(H.REPO, i["path"])
        got = H.md5_file(p) if os.path.isfile(p) else None
        ins.append(dict(path=i["path"], md5_ok=(got == i["md5"]) if i.get("md5") else got is not None))
    res["inputs_ok"] = all(x["md5_ok"] for x in ins)
    res["inputs_bad"] = [x["path"] for x in ins if not x["md5_ok"]]
    ok = res["inputs_ok"]
    if a.phase == "validate" or not ok:
        res["ok"] = ok
        res["escalate"] = not ok
        H.emit(res)
    if a.phase in ("run", "all"):
        res["steps"] = run_cmds(spec.get("steps", []), out_dir)
        ok = ok and all(s["ran"] for s in res["steps"])
    if a.phase in ("check", "all") and ok:
        ag = spec.get("agent")
        if ag:
            wf = ag["write"]
            if os.path.isfile(wf) and not a.as_verifier:
                # keep every version the agent handed in, so a first attempt can be read after a fix
                n = 1
                while os.path.exists("%s.attempt%d" % (wf, n)):
                    n += 1
                with open(wf, "rb") as src, open("%s.attempt%d" % (wf, n), "wb") as dst:
                    dst.write(src.read())
                res["agent_attempt"] = n
            if not os.path.isfile(wf):
                res["agent_file"] = dict(path=wf, present=False)
                ok = False
            elif not ag.get("output_schema"):
                errs = [] if os.path.getsize(wf) > 0 else ["empty file"]
                res["agent_file"] = dict(path=wf, present=True, schema_errors=errs, md5=H.md5_file(wf))
                ok = ok and not errs
            else:
                try:
                    errs = validate_schema(H.load_json(wf), ag.get("output_schema", {}))
                except (ValueError, SystemExit) as e:
                    errs = ["not JSON: %s" % e]
                res["agent_file"] = dict(path=wf, present=True, schema_errors=errs[:20], md5=H.md5_file(wf))
                ok = ok and not errs
        if ok:
            res["check_steps"] = run_cmds(spec.get("check_steps", []), out_dir)
            ok = all(s["ran"] for s in res["check_steps"])
        res["checks"] = eval_checks(spec["checks"], out_dir) if ok else []
        ok = ok and all(c["ok"] for c in res["checks"])
        res["checks_failed"] = [c["name"] for c in res["checks"] if not c["ok"]]
    res["ok"] = ok
    res["escalate"] = not ok
    res["digest"] = H.sha256_text(json.dumps([(c["name"], c["ok"], c.get("got")) for c in res.get("checks", [])],
                                             ensure_ascii=False, sort_keys=True))[:16]
    if os.path.exists(result_file):  # never write over an earlier result: keep it numbered
        n = 1
        while os.path.exists(result_file[:-5] + ".%d.json" % n):
            n += 1
        os.replace(result_file, result_file[:-5] + ".%d.json" % n)
    H.write_json(result_file, res)
    H.emit(res)


def brief(spec, m, a):
    """What a Workflow needs to give one agent this job: the commands, and the agent's part, placeholders filled."""
    here = os.path.abspath(__file__)
    cmd = lambda ph, extra="": 'python3 -B "%s" "%s" --phase %s --run %s%s' % (here, os.path.abspath(a.spec), ph, a.run, extra)
    return dict(ok=True, id=spec["id"], job=spec["job"], kind=spec["kind"], purpose=spec["purpose"],
                spec=os.path.abspath(a.spec), run=a.run, out_dir=m["OUT"], never=spec.get("never", []),
                agent=spec.get("agent"), long=any(int(c.get("timeout_s", 600)) > 500 for c in spec.get("steps", [])),
                commands=dict(all=cmd("all"), run=cmd("run"), check=cmd("check"),
                              all_background=cmd("all", " --background"), all_wait=cmd("all", " --wait 540"),
                              verify=cmd("check", " --as-verifier")))


if __name__ == "__main__":
    main()
