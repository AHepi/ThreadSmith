"""Build the audit bundle (decision H2): a zip with everything an outside auditor needs.
Contents: AUDIT-BRIEF.md (the H60 brief), conventions/ (the repository root's general files and tutorials),
HV Skill/ (this project as committed, minus fetched texts, skill copies and caches), shared-history/
(the shared record the projects began with, unchanged). Nothing is rewritten; files are copied as they are.

  python3 make_audit_bundle.py [out.zip]
"""
import os, sys, zipfile, fnmatch
HERE = os.path.dirname(os.path.abspath(__file__))          # HV Skill/rigs
PROJ = os.path.normpath(f"{HERE}/..")                        # HV Skill
ROOT = os.path.normpath(f"{PROJ}/..")                        # repository root
BRIEF = f"{PROJ}/tests/H60 Audit brief - for an adversarial audit of the HV Skill project.md"
SKIP_DIRS = {"corpus", "raw", "skill", "__pycache__", ".git"}
SKIP_GLOBS = ["skill_*", "*.pyc", "*.tmp"]

def skip(name):
    return name in SKIP_DIRS or any(fnmatch.fnmatch(name, g) for g in SKIP_GLOBS)

def add_tree(z, src, dest):
    for root, dirs, files in os.walk(src):
        dirs[:] = sorted(d for d in dirs if not skip(d))
        for f in sorted(files):
            if skip(f): continue
            p = os.path.join(root, f)
            z.write(p, os.path.join(dest, os.path.relpath(p, src)))

out = sys.argv[1] if len(sys.argv) > 1 else f"{HERE}/HV Skill - audit bundle.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(BRIEF, "AUDIT-BRIEF.md")
    for f in ("README.md", "START-HERE.md", "RESEARCH-CONVENTIONS.md", "LEGEND.md", "GLOSSARY.md"):
        z.write(f"{ROOT}/{f}", f"conventions/{f}")
    add_tree(z, f"{ROOT}/tutorials", "conventions/tutorials")
    add_tree(z, PROJ, "HV Skill")
    for f in sorted(os.listdir(f"{ROOT}/Language/records")):
        if f.startswith("Checked reasoning language - "):
            z.write(f"{ROOT}/Language/records/{f}", f"shared-history/{f}")
    n = len(z.namelist())
print(f"wrote {out}: {n} files, {os.path.getsize(out)/1e6:.1f} MB")
