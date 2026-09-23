"""c4: the four run-record fields, and modules_served, which only the harness counts.

  /home/user/.venvs/threadsmith/bin/python c4_run_record_fields.py

Explanation under test: stage_b.py shows modules_served at 0 agree / 0 disagree / 96 unreadable
because first_marker.py collect fills the four run-record fields into the first marks only and
second_marker.py collect fills nothing, so every second value is missing. It forbids any marker
having returned a value for these fields (the prompts leave them out). Rival: the markers returned
modules_served and disagreed or nulled it. Separating check: the raw marks' keys, and the
harness's validate logs from the scratch-copy run. Writes nothing.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
B = os.path.join(RIG, "stage-B", "w10")
REC = ["modules_served", "requests", "request_text_saved", "ports_set"]
for side, folder in (("first (M)", "marking1"), ("second (R)", "marking2")):
    d = os.path.join(B, folder, "marks")
    have = {k: 0 for k in REC}
    for fn in sorted(os.listdir(d)):
        row = json.load(open(os.path.join(d, fn)))
        for k in REC:
            have[k] += (k in row)
    print(f"raw marks, {side}: reports carrying each run-record field: {have}")
L = os.path.join(HERE, "harness-programs-on-a-scratch-copy")
for fn in ("03-validate-first.txt", "04-validate-second.txt"):
    t = open(os.path.join(L, fn)).read()
    print(f"{fn}: 'no value for' lines {t.count('no value for')}; "
          + ", ".join(f"{k} {t.count(repr(k))}" for k in REC) + f"; last line: {t.strip().splitlines()[-2]}")
sb = json.load(open(os.path.join(L, "stage_b_record96.json")))["fields"]["modules_served"]
print(f"stage_b.py modules_served: {sb['per_set']} pooled {sb['pooled']} certified_candidate {sb['certified_candidate']}")
src = open(os.path.join(RIG, "code", "second_marker.py")).read()
print(f"second_marker.py collect calls from_the_record: {'from_the_record' in src}")
