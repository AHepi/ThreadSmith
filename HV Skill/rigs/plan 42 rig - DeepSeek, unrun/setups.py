"""The four setups. Each differs from the one before in one thing only."""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
Q0 = "Is this a good explanation? Say why, in under 250 words."
SHAPE = ("Reply in this shape, in everyday words, in under 250 words. "
         "(1) The parts of the explanation that are claimed to do the work. "
         "(2) For each part, one sentence: what holds it in place, or what could take its place just as well. "
         "(3) The weakest part, and one change to the situation that would show whether it does any work. "
         "(4) Your verdict, one of: RELY ON IT / RELY ON IT FOR A NARROWER QUESTION, and say which / SET IT ASIDE.")
FRAME = "Below is a skill, as a set of files, and after it a case. Use the skill on the case."
FILES = ["SKILL.md", "references/the-idea-in-depth.md", "references/question-bank.md",
         "references/by-domain.md", "references/building.md", "references/testing-against-cases.md",
         "references/reporting.md", "references/word-list.md"]

def skill_text(folder):
    out = []
    for f in FILES:
        body = open(os.path.join(HERE, folder, "hard-to-vary", f), encoding="utf-8").read()
        out.append(f"=== FILE: hard-to-vary/{f} ===\n{body.strip()}\n")
    return "\n".join(out)

def prompt(setup, passage):
    case = "The case:\n\n" + passage.strip()
    if setup == 0:
        return case + "\n\n" + Q0
    if setup == 1:
        return case + "\n\n" + SHAPE
    folder = "skill_as_is" if setup == 2 else "skill_with_line"
    return FRAME + "\n\n" + skill_text(folder) + "\n=== END OF SKILL ===\n\n" + case + "\n\n" + SHAPE

if __name__ == "__main__":
    for s in range(4):
        p = prompt(s, "Example passage.")
        print(s, len(p.split()), "words")
    a, b = prompt(2, "x"), prompt(3, "x")
    print("setup 3 minus setup 2:", len(b.split()) - len(a.split()), "words")
