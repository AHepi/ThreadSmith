#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: redoes, from the formulas reply 04 states, the two small arithmetic checks
# whose outputs reply 04 pasted (copied unchanged into tools/s122/04/), and compares line by
# line. Reply 04 did not give its code, so the print formats here are Claude's guesses at its
# formats; the numbers are what is checked. It also redoes the reply's other arithmetic (the
# ceiling of 116,640,000 bounded executions) and the same sample-size formula for reply 01's
# Bonferroni variant. Pure arithmetic; runs nothing else.
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent / "s122" / "04"


def first_check():
    lines = []
    for history in ([0.8, 0.2, 0.5], [0.2, 0.8, 0.5]):
        fast = slow = 0.5
        for p in history:
            fast = 0.5 * fast + 0.5 * p
            slow = 0.875 * slow + 0.125 * p
        lines.append(f"{history} {fast} {slow} {fast - slow}")
    return lines


def second_check():
    lines = []
    for name, gap in (("short", 10), ("long", 100)):
        trace = math.exp(-gap / 50)
        gate = int(trace > 0.5)
        timer = int(gap < -50 * math.log(0.5))
        lines.append(f"{name}: trace={trace:.6f}; trace_gate={gate}; timer_gate={timer}")
    for name, history in (("fall_then_middle", [0.8, 0.2, 0.5]), ("rise_then_middle", [0.2, 0.8, 0.5])):
        fast = slow = 0.5
        for p in history:
            fast = 0.5 * fast + 0.5 * p
            slow = 0.875 * slow + 0.125 * p
        p = history[-1]
        temporal = 0.01 + (1 - p) + max(fast - slow, 0)
        memoryless = 0.01 + (1 - p)
        lines.append(f"{name}: fast={fast:.9f}; slow={slow:.9f}; temporal_u={temporal:.9f}; "
                     f"memoryless_u={memoryless:.9f}")
    for name, values in (("growing", [48, 55, 65]), ("all77", [13, 32, 41])):
        mean = sum(values) / 3
        var = sum((v - mean) ** 2 for v in values) / 2
        n = 2 * (1.96 + 0.84) ** 2 * var / 100
        lines.append(f"{name}: mean={mean:.6f}; sample_variance={var:.6f}; sample_sd={math.sqrt(var):.6f}; "
                     f"n_raw={n:.6f}; n_ceil={math.ceil(n)}")
    lines.append("36 seeds x 3 arms x 1 CPU-hour = 108 CPU-hours; at 3 concurrent = 36 wall-hours")
    lines.append("6 seeds x 3 arms x 1 CPU-hour = 18 CPU-hours; at 3 concurrent = 6 wall-hours")
    return lines


def compare(name, ours, filename):
    theirs = (HERE / filename).read_text().splitlines()
    same = 0
    for a, b in zip(ours, theirs):
        flag = "same" if a == b else "DIFFERENT"
        same += a == b
        print(f"  {flag}: {b}" + ("" if a == b else f"\n    ours: {a}"))
    print(f"{name}: {same} of {len(theirs)} lines identical ({len(ours)} computed)")


if __name__ == "__main__":
    compare("first check", first_check(), "block-01 reported output of the first arithmetic check.txt")
    compare("second check", second_check(), "block-02 reported output of the second arithmetic check.txt")
    print("ceiling of bounded executions: 108 x 50 x 3600 x 6 =", 108 * 50 * 3600 * 6)
    z = 2.2414
    print("reply 01 Bonferroni, all-77 variance: n =", round(2 * (z + 0.84) ** 2 * 204.3333333 / 100, 2))
    print("reply 01 at n=3, s=14.295: detectable difference =",
          round(math.sqrt(2 * (1.96 + 0.84) ** 2 * 14.294521 ** 2 / 3), 2))
