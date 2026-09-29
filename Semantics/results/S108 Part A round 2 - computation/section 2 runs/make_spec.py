# Writes tools/sonnet_harness/specs/s108r2 claim suites, section 2.json (S108 Part A round 2, section 2's computing agent).
import hashlib, json, os
SEM = "/home/user/ThreadSmith/Semantics"
REPO = os.path.dirname(SEM)
COPY_REL = "results/S108 Part A round 2 - computation/section 2 model"
REC_REL = "results/S107 Round 4 - maths after the reading/formal claims, after round 4.json"
CORE_REL = "results/S107 Round 4 - maths after the reading/formal core, after round 4.md"
SW = ["S108_S2_VARIANT", "S108R2_S2_VARIANT", "S108R2_S2_R26", "S108R2_S2_DESC", "S105_SLOT_QUANTIFIER", "S106_ACCOUNT_READING"]


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


inputs = []
mdir = os.path.join(SEM, COPY_REL, "model")
for f in sorted(os.listdir(mdir)):
    if f.endswith(".py"):
        inputs.append({"path": "Semantics/%s/model/%s" % (COPY_REL, f), "md5": md5(os.path.join(mdir, f))})
for rel in (REC_REL, CORE_REL):
    inputs.append({"path": "Semantics/" + rel, "md5": md5(os.path.join(SEM, rel))})


def argv(envs, out, claims=None, expect=True, timeout=2400):
    a = ["/usr/bin/env"]
    for v in SW:
        a += ["-u", v]
    a += envs
    a += ["{PY}", "-B", "{H}/run_claims.py", "--model-dir", "{SEM}/" + COPY_REL, "--out-dir", "{OUT}/" + out,
          "--scale", "4", "--time-cap", "45", "--timeout", str(timeout)]
    for c in claims or []:
        a += ["--claim", c]
    if expect:
        a += ["--expect", "{SEM}/" + REC_REL, "--expect-key", "after_round4"]
    return a


# (label, what it is, env, expected claims_equal (int) or ('lte', n), expected claims_not_in_record count, claims expected to move)
RUNS = [
    ("s00 off", "every switch off: the program after round 4 (the record, 133 / 2 / 7 of 142)", [], 142, 0, []),
    ("s01 R2V2.2 q some", "D6.3's quantifier 'some', (E) as it is", ["S105_SLOT_QUANTIFIER=some"], 140, 0, ["FC26", "FC34"]),
    ("s02 R2V2.2 q some-exempt", "D6.3's quantifier 'some-exempt', (E) as it is", ["S105_SLOT_QUANTIFIER=some-exempt"], 141, 0, ["FC34"]),
    ("s03 R2V2.2 q some-exempt-set", "D6.3's quantifier 'some-exempt-set', (E) as it is", ["S105_SLOT_QUANTIFIER=some-exempt-set"], 141, 0, ["FC34"]),
    ("s04 R2V2.2 x V2.4 q some", "'some' with round 1's V2.4 on (NC1 in (E), C6)", ["S108_S2_VARIANT=V2.4", "S105_SLOT_QUANTIFIER=some"], ("lte", 132), 0,
     ["FC23", "FC23.new1", "FC23.new2", "FC23.new3", "FC23.new5", "FC25.new2", "FC26", "FC27.new1", "FC34", "FC72.new2", "(and possibly claims over generated candidates)"]),
    ("s05 R2V2.2 x V2.4 q some-exempt", "'some-exempt' with V2.4 on", ["S108_S2_VARIANT=V2.4", "S105_SLOT_QUANTIFIER=some-exempt"], ("lte", 134), 0,
     ["FC23", "FC23.new1", "FC23.new2", "FC23.new5", "FC25.new2", "FC27.new1", "FC34", "FC72.new2", "(and possibly claims over generated candidates)"]),
    ("s06 R2V2.2 x V2.4 q some-exempt-set", "'some-exempt-set' with V2.4 on", ["S108_S2_VARIANT=V2.4", "S105_SLOT_QUANTIFIER=some-exempt-set"], ("lte", 134), 0,
     ["FC23", "FC23.new1", "FC23.new2", "FC23.new5", "FC25.new2", "FC27.new1", "FC34", "FC72.new2", "(and possibly claims over generated candidates)"]),
    ("s07 R2V2.3a", "the hand-set histories computed as one-holding chains (I90's other choice)", ["S108R2_S2_VARIANT=R2V2.3a"], 142, 0, []),
    ("s08 R2V2.5", "D6.9 with '≠ ⊥'", ["S108R2_S2_VARIANT=R2V2.5"], 142, 0, []),
    ("s09 R2V2.6 written", "D11.2's second sentence deleted, its own reach (t, H, surv untyped)", ["S108R2_S2_VARIANT=R2V2.6", "S108R2_S2_R26=written"], 142, 0, []),
    ("s10 R2V2.6 HS", "D11.2's second sentence deleted, H and surv untyped", ["S108R2_S2_VARIANT=R2V2.6", "S108R2_S2_R26=HS"], 142, 0, []),
    ("s11 R2V2.6 reply", "the reply's reach: the whole exclusion dropped", ["S108R2_S2_VARIANT=R2V2.6", "S108R2_S2_R26=reply"], 137, 0,
     ["FC12.new2", "FC30.new1", "FC83", "FC98", "FC98.new1"]),
    ("s12 R2V2.8 target", "V1.6's formula on Acc, Desc at the target's grain", ["S108R2_S2_VARIANT=R2V2.8", "S108R2_S2_DESC=target"], 142, 0, []),
    ("s13 R2V2.8 program", "V1.6's formula on Acc, Desc naming the phenomenon; the program's targets for it", ["S108R2_S2_VARIANT=R2V2.8", "S108R2_S2_DESC=program"], 138, 0,
     ["FC22", "FC23.new1", "FC23.new2", "FC23.new5"]),
    ("s14 R2V2.8 widest", "V1.6's formula on Acc, every organization over Desc's ports with its answers (no question has one target)", ["S108R2_S2_VARIANT=R2V2.8", "S108R2_S2_DESC=widest"], ("lte", 130), 0,
     ["FC22", "FC23", "FC23.new1", "FC23.new2", "FC23.new3", "FC23.new5", "FC25.new2", "FC26", "FC27.new1", "FC34", "FC72.new2", "FC74", "(and every other claim asserting that some candidate meets (E))"]),
    ("s15 R2V2.9", "D6.8's five headings (read only by FC31's label)", ["S108R2_S2_VARIANT=R2V2.9"], 141, 0, ["FC31 (its part's label)"]),
    ("s16 R2V2.10", "D12.7: Viol := Viol⁺", ["S108R2_S2_VARIANT=R2V2.10"], 142, 0, []),
    ("s17 R2V2.11", "two claims beside FC21 (FC21.v1, FC21.v2) registered: 144 claims", ["S108R2_S2_VARIANT=R2V2.11"], 142, 2, ["FC21.v1, FC21.v2 (new, not in the record; both hold)"]),
]

steps, checks = [], []
for lab, what, env, eq, extra, mv in RUNS:
    key = lab.split()[0]
    steps.append({"name": "%s: the whole suite with %s, compared with the round-4 record" % (lab, what), "argv": argv(env, key), "timeout_s": 2600,
                  "save": "%s.json" % key})
    f = "%s.json" % key
    checks += [
        {"name": "%s: the suite ran to its end" % lab, "file": f, "path": "exit", "equals": 0},
        {"name": "%s: no claim raised an error" % lab, "file": f, "path": "claims_with_error", "empty": True},
        {"name": "%s: nothing written in the program's folder" % lab, "file": f, "path": "model_folder_changed", "empty": True},
        {"name": "%s: every claim of the record compared" % lab, "file": f, "path": "claims_compared", "equals": 142},
    ]
    if isinstance(eq, int):
        checks.append({"name": "%s: claims equal to the record: %d (moving: %s)" % (lab, eq, ", ".join(mv) or "none"), "file": f, "path": "claims_equal", "equals": eq})
    else:
        checks.append({"name": "%s: claims equal to the record: at most %d (at least these move: %s)" % (lab, eq[1], ", ".join(mv)), "file": f, "path": "claims_equal", "lte": eq[1]})
    if extra:
        checks.append({"name": "%s: claims outside the record: %d" % (lab, extra), "file": f, "path": "claims_not_in_record", "length_equals": extra})
        checks.append({"name": "%s: 144 claims, 135 hold, 2 counterexamples, 7 not tested" % lab, "file": f, "path": "counts.of", "equals": 144})
        checks.append({"name": "%s: 135 hold" % lab, "file": f, "path": "counts.H", "equals": 135})
    else:
        checks.append({"name": "%s: no claim outside the record" % lab, "file": f, "path": "claims_not_in_record", "empty": True})
    if key == "s00":
        checks += [{"name": "s00 off: 133 hold", "file": f, "path": "counts.H", "equals": 133},
                   {"name": "s00 off: 2 counterexamples", "file": f, "path": "counts.CEX", "equals": 2},
                   {"name": "s00 off: 7 not tested", "file": f, "path": "counts.NT", "equals": 7},
                   {"name": "s00 off: every claim and part equal to the record", "file": f, "path": "differences", "empty": True}]

check_steps = [
    {"name": "spot, off: FC23, FC63 (the two counterexamples), FC30.new1, FC31, compared with the record", "argv": argv([], "spot off", ["FC23", "FC63", "FC30.new1", "FC31"], timeout=900),
     "timeout_s": 1000, "save": "spot off.json"},
    {"name": "spot, R2V2.2 'some': FC26, FC34 (both move)", "argv": argv(["S105_SLOT_QUANTIFIER=some"], "spot q some", ["FC26", "FC34"], timeout=900), "timeout_s": 1000, "save": "spot q some.json"},
    {"name": "spot, R2V2.6 the reply's reach: FC30.new1 (moves: (d), the student's copy, selected)", "argv": argv(["S108R2_S2_VARIANT=R2V2.6", "S108R2_S2_R26=reply"], "spot r26", ["FC30.new1"], timeout=900),
     "timeout_s": 1000, "save": "spot r26.json"},
    {"name": "spot, R2V2.8 at the program's grain: FC22, FC23.new2 (both move: the owner's vane and sign)", "argv": argv(["S108R2_S2_VARIANT=R2V2.8", "S108R2_S2_DESC=program"], "spot r28", ["FC22", "FC23.new2"], timeout=900),
     "timeout_s": 1000, "save": "spot r28.json"},
    {"name": "spot, R2V2.11 with round 1's V2.1: FC21.v1 counterexample, FC21.v2 holds (e2.39)", "argv": argv(["S108R2_S2_VARIANT=R2V2.11", "S108_S2_VARIANT=V2.1"], "spot r211 v21", ["FC21.v1", "FC21.v2"], expect=False, timeout=900),
     "timeout_s": 1000, "save": "spot r211 v21.json"},
    {"name": "spot, R2V2.11 with round 1's V2.2: FC21.v1 holds, FC21.v2 counterexample (e2.38)", "argv": argv(["S108R2_S2_VARIANT=R2V2.11", "S108_S2_VARIANT=V2.2"], "spot r211 v22", ["FC21.v1", "FC21.v2"], expect=False, timeout=900),
     "timeout_s": 1000, "save": "spot r211 v22.json"},
]
checks += [
    {"name": "spot off: equal to the record", "file": "spot off.json", "path": "ok", "equals": True},
    {"name": "spot q some: both claims move (0 equal)", "file": "spot q some.json", "path": "claims_equal", "equals": 0},
    {"name": "spot R2V2.6 reply: FC30.new1 moves", "file": "spot r26.json", "path": "claims_equal", "equals": 0},
    {"name": "spot R2V2.8 program: FC22 and FC23.new2 move", "file": "spot r28.json", "path": "claims_equal", "equals": 0},
    {"name": "spot R2V2.11 x V2.1: one counterexample (FC21.v1)", "file": "spot r211 v21.json", "path": "counts.CEX", "equals": 1},
    {"name": "spot R2V2.11 x V2.1: one holds (FC21.v2)", "file": "spot r211 v21.json", "path": "counts.H", "equals": 1},
    {"name": "spot R2V2.11 x V2.2: one counterexample (FC21.v2)", "file": "spot r211 v22.json", "path": "counts.CEX", "equals": 1},
    {"name": "spot R2V2.11 x V2.2: one holds (FC21.v1)", "file": "spot r211 v22.json", "path": "counts.H", "equals": 1},
]

spec = {
    "spec": "sonnet-harness task v1",
    "id": "s108r2-claim-suites-section-2",
    "job": "claim_suite",
    "kind": "mechanical",
    "purpose": ("S108 Part A round 2, section 2 (rule 5 of 'results/S108 Part A round 2 - how the replies will be read, written before sending.md'; "
                "'Who does what': the whole-suite runs are harness jobs). On the section-2 copy of the program ('%s', round 1's copy with round 2's "
                "switches added; every switch off is the program after round 4), run the whole claim suite once with every switch off and once "
                "per in-scope variant setting of round 2's reply (18 runs, one after another; each about 10 minutes), each compared, claim by claim and "
                "part by part (status; each part's label, kind, status), with the round-4 record ('formal claims, after round 4.json', key after_round4). "
                "The claims whose results move are listed by run_claims.py in each run's 'differences'. The expected moves (checks below) come from "
                "single-claim runs by the computing agent (results/S108 Part A round 2 - computation/section 2 runs/single claims/); where a "
                "setting moves (E) for generated candidates (s04-s06, s14) only a lower bound is known and the check is 'at most N equal'. "
                "Round 1's V2.4 with 'every' is not run again (round 1's section-2 run: 7 claims move, as the single-claim runs here confirm). "
                "R2V2.1 (an encoding of the owner's change), R2V2.3 (b) (a built case) vary no code the suite runs; R2V2.4 and R2V2.7 were flagged "
                "out of scope by the tabulation and are not implemented. Each run's switches are set by /usr/bin/env in its argv (the other switch "
                "variables unset). Any failure, any check not met, any difference from the expected goes to Opus (the section-2 computing agent)." % COPY_REL),
    "out_dir": "{TEST_ROOT}/{RUN}/s108r2-claim-suites-section-2",
    "inputs": inputs,
    "steps": steps,
    "check_steps": check_steps,
    "checks": checks,
    "on_fail": "escalate to Opus (the section-2 computing agent) with result.*.json, each run's <label>/raw.txt and <label>/result.json",
    "never": ["decide whether a claim should hold", "decide whether a move is expected beyond the checks", "edit the program or any file of the copy",
              "write outside the out folder", "open a key file", "call GLM", "commit"],
}
out = os.path.join(SEM, "tools/sonnet_harness/specs/s108r2 claim suites, section 2.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(spec, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(out, len(steps), "runs", len(checks), "checks", len(inputs), "inputs")
