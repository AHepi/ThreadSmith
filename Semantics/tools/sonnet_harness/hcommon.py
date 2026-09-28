#!/usr/bin/env python3
"""What every script of the Sonnet harness shares (log S105, decision S42).

Every script prints ONE JSON object on stdout and exits 0 when its own "ok" is true, 1 when it is false, and 2 when it
refused to run (bad input, a path it may not touch). No script weighs an argument, rules on a finding or writes maths:
each computes, copies or compares, and says what it found.

Paths. A script reads anything in the repository except key files. It writes only
  - under the harness's test folder in the scratchpad (TEST_ROOT), or anywhere in the scratchpad, or
  - a NEW file inside Semantics/ when the script's own flag allows it (never over an existing file, never in
    authority/ or records/, never in .git/).
Standard library only.
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.abspath(os.path.join(HERE, "..", ".."))
REPO = os.path.dirname(SEM)
SCRATCH = os.environ.get("SONNET_HARNESS_SCRATCH",
                         "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad")
TEST_ROOT = os.path.join(SCRATCH, "sonnet_harness_tests")

# Any path that looks like a key file is refused, for reading and for writing. The scripts never print a key.
KEYLIKE = re.compile(r"(\.env$|keys?\.env|cross_examiner_keys|credential|secret|/\.claude(/|$)|/\.ssh(/|$))", re.I)
NO_WRITE_IN_SEM = ("authority", "records", ".git")

# Words outside formulas: the rule of round 2's appliers ("apply text changes.py"): \( \) and \[ \] stripped.
MATH = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.S)
BOLD = re.compile(r"\*\*(.+?)\*\*")
TAG = re.compile(r"\\tag\{[^}]*\}")
S95_SCRIPT = os.path.join(SEM, "tests", "S95 Scrub - scripts", "scrub_apply.py")
S96_SCRIPT = os.path.join(SEM, "tests", "S96 Repair - scripts", "repair_apply.py")
# Decision S23's forbidden families, as round 2's appliers list them.
S23_FORBIDDEN = {"reason to believe/reject", "better/worse than", "not true / more true", "fit", "support", "verify",
                 "corroborate", "disprove", "prove/proof", "true/truth", "establish", "authority", "foundation",
                 "derive", "belief"}


def emit(obj, code=None):
    """Print the one JSON object and exit: 0 if obj['ok'], else 1 (or the code given)."""
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")
    sys.stdout.flush()
    sys.exit(code if code is not None else (0 if obj.get("ok") else 1))


def refuse(msg, **kw):
    emit(dict(ok=False, refused=msg, **kw), 2)


def real(p):
    return os.path.realpath(os.path.abspath(p))


def inside(p, root):
    p, root = real(p), real(root)
    return p == root or p.startswith(root + os.sep)


def guard_read(p):
    if KEYLIKE.search(real(p)) or KEYLIKE.search(os.path.abspath(p)):
        refuse("refused to read a path that looks like a key file or a config folder: %s" % os.path.basename(p))
    if not os.path.exists(p):
        refuse("no such file: %s" % p)
    return p


def guard_write(p, allow_new_in_sem=False):
    """Refuse unless p may be written: in the scratchpad; or, with allow_new_in_sem, a new file in Semantics/."""
    if KEYLIKE.search(real(p)):
        refuse("refused to write a path that looks like a key file or a config folder")
    if inside(p, SCRATCH):
        return p
    if allow_new_in_sem and inside(p, SEM):
        rel = os.path.relpath(real(p), real(SEM)).split(os.sep)
        if rel[0] in NO_WRITE_IN_SEM:
            refuse("refused to write in Semantics/%s/" % rel[0])
        if os.path.exists(p):
            refuse("refused to write over an existing file: %s" % os.path.relpath(p, SEM))
        return p
    refuse("refused to write outside the scratchpad: %s" % p)


def md5_bytes(b):
    return hashlib.md5(b).hexdigest()


def md5_file(p):
    guard_read(p)
    with open(p, "rb") as f:
        return md5_bytes(f.read())


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def read_text(p):
    guard_read(p)
    with open(p, "rb") as f:
        return f.read().decode("utf-8")


def write_text(p, text, allow_new_in_sem=False):
    guard_write(p, allow_new_in_sem)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    tmp = p + ".tmp.%d" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, p)


def write_json(p, obj, allow_new_in_sem=False):
    write_text(p, json.dumps(obj, ensure_ascii=False, indent=1) + "\n", allow_new_in_sem)


def load_json(p):
    return json.loads(read_text(p))


def run(argv, cwd=None, timeout=600, env_extra=None, clean_env=True):
    """Run argv (a list; never a shell string) with a deadline on the whole call. With clean_env (the default) the
    environment passed on is the caller's minus every variable whose name says key, token, secret or password; only
    git (git_commit.py) runs with the whole environment, because its proxy settings live there."""
    env = dict(os.environ)
    if clean_env:
        # GIT_CONFIG_COUNT/KEY_n/VALUE_n go together: dropping only the KEY_n names would break git (exit 128)
        env = {k: v for k, v in env.items() if not re.search(r"KEY|TOKEN|SECRET|PASSWORD|^GIT_CONFIG_", k, re.I)}
    env.update(env_extra or {})
    t0 = time.time()
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, timeout=timeout)
        return dict(exit=p.returncode, seconds=round(time.time() - t0, 1), timed_out=False,
                    stdout=p.stdout.decode("utf-8", "replace"), stderr=p.stderr.decode("utf-8", "replace"))
    except subprocess.TimeoutExpired as e:
        return dict(exit=None, seconds=round(time.time() - t0, 1), timed_out=True,
                    stdout=(e.stdout or b"").decode("utf-8", "replace"), stderr=(e.stderr or b"").decode("utf-8", "replace"))


def load_module(path, name):
    guard_read(path)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


def prose(s):
    """The words outside formulas, as round 2's appliers count them."""
    return MATH.sub(" ", s).split()


def rel(p):
    """A path inside the repository relative to its root; any other path absolute."""
    return os.path.relpath(real(p), real(REPO)) if inside(p, REPO) else real(p)
