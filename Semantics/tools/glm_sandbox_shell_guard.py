#!/usr/bin/env python3
"""glm_sandbox_shell_guard.py: the only way a sandboxed GLM call can run a command (round 3 of the review rounds, log
S105; written 28 September 2026 by a Claude subagent for the orchestrator).

tools/glm_via_claude_code_sandboxed.py sets Claude Code's CLAUDE_CODE_SHELL_PREFIX to this file. Claude Code then hands
every command its Bash tool would run to this file, as one argument: the whole shell line it would otherwise give to a
shell (`source <snapshot> ... && eval <command, quoted> < /dev/null && pwd -P >| <tmp>/claude-<hex>-cwd`; observed with
Claude Code 2.1.283; <tmp> is the call's TMPDIR, GLM_SANDBOX_TMP, which the sandboxed helper puts in the scratchpad). This file never starts a shell. It takes the quoted command out of that line and runs it only if
the command, character for character, is

    python3 -m model.run [--claim FCnn[.newN]]... [--scale N] [--time-cap N] [--brief] [--help]

(letters, digits, dots, hyphens and single spaces only: no quoting, no variable, no glob, no substitution, no
redirection, no chaining). Then it runs /usr/local/bin/python3 -B -s -m model.run with those arguments and --no-write,
in the sandbox folder (GLM_SANDBOX_DIR; the current folder must be it), with a clean environment (PATH, LANG, LC_ALL,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, PYTHONNOUSERSITE=1: the key and every other variable of the call are not
passed on). --scale is capped at 4 and --time-cap at 60 (the settings of the round-2 whole-suite runs are 4 and 45).
Anything else is refused with one fixed line; nothing of it runs. Every command handed here, run or refused, is logged
as one JSON line to GLM_SANDBOX_GUARD_LOG (outside the sandbox). Before running, the sandbox path is written to the
cwd file Claude Code names (<tmp>/claude-<hex>-cwd, which must lie directly in GLM_SANDBOX_TMP), which Claude Code reads
to track the working folder.
"""
import json, os, re, shlex, sys, time

PY = "/usr/local/bin/python3" if os.access("/usr/local/bin/python3", os.X_OK) else "/usr/bin/python3"
TAIL = re.compile(r" && eval (?P<cmd>.+) < /dev/null && pwd -P >\| (?P<cwdf>/[^\s'\"]*/claude-[0-9a-f]+-cwd)\Z", re.S)
ARG = r"(?:--claim FC[0-9]{1,3}(?:\.new[0-9])?|--scale [0-9]{1,2}(?:\.[0-9]{1,3})?|--time-cap [0-9]{1,3}(?:\.[0-9]{1,3})?|--brief|--help|-h)"
COMMAND = re.compile(r"python3 -m model\.run(?: %s)*" % ARG)
CAPS = {"--scale": 4.0, "--time-cap": 60.0}
REFUSAL = ("refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N "
           "(at most 4), --time-cap N (at most 60), --brief or --help, typed plainly from the sandbox folder; nothing "
           "else was run")


def log(entry):
    path = os.environ.get("GLM_SANDBOX_GUARD_LOG")
    if not path:
        return
    entry["t"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def refuse(why, shown):
    log({"decision": "refused", "why": why, "command": shown[:500]})
    print(REFUSAL)
    sys.exit(126)


def main():
    line = sys.argv[1] if len(sys.argv) == 2 else ""
    sandbox = os.path.realpath(os.environ.get("GLM_SANDBOX_DIR") or "/nonexistent")
    m = TAIL.search(line)
    if not line.startswith("source ") or not m:
        refuse("not the shell line Claude Code builds", line[-300:])
    try:
        parts = shlex.split(m.group("cmd"))
    except ValueError:
        refuse("the command does not parse", m.group("cmd"))
    if len(parts) != 1:               # Claude Code quotes the command as one word for eval
        refuse("the command is not one quoted word", m.group("cmd"))
    cmd = parts[0]
    if not COMMAND.fullmatch(cmd):
        refuse("not the one command allowed", cmd)
    if os.path.realpath(os.getcwd()) != sandbox or not os.path.isdir(os.path.join(sandbox, "model")):
        refuse("not run from the sandbox folder", cmd)
    args = cmd.split(" ")[3:]
    for i, a in enumerate(args[:-1]):
        if a in CAPS and float(args[i + 1]) > CAPS[a]:
            refuse("%s above its cap %s" % (a, CAPS[a]), cmd)
    tmp = os.path.realpath(os.environ.get("GLM_SANDBOX_TMP") or "/tmp")
    if os.path.dirname(os.path.realpath(m.group("cwdf"))) != tmp:
        refuse("the cwd file is not in the call's temporary folder", cmd)
    with open(m.group("cwdf"), "w") as f:
        f.write(sandbox)
    argv = [PY, "-B", "-s", "-m", "model.run"] + args + ([] if ("--help" in args or "-h" in args) else ["--no-write"])
    log({"decision": "run", "command": cmd, "argv": argv[1:]})
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PYTHONHASHSEED": "0",
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1"}
    sys.stdout.flush()
    os.execve(PY, argv, env)


if __name__ == "__main__":
    main()
