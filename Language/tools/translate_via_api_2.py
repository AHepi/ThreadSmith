#!/usr/bin/env python3
"""translate_via_api_2.py: one text, one outside model, one ledger pair the rig can run.

Assembles the translator's prompt (the task 39, the language L80, the encoding guide with its three
examples, the text), calls ask_model.py, extracts the ```json block, builds ledger_<id>.json and
ledger_<id>.pl, validates them (JSON fields; every clause guarded by its own line; the old driver runs
without a Prolog error), and on a validation failure asks once more with the failure appended.

Usage: translate_via_api_2.py PROVIDER TEXT_ID TEXT_FILE OUT_DIR
       translate_via_api_2.py --rebuild PROVIDER TEXT_ID OUT_DIR RESPONSE_FILE   (no call; rebuild and validate from a saved response)
Writes OUT_DIR/<id>.<provider>.translation.md (the whole response), OUT_DIR/ledger_<id>_<provider>.json/.pl,
OUT_DIR/<id>.<provider>.validation.txt, and the ask_model receipts. Keys from the environment.
Written under decision L11, 22 September 2026.

Second version (translate_via_api_2.py), 22 September 2026, kept beside translate_via_api_2.py (284be80d1703b60f). Give-up
line: the first version called ask_model.py, whose non-streaming request died at 301 s on every Atria attempt of the first
Arm B run; this version calls ask_model_2.py (streamed) and is otherwise the same file. Its output names are unchanged.
"""
import json, os, re, subprocess, sys, tempfile, shutil, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
LANG = os.path.join(HERE, "..")
BRIEF = os.path.join(LANG, "tests", "L82 Arm B corpus brief")
FILES = {
    "task": os.path.join(LANG, "authority", "39 Prompt - translate a text into the ledger language.md"),
    "language": os.path.join(LANG, "authority", "L80 The ledger language - complete definition, second version.md"),
    "guide": os.path.join(BRIEF, "ENCODING GUIDE for translators.md"),
}
RIG = os.path.join(LANG, "rigs", "rig 1 - arguments")

def prompt(text_id, text):
    parts = ["You are the translator. Below are, in order: the translator's task (file 39); the language definition (L80); the encoding guide with three examples; and the text. Read all of them, then do the task on the text and print exactly what the task and the guide ask for, ending with the JSON block and then the words TRANSLATION COMPLETE.\n"]
    for k in ("task", "language", "guide"):
        parts.append("\n\n===== %s =====\n" % os.path.basename(FILES[k]) + open(FILES[k]).read())
    for ex in ("example_T10D.json", "example_P14.json", "example_A.json", "example_A.pl"):
        parts.append("\n\n===== %s =====\n" % ex + open(os.path.join(BRIEF, ex)).read())
    parts.append("\n\n===== THE TEXT TO TRANSLATE: %s =====\n" % text_id + text + "\n")
    return "".join(parts)

def extract_json(response):
    m = re.search(r"```json\s*(\{.*?\})\s*```", response, re.S)
    if not m:
        m = re.search(r"(\{.*\})", response, re.S)
    if not m: raise ValueError("no JSON block found")
    return json.loads(m.group(1))

def build_pl(led, text_id, provider):
    out = ["%% ledger_%s_%s.pl - built by translate_via_api_2.py from the model's JSON (%s). Standing and marks are in the JSON." % (text_id, provider, provider)]
    for lid, info in led["lines"].items():
        out.append("line(%s)." % lid)
        for c in info.get("prolog_clauses", []):
            c = c.strip()
            if not c.endswith("."): c += "."
            out.append(c)
    return "\n".join(out) + "\n"

def validate(led, pl_text, json_path, pl_path):
    problems = []
    for k in ("paragraph", "sentences", "lines", "bin", "leftover", "whatifs"):
        if k not in led: problems.append("missing field: %s" % k)
    for lid, info in led.get("lines", {}).items():
        for k in ("mark", "sentence", "standing", "text"):
            if k not in info: problems.append("line %s lacks %s" % (lid, k))
        if info.get("mark") not in ("said", "filled in", "usual case"): problems.append("line %s: mark must be said / filled in / usual case" % lid)
        if not isinstance(info.get("sentence"), int): problems.append("line %s: sentence must be an integer" % lid)
        st = str(info.get("standing", ""))
        if st.startswith("TOLD") or st.startswith("SUPPOSED"):
            if not info.get("case") or info.get("case_kind") not in ("told", "supposed"): problems.append("line %s: TOLD/SUPPOSED needs case and case_kind" % lid)
        for c in info.get("prolog_clauses", []):
            body = c.split(":-", 1)[1] if ":-" in c else ""
            if not re.search(r"\bline\(%s\)" % re.escape(lid), body): problems.append("line %s: clause not guarded by line(%s): %s" % (lid, lid, c[:80]))
    covered = set(int(i.get("sentence")) for i in led.get("lines", {}).values() if isinstance(i.get("sentence"), int))
    covered |= set(int(b.get("sentence")) for b in led.get("bin", []) if isinstance(b.get("sentence"), int))
    for s in led.get("sentences", {}):
        if int(s) not in covered: problems.append("sentence %s reaches neither a line nor the bin" % s)
    # run the old driver on a scratch copy of the rig for a Prolog syntax check
    tmp = tempfile.mkdtemp(prefix="l82_validate_")
    try:
        shutil.copytree(RIG, os.path.join(tmp, "rig"))
        shutil.copy(json_path, os.path.join(tmp, "rig", "ledger_V.json")); shutil.copy(pl_path, os.path.join(tmp, "rig", "ledger_V.pl"))
        r = subprocess.run([sys.executable, "patched/run_check.py", "ledger_V.pl", os.path.join(tmp, "raw.txt")], cwd=os.path.join(tmp, "rig"), capture_output=True, text=True, timeout=600)
        raw = open(os.path.join(tmp, "raw.txt")).read() if os.path.exists(os.path.join(tmp, "raw.txt")) else ""
        if r.returncode != 0: problems.append("driver failed: " + (r.stderr[-800:] or r.stdout[-800:]))
        for bad in ("syntax error", "Syntax error", "syntax_error"):
            if bad in raw: problems.append("Prolog syntax error in the ledger (see raw log): " + raw[raw.find(bad)-200:raw.find(bad)+200].replace("\n", " "))
        report = r.stdout
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return problems, report

def rebuild(provider, text_id, out_dir, response_path):
    """Rebuild the ledger pair from a saved response (no call). Returns 0 when valid."""
    response = open(response_path).read()
    open(os.path.join(out_dir, "%s.%s.translation.md" % (text_id, provider)), "w").write(response)
    led = extract_json(response)
    json_path = os.path.join(out_dir, "ledger_%s_%s.json" % (text_id, provider)); pl_path = os.path.join(out_dir, "ledger_%s_%s.pl" % (text_id, provider))
    led.setdefault("paragraph", text_id); led["whose"] = "%s, under L82" % provider
    json.dump(led, open(json_path, "w"), indent=1, ensure_ascii=False)
    pl_text = build_pl(led, text_id, provider); open(pl_path, "w").write(pl_text)
    problems, report = validate(led, pl_text, json_path, pl_path)
    open(os.path.join(out_dir, "%s.%s.validation.txt" % (text_id, provider)), "w").write("rebuilt from %s\n%s\n\n--- old driver's report on this ledger ---\n%s" % (response_path, "\n".join(problems) or "VALID", report))
    print("%s %s: %s (%d lines)" % (provider, text_id, "valid" if not problems else "INVALID: " + "; ".join(problems)[:300], len(led["lines"])))
    return 0 if not problems else 1

def main():
    if sys.argv[1] == "--rebuild":
        return rebuild(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    provider, text_id, text_file, out_dir = sys.argv[1:5]
    attempts = 2
    os.makedirs(out_dir, exist_ok=True)
    text = open(text_file).read()
    user_path = os.path.join(out_dir, "%s.%s.prompt.txt" % (text_id, provider))
    open(user_path, "w").write(prompt(text_id, text))
    feedback = ""
    for attempt in range(1, attempts + 1):
        if feedback: open(user_path, "w").write(prompt(text_id, text) + "\n\n===== YOUR PREVIOUS ANSWER DID NOT VALIDATE =====\n" + feedback + "\nPrint the whole output again, corrected.\n")
        tag = "%s.%s.attempt%d" % (text_id, provider, attempt)
        rc = subprocess.run([sys.executable, os.path.join(HERE, "ask_model_2.py"), provider, "--user", user_path, "--out", out_dir, "--tag", tag, "--max-tokens", "60000", "--temperature", "0.2"]).returncode
        if rc != 0: feedback = "the call failed"; continue
        response = open(os.path.join(out_dir, tag + ".response.txt")).read()
        open(os.path.join(out_dir, "%s.%s.translation.md" % (text_id, provider)), "w").write(response)
        try: led = extract_json(response)
        except Exception as e:
            feedback = "Could not read a JSON block from your answer: %s" % e; continue
        json_path = os.path.join(out_dir, "ledger_%s_%s.json" % (text_id, provider)); pl_path = os.path.join(out_dir, "ledger_%s_%s.pl" % (text_id, provider))
        led.setdefault("paragraph", text_id); led["whose"] = "%s, under L82" % provider
        json.dump(led, open(json_path, "w"), indent=1, ensure_ascii=False)
        pl_text = build_pl(led, text_id, provider); open(pl_path, "w").write(pl_text)
        problems, report = validate(led, pl_text, json_path, pl_path)
        open(os.path.join(out_dir, "%s.%s.validation.txt" % (text_id, provider)), "w").write("attempt %d\n%s\n\n--- old driver's report on this ledger ---\n%s" % (attempt, "\n".join(problems) or "VALID", report))
        if not problems:
            print("%s %s: valid on attempt %d (%d lines)" % (provider, text_id, attempt, len(led["lines"]))); return 0
        feedback = "\n".join("- " + p for p in problems)
        print("%s %s: attempt %d invalid: %s" % (provider, text_id, attempt, "; ".join(problems)[:300]))
    return 1

if __name__ == "__main__": sys.exit(main())
