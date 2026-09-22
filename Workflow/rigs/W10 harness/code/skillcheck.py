"""The skill copy is diffed against the authority before every call (Lesson 44, W10 section 3 A1).

A RULE with two small driver commands:
  python3 skillcheck.py --check     # compares the copy with HV file 33; prints and exits non-zero on a difference
  python3 skillcheck.py --sync      # copies the authority into the rig's copy (the only write it makes)

check() is called by every driver before every call it makes, not once per batch.
What would show this design wrong: a run record whose skill_check field is absent, or a call
made after a difference was found. Both are visible in the run record, which carries the digest
of every one of the eight files as sent.
"""
import os, sys, filecmp, shutil, hashlib
from rig import AUTHORITY_SKILL, SKILL_COPY, SKILL_FILES, SKILL_FILE, MODULES


def digests():
    out = {}
    for f in SKILL_FILES:
        p = os.path.join(SKILL_COPY, f)
        with open(p, "rb") as fh:
            out[f] = hashlib.sha256(fh.read()).hexdigest()[:16]
    return out


def check():
    """Raise unless the copy is file 33 exactly. Returns the digest of every file as sent."""
    if not os.path.isdir(SKILL_COPY):
        raise SystemExit(f"no skill copy at {SKILL_COPY}; run `python3 skillcheck.py --sync` first. Nothing sent.")
    missing = [f for f in SKILL_FILES if not os.path.exists(os.path.join(SKILL_COPY, f))]
    if missing:
        raise SystemExit(f"skill copy is missing {missing}. Nothing sent.")
    bad = [f for f in SKILL_FILES
           if not filecmp.cmp(os.path.join(SKILL_COPY, f), os.path.join(AUTHORITY_SKILL, f), shallow=False)]
    if bad:
        raise SystemExit(f"skill copy differs from HV file {SKILL_FILE} in {bad}. Nothing sent.")
    return digests()


def sync():
    if os.path.isdir(SKILL_COPY):
        shutil.rmtree(SKILL_COPY)
    shutil.copytree(AUTHORITY_SKILL, SKILL_COPY)
    return SKILL_COPY


def skill_main():
    with open(os.path.join(SKILL_COPY, "SKILL.md"), encoding="utf-8") as f:
        return f.read().strip()


def module_text(name):
    if name not in MODULES:
        return f"no file named {name!r}"
    with open(os.path.join(SKILL_COPY, "references", f"{name}.md"), encoding="utf-8") as f:
        return f.read()


def skill_all():
    out = [f"=== FILE: hard-to-vary/SKILL.md ===\n{skill_main()}\n"]
    for m in MODULES:
        out.append(f"=== FILE: hard-to-vary/references/{m}.md ===\n{module_text(m).strip()}\n")
    return "\n".join(out)


if __name__ == "__main__":
    if "--sync" in sys.argv:
        print(f"copied HV file {SKILL_FILE} to {sync()}")
    d = check()
    print(f"skill copy checked against HV file {SKILL_FILE}: {len(d)} files identical")
    for f, h in d.items():
        print(f"  {h}  {f}")
