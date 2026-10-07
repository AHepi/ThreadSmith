# S108 Part A round 2, section 3: write the Sonnet harness specs for the whole-suite runs (rule 5; "Who does what"), on the model of
# tools/sonnet_harness/specs/r2 claim suite.json and section 1's s108r2_s1_specs.py.
#   python3 -B s108r2_s3_specs.py
# Writes, under Semantics/tools/sonnet_harness/specs/:
#   "s108r2 claim suites, section 3.json"   every run: the suite with every switch off once, then one run per variant reading;
#   "s108r2 suite, section 3, <variant>.json"  the same commands for one variant alone (the rule's naming), for a re-run.
# Each run is run_claims.py on this section's copy of the program, compared with the round-4 record (key after_round4); a check
# step (s108r2_s3_suite_check.py) lists the claims that move and compares them with "suite - expected moves.json". The inputs'
# md5s are taken when this runs; the harness refuses a run if any input has changed since.
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REPO = os.path.dirname(SEM)
COPY = "results/S108 Part A round 2 - computation/section 3 model"
RUNS = "results/S108 Part A round 2 - computation/section 3 runs"
RECORD = "results/S107 Round 4 - maths after the reading/formal claims, after round 4.json"
EXPECT = RUNS + "/suite - expected moves.json"
CHECK = COPY + "/s108r2_s3_suite_check.py"
SPECS = os.path.join(SEM, "tools", "sonnet_harness", "specs")

RUN_ORDER = [
    ("off", "every switch off (the program after round 4)"),
    ("R2V3.1", "R2V3.1, CT a Build subhistory, ExplUse asking Acc of the claim used (round 1's V3.4 with S108_S3_CT=build)"),
    ("R2V3.2-contract", "R2V3.2's old form, D13.8's record keyed by the new contract (the formal core's words); the variant's new form, keyed by the change, is the program's ('off')"),
    ("R2V3.4-ports", "R2V3.4, D15.8's parts read as the ports of t's codomain with their bindings"),
    ("R2V3.4-edits", "R2V3.4's other choice, D15.8's parts read as edits"),
    ("R2V3.5", "R2V3.5, no construction stated ⇒ 𝒯 = ∅"),
    ("R2V3.6", "R2V3.6, provenance_of's histories as chains with Rep computed (I90's other choice)"),
    ("R2V3.7", "R2V3.7, ⪯_h the reflexive closure of ≺_h (D11.3)"),
    ("R2V3.8", "R2V3.8, every argument has a step (D9.2; departs from S41 Q23)"),
    ("R2V3.9", "R2V3.9, D9.1 without 'Ans_p(a,b) = y'"),
    ("R2V3.10", "R2V3.10, Can without its construction disjunct (D15.5)"),
]
GROUPS = {"R2V3.1": ["R2V3.1"], "R2V3.2": ["R2V3.2-contract"], "R2V3.4": ["R2V3.4-ports", "R2V3.4-edits"], "R2V3.5": ["R2V3.5"],
          "R2V3.6": ["R2V3.6"], "R2V3.7": ["R2V3.7"], "R2V3.8": ["R2V3.8"], "R2V3.9": ["R2V3.9"], "R2V3.10": ["R2V3.10"]}


def md5(p):
    with open(os.path.join(SEM, p), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def inputs():
    files = sorted(COPY + "/model/" + f for f in os.listdir(os.path.join(SEM, COPY, "model")) if f.endswith(".py"))
    return [dict(path="Semantics/" + p, md5=md5(p)) for p in files + [CHECK, EXPECT, RECORD]]


def run_step(name, env):
    argv = (["/usr/bin/env"] + ["%s=%s" % kv for kv in sorted(env.items())] if env else []) + [
        "{PY}", "-B", "{H}/run_claims.py", "--model-dir", "{SEM}/" + COPY, "--out-dir", "{OUT}/" + name,
        "--scale", "4", "--time-cap", "45", "--timeout", "2700", "--expect", "{SEM}/" + RECORD, "--expect-key", "after_round4"]
    if name == "off":
        argv += ["--expect-counts", "H=133,CEX=2,NT=7,of=142"]
    return argv


def spec(sid, runs, with_off):
    exp = json.load(open(os.path.join(SEM, EXPECT), encoding="utf-8"))["runs"]
    labels = dict(RUN_ORDER)
    names = (["off"] if with_off else []) + runs
    steps = [dict(name="the whole suite, %s" % labels[n], argv=run_step(n, exp[n]["env"]), timeout_s=2800, save="%s.json" % n) for n in names]
    check_steps = []
    for n in names:
        argv = ["{PY}", "-B", "{SEM}/" + CHECK, "--claims", "{OUT}/%s/claims.json" % n, "--record", "{SEM}/" + RECORD,
                "--key", "after_round4", "--expected", "{SEM}/" + EXPECT, "--run", n]
        if with_off and n != "off":
            argv += ["--off-raw", "{OUT}/off/raw.txt", "--on-raw", "{OUT}/%s/raw.txt" % n]
        check_steps.append(dict(name="the claims that move in '%s', against the record and against what the computing agent expects" % n,
                                argv=argv, timeout_s=300, save="check.%s.json" % n, exit_ok=[0, 1]))
    checks = []
    for n in names:
        f = "%s.json" % n
        checks += [dict(name="%s: the suite ran to its end" % n, file=f, path="timed_out", equals=False),
                   dict(name="%s: the run's exit is 0 or 1 (1: it differs from the record)" % n, file=f, path="exit", **{"in": [0, 1]}),
                   dict(name="%s: no claim raised an error" % n, file=f, path="claims_with_error", empty=True),
                   dict(name="%s: 142 claims" % n, file=f, path="counts.of", equals=142),
                   dict(name="%s: nothing written in the program's folder" % n, file=f, path="model_folder_changed", empty=True),
                   dict(name="%s: no __pycache__ left in the program's folder" % n, file=f, path="pycache_new", empty=True),
                   dict(name="%s: the claims that move are exactly those expected" % n, file="check.%s.json" % n, path="ok", equals=True)]
        if n == "off":
            checks += [dict(name="off: exit 0", file=f, path="exit", equals=0),
                       dict(name="off: 133 hold", file=f, path="counts.H", equals=133),
                       dict(name="off: 2 counterexamples", file=f, path="counts.CEX", equals=2),
                       dict(name="off: 7 not tested", file=f, path="counts.NT", equals=7),
                       dict(name="off: every claim and part equal to the round-4 record", file=f, path="differences", empty=True)]
    purpose = ("S108 Part A round 2, section 3 (rule 5 of the round-2 reading rule; 'Who does what'): the whole claim suite on section 3's "
               "copy of the program (results/S108 Part A round 2 - computation/section 3 model/), %s, each run compared claim by claim "
               "and part by part with the round-4 record (formal claims, after round 4.json, key after_round4: 133 hold, 2 "
               "counterexamples, 7 not tested, of 142); a check step lists the claims whose results move and compares them with what the "
               "computing agent expects ('suite - expected moves.json'). A variant is switched on only by the environment each command "
               "sets (/usr/bin/env NAME=value); nothing in the program is edited. R2V3.3 has no switch (no function of the program reads "
               "a trace's extent or a tag's reading of Held: Prepares is a label at one occurrence, I56; Held at an output is set by each "
               "claim, I90), so its whole suite is the 'off' run. Runs: %s. Any failure, and any claim that moves other than those "
               "expected, goes back to the section 3 computing agent (Opus)."
               % ("with every switch off once and then with each variant reading on" if with_off else "with the variant on", ", ".join(names)))
    return {"spec": "sonnet-harness task v1", "id": sid, "job": "claim_suite", "kind": "mechanical", "purpose": purpose,
            "out_dir": "{TEST_ROOT}/{RUN}/%s" % sid, "inputs": inputs(), "steps": steps, "check_steps": check_steps, "checks": checks,
            "on_fail": "escalate to the section 3 computing agent (Opus) with result.*.json, <run>/raw.txt, <run>/claims.json and check.<run>.json",
            "never": ["decide whether a claim should hold", "decide whether a move is right", "edit the program, the record or the expected moves",
                      "write outside the out folder", "open a key file", "call GLM", "commit"]}


def main():
    out = {}
    s = spec("s108r2-claim-suites-section-3", [n for n, _ in RUN_ORDER if n != "off"], True)
    p = os.path.join(SPECS, "s108r2 claim suites, section 3.json")
    json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    out[p] = len(s["steps"])
    for g, runs in GROUPS.items():
        s = spec("s108r2-suite-section-3-%s" % g.lower().replace(".", "-"), runs, False)
        p = os.path.join(SPECS, "s108r2 suite, section 3, %s.json" % g)
        json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        out[p] = len(s["steps"])
    for p, n in out.items():
        print("%s: %d run(s)" % (os.path.relpath(p, REPO), n))


if __name__ == "__main__":
    main()
