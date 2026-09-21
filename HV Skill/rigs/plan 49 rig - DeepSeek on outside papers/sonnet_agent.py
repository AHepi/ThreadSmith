"""Addendum H61: the Sonnet 5 arm through Claude Code subagents (the session's Workflow tool, model pinned to Sonnet).
  python3 sonnet_agent.py prompts <scratch>    # writes prompt files and the skill copy under <scratch>/sonnet[_31]/
  python3 sonnet_agent.py wrap <scratch>       # wraps each reply file into runs_sonnet5[_31]/<sid>-m<mode>-r<k>.json
The skill version comes from SKILL_FILE (30 or 31), as in run.py. Sends nothing itself."""
import os, sys, json, shutil, time, re
from run import HERE, MODULES, FRAMING, SKILL, SKILL_FILE, _SUF, skill_all, source_text, check_skill

JOBS = [(s, m, k) for s in ("P3", "F4") for m in (1, 2) for k in (1, 2, 3)]
TOOLS_M1 = ("You are a reader under test. This file is your whole instruction. Use no tool except Write, once, to save "
            "your report at the output path named at the end of this file. Read no other file, run nothing, search "
            "nothing. Your working directory is irrelevant.\n\n")
TOOLS_M2 = ("You are a reader under test. This file is your whole instruction. The method below names reference files; "
            "they are in the folder {refs} as <name>.md, and you open one with the Read tool when the method's own table "
            "and map say to open it, and only then. Use no other tool except Write, once, to save your report at the "
            "output path named at the end of this file. Read no file outside that folder, run nothing, search nothing. "
            "Your working directory is irrelevant.\n\n")

def joined(text):
    """Join line breaks inside paragraphs so the prompt file reads in one call; paragraph breaks kept."""
    return "\n\n".join(re.sub(r"\s*\n\s*", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip())

def prompts(scratch):
    check_skill()
    base = f"{scratch}/sonnet{_SUF}"
    os.makedirs(f"{base}/prompts", exist_ok=True); os.makedirs(f"{base}/replies", exist_ok=True)
    refs = f"{base}/hard-to-vary/references"
    if os.path.isdir(f"{base}/hard-to-vary"): shutil.rmtree(f"{base}/hard-to-vary")
    shutil.copytree(SKILL, f"{base}/hard-to-vary")
    skill_main = open(f"{SKILL}/SKILL.md", encoding="utf-8").read().strip()
    for s, m, k in JOBS:
        out = f"{base}/replies/{s}-m{m}-r{k}.md"
        if m == 1:
            body = TOOLS_M1 + FRAMING + skill_all()
        else:
            body = TOOLS_M2.format(refs=refs) + FRAMING + f"=== FILE: hard-to-vary/SKILL.md ===\n{skill_main}\n"
        body += f"\n\n=== THE DOCUMENT TO JUDGE ===\n\n{joined(source_text(s))}\n\n=== END OF DOCUMENT ===\n\n"
        body += f"Output path for your report (use Write, once, the report only): {out}\n"
        p = f"{base}/prompts/{s}-m{m}-r{k}.txt"
        open(p, "w", encoding="utf-8").write(body)
        print(f"{os.path.relpath(p, scratch)}\t{len(body.split())} words\t{body.count(chr(10))+1} lines")

def wrap(scratch, meta_path=None):
    base = f"{scratch}/sonnet{_SUF}"
    meta = json.load(open(meta_path)) if meta_path and os.path.exists(meta_path) else {}
    outdir = f"{HERE}/runs_sonnet5{_SUF}"; os.makedirs(outdir, exist_ok=True)
    for s, m, k in JOBS:
        rp = f"{base}/replies/{s}-m{m}-r{k}.md"
        if not os.path.exists(rp): print(f"MISSING {rp}"); continue
        reply = open(rp, encoding="utf-8").read()
        rec_meta = meta.get(f"{s}-m{m}-r{k}", {})
        rec = {"source": s, "mode": m, "repeat": k, "skill_file": SKILL_FILE,
               "model": "sonnet (Claude Code Workflow tool; expected claude-sonnet-5, not verified)",
               "transport": "claude-code-workflow-agent", "effort": "high",
               "reply": reply, "reasoning": "", "reasoning_kept": False,
               "modules_opened": rec_meta.get("modules_opened", []), "modules_self_reported": True,
               "reader_reported_words": rec_meta.get("words"),
               "finish_reasons": [None], "automatic_retries": 0, "usage_total": {},
               "seconds": None, "finished_at": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(rp)))}
        op = f"{outdir}/{s}-m{m}-r{k}.json"
        json.dump(rec, open(op, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"{os.path.relpath(op, HERE)}\t{len(reply.split())} words\tmodules {rec['modules_opened']}")

if __name__ == "__main__":
    cmd, scratch = sys.argv[1], sys.argv[2]
    if cmd == "prompts": prompts(scratch)
    else: wrap(scratch, sys.argv[3] if len(sys.argv) > 3 else None)
