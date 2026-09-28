# S108 Part A round 2, section 1: write the Sonnet harness specs for the whole-suite runs (rule 5; "Who does what").
#   python3 -B s108r2_s1_specs.py
# Writes, under Semantics/tools/sonnet_harness/specs/:
#   "s108r2 claim suites, section 1.json"   every run: the suite with every variant off once, then one run per variant reading;
#   "s108r2 suite, section 1, <variant>.json"  the same commands for one variant alone (the rule's naming), for a re-run.
# Each run is run_claims.py on this section's copy of the program, compared with the round-4 record (key after_round4); a
# check step (s108r2_s1_suite_check.py) lists the claims that move and compares them with "suite - expected moves.json".
# The inputs' md5s are taken when this runs; the harness refuses a run if any input has changed since.
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REPO = os.path.dirname(SEM)
COPY = "results/S108 Part A round 2 - computation/section 1 model"
RUNS = "results/S108 Part A round 2 - computation/section 1 runs"
RECORD = "results/S107 Round 4 - maths after the reading/formal claims, after round 4.json"
EXPECT = RUNS + "/suite - expected moves.json"
CHECK = COPY + "/s108r2_s1_suite_check.py"
SPECS = os.path.join(SEM, "tools", "sonnet_harness", "specs")

RUN_ORDER = [
    ("off", "every variant off (the program after round 4)"),
    ("R2V1.1-declared", "R2V1.1, every question's recorded ρ_p declared"),
    ("R2V1.1-selected", "R2V1.1, every question's recorded ρ_p selected"),
    ("R2V1.1-constructed", "R2V1.1, every question's recorded ρ_p constructed"),
    ("R2V1.6", "R2V1.6, Expl := (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t), the defeat sets as written"),
    ("R2V1.6s", "R2V1.6s, as R2V1.6 with (Suff)'s and (Nec)'s antecedent co-varied"),
    ("R2V1.10", "R2V1.10, S108-1-I1 read (iii), with round 1's V1.1 on"),
]
GROUPS = {"R2V1.1": ["R2V1.1-declared", "R2V1.1-selected", "R2V1.1-constructed"], "R2V1.6": ["R2V1.6", "R2V1.6s"], "R2V1.10": ["R2V1.10"]}


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
    purpose = ("S108 Part A round 2, section 1 (rule 5 of the round-2 reading rule; 'Who does what'): the whole claim suite on section 1's "
               "copy of the program (results/S108 Part A round 2 - computation/section 1 model/), %s, each run compared claim by claim "
               "and part by part with the round-4 record (formal claims, after round 4.json, key after_round4: 133 hold, 2 "
               "counterexamples, 7 not tested, of 142); a check step lists the claims whose results move and compares them with what the "
               "computing agent expects ('suite - expected moves.json'). A variant is switched on only by the environment each command "
               "sets (/usr/bin/env NAME=value); nothing in the program is edited. Runs: %s. Any failure, and any claim that moves "
               "other than those expected, goes back to the section 1 computing agent (Opus)."
               % ("with every variant off once and then with each variant reading on" if with_off else "with the variant on", ", ".join(names)))
    return {"spec": "sonnet-harness task v1", "id": sid, "job": "claim_suite", "kind": "mechanical", "purpose": purpose,
            "out_dir": "{TEST_ROOT}/{RUN}/%s" % sid, "inputs": inputs(), "steps": steps, "check_steps": check_steps, "checks": checks,
            "on_fail": "escalate to the section 1 computing agent (Opus) with result.*.json, <run>/raw.txt, <run>/claims.json and check.<run>.json",
            "never": ["decide whether a claim should hold", "decide whether a move is right", "edit the program, the record or the expected moves",
                      "write outside the out folder", "open a key file", "call GLM", "commit"]}


def main():
    out = {}
    s = spec("s108r2-claim-suites-section-1", [n for n, _ in RUN_ORDER if n != "off"], True)
    p = os.path.join(SPECS, "s108r2 claim suites, section 1.json")
    json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    out[p] = len(s["steps"])
    for g, runs in GROUPS.items():
        s = spec("s108r2-suite-section-1-%s" % g.lower().replace(".", "-"), runs, False)
        p = os.path.join(SPECS, "s108r2 suite, section 1, %s.json" % g)
        json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        out[p] = len(s["steps"])
    for p, n in out.items():
        print("%s: %d run(s)" % (os.path.relpath(p, REPO), n))


if __name__ == "__main__":
    main()
