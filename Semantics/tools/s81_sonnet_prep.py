#!/usr/bin/env python3
"""s81_sonnet_prep.py: build the working folders and prompts for Stage 1 of round S81, second version (plan
`tests/S81 Plan - second version, Sonnet testers and API auditors.md`, decision S15). Stage 1 is run by two independent
Sonnet subagent testers, A and B, each doing the three calls 1C, 1K and 1D as three separate fresh agents: six agents.

  python Semantics/tools/s81_build.py build                        # first: the exact texts, in <OUT>/briefs/
  python Semantics/tools/s81_sonnet_prep.py                        # attempt 1 for all six agents
  python Semantics/tools/s81_sonnet_prep.py --attempt 2 A2 ...     # the one rerun of a voided or incomplete run

Agent tags. The tag names the agent's folder, and the agent sees its folder's path, so the tag says nothing of arm or
version: a tester letter and a call number.
  A1 = s81_1C_A   A2 = s81_1K_A   A3 = s81_1D_A        (tester A)
  B1 = s81_1C_B   B2 = s81_1K_B   B3 = s81_1D_B        (tester B)
A rerun is <tag>-2 (A2-2), in a fresh folder.

Each folder is OUTSIDE the repository, <RUNS>/<tag>/, and holds only brief.md: the exact user text the API version
would have sent (<OUT>/briefs/<s81 tag>.txt, rebuilt here from the frozen sources and compared byte for byte). The
agent writes return.md there. The prompt for each agent goes to <RUNS>/_prompts/<tag>.txt, and the map from tag to
folder, call and hashes to <RUNS>/_prompts/MAP.json; neither is in any agent's folder. RUNS defaults to the session
scratchpad's s81runs/ and can be set with S81_RUNS. Nothing is sent anywhere by this script.
"""
import hashlib, json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s81_build as B

RUNS = os.environ.get("S81_RUNS",
                      "/tmp/claude-0/-home-user-ThreadSmith/b7f93a41-2fef-58bf-8052-3a6eefa05845/scratchpad/s81runs")
PROMPTS = os.path.join(RUNS, "_prompts")
MAP = os.path.join(PROMPTS, "MAP.json")
AGENTS = {"A1": "s81_1C_A", "A2": "s81_1K_A", "A3": "s81_1D_A",
          "B1": "s81_1C_B", "B2": "s81_1K_B", "B3": "s81_1D_B"}
SENTINEL = "END OF REPORT"
# Words the prompt must not carry: the build's call-text checks, the collector's void strings, and any word naming an
# arm, a version or the tester's role. Identifiers are matched as written, words in any case; whole words only.
PROMPT_FORBID_IDS = ["S81", "S76", "S75", "R2", "O48", "O24", "Revision 1"]
PROMPT_FORBID_WORDS = ["O48 change", "file 10", "file 11", "Semantics results", "prediction", "control", "arm",
                       "version", "revision", "tester", "Sonnet", "round"]

PROMPT = """Your working folder is {F}. It holds one file, {F}/brief.md: a task, followed by the texts the task works on.

Read {F}/brief.md from its first line to its last, and carry out its task exactly as it says. The file is long: read it with the Read tool in parts, about 300 lines at a time, using offset and limit, until you have read every line.

Work from brief.md alone. Use absolute paths inside {F} only, and open no other file or folder. The Read, Write and Edit tools are all the task needs.

Write your whole answer, in exactly the form brief.md asks for, to {F}/return.md. A long answer may be written in parts: the first part with the Write tool, and each later part added at the end of return.md. The last line of return.md is the brief's closing line, on its own:
{S}

When return.md is complete, reply with the single word DONE.
"""


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def folder_tag(tag, attempt):
    return tag if attempt == 1 else "%s-%d" % (tag, attempt)


def prompt_for(folder):
    p = PROMPT.format(F=folder, S=SENTINEL)
    for w in PROMPT_FORBID_IDS:
        assert not re.search(r"\b%s\b" % re.escape(w), p), "the prompt carries %r" % w
    for w in PROMPT_FORBID_WORDS:
        assert not re.search(r"\b%s\b" % re.escape(w), p, re.I), "the prompt carries %r" % w
    return p


def expected_text(s81tag):
    """The call text as the build makes it now, from the frozen sources (md5-checked), and as it stands in briefs/."""
    b, secs = B.calls1()[s81tag]
    whole = B.joined(b, secs)
    path = os.path.join(B.BRIEFS, s81tag + ".txt")
    if not os.path.exists(path):
        raise SystemExit("%s missing: run `python Semantics/tools/s81_build.py build` first" % path)
    if B.read(path) != whole:
        raise SystemExit("%s differs from the text the build makes from the frozen sources" % path)
    assert SENTINEL in b, "the brief's closing line is missing"
    return whole


def build(tag, attempt, mp):
    s81tag = AGENTS[tag]
    ft = folder_tag(tag, attempt)
    folder = os.path.join(RUNS, ft)
    if os.path.exists(os.path.join(folder, "return.md")):
        print(ft, "already has a return; left as it is")
        return
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
    whole = expected_text(s81tag)
    with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as f:
        f.write(whole)
    assert sorted(os.listdir(folder)) == ["brief.md"]
    prompt = prompt_for(folder)
    ppath = os.path.join(PROMPTS, ft + ".txt")
    B.write(ppath, prompt)
    mp.setdefault(tag, {})[str(attempt)] = {
        "s81_tag": s81tag, "folder_tag": ft, "folder": folder, "prompt": ppath, "prompt_sha256": sha(prompt),
        "brief_sha256": sha(whole), "brief_words": len(whole.split()), "model": "sonnet (subagent)"}
    print("%-5s -> %-9s folder %s  brief %d words, sha256 %s" % (ft, s81tag, folder, len(whole.split()), sha(whole)[:12]))


def main(a):
    attempt, tags = 1, list(AGENTS)
    if a and a[0] == "--attempt":
        attempt, tags = int(a[1]), a[2:]
        if attempt != 2 or not tags or any(t not in AGENTS for t in tags):
            raise SystemExit("--attempt 2 TAG ... (one rerun only; tags %s)" % ", ".join(AGENTS))
    elif a:
        raise SystemExit(__doc__)
    mp = json.loads(B.read(MAP)) if os.path.exists(MAP) else {}
    for t in tags:
        if attempt == 2 and "1" not in mp.get(t, {}):
            raise SystemExit("%s has no first attempt to rerun" % t)
        build(t, attempt, mp)
    B.write(MAP, json.dumps(mp, indent=1))
    print("map:", MAP)


if __name__ == "__main__":
    main(sys.argv[1:])
