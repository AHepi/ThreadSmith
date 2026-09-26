"""Build the edited W38.1 block from the original by exact, counted replacements."""
import pathlib
S = pathlib.Path("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/rivals")
b = (S / "orig_W38.1.md").read_text(encoding="utf-8")

def rep(old, new, text):
    n = text.count(old)
    assert n == 1, (n, old[:80])
    return text.replace(old, new)

# 1. NEW: the Idle parts line, and the new Hard to vary line after it
b = rep(
"- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and how hard an account is to vary grades nothing (Part VI).\n",
"- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0 and VI).\n"
"- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it nowhere the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Three departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation able to fit anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and the remedy is a finer question. And variants whose differing details do no work, which he finds reduce to one core explanation (p.21), are here one account written two ways, not rivals (Derivation 2).\n",
b)

# 2. NEW: the Reach line
b = rep(
"- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the reach of an account is the set of jobs on which it is an account, fixed by the account and the world (Part VI).\n",
"- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Parts I and VI).\n",
b)

# 3. NEW: the Surprise and problems line
b = rep(
"Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.\n",
"Here surprise is kept for selected transports (Part IV). A problem for a question is narrower: two rivals that both fit what is established (Part VI). A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.\n",
b)

# 4. Heading / GROUP marker / CHECK line added
b = rep("- **GROUP:** M\n", "- **GROUP:** M; edited 25 September (group H)\n", b)
check_end = "The assembler also gave the fallback for \"Surprise and problems\" the corrected account of Deutsch's \"problem\", which check 2's fix (c) implies but did not write out.\n"
b = rep(check_end, check_end +
"  - **25 September:** four lines of NEW changed for W59.1 and the edits to W34.1 and W33.1, and the fallback table with them. *Idle parts* no longer says that how hard an account is to vary grades nothing, since Pres goes; it says that nothing grades a candidate for carrying a commitment that does no work. A line *Hard to vary* is added after it. *Reach* no longer gives a definition by jobs. *Surprise and problems* now names the problem for a question of Part VI and says that a problem in the wider sense \"can be\" a recognized difficulty, where it said \"is\", to agree with Part VI's \"can be\". Every other line is byte for byte as before. Checked by the drafter only; no outside reader has seen these lines.\n", b)

# 5. REASON bullet added (before the Named and not named bullet)
b = rep("  - **Named and not named.**",
"  - **25 September: hard to vary.** The owner's position of 24–25 September states hard-to-vary through rivals and problems (W59.1), and this note says so. Deutsch p.17 on problems as conflicts, p.16 on experiment between two viable theories, pp.20–22 on ease of variation (p.21, the southern variant and the one core of the Persephone and Freyr myths; p.22, an explanation that could explain anything), p.25 on rejection without experiment, and p.31 (glossary, good and bad explanation). Each page was checked with `sources/locate.py` on a phrase from the page. No book is quoted: the lines paraphrase. The departures recorded are the three that remain after the change: judgement before a rival is offered, the name of explanation kept for an account with an easy rival, and label-only variants read as one account. The *Surprise and problems* line changes \"is\" to \"can be\" for the wider sense, since Part VI now says a represented problem for a question \"can be\" a recognized difficulty, and \"is\" would contradict it.\n  - **Named and not named.**", b)

# 6. CASES AT RISK: add hard to vary guard rows
b = rep("idle parts (N1, N25), stated limits", "idle parts (N1, N25), hard to vary (N2, N3, N5, N25, O24), stated limits", b)

# 7. FALLBACKS rows
b = rep(
"  | Idle parts | C W33.1 (the words 'grades nothing'); the claim itself holds on file 11 |",
"  | Idle parts | C W33.1 (the words 'does no work by itself'); H W59.1 ('Nothing here … grades'); the claim itself holds on file 11 |", b)
b = rep(
"  | Reach | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |\n",
"  | Hard to vary | H W59.1 | - *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31). Here no measure of variation is stated and nothing is graded (Parts 0 and XIV). |\n"
"  | Reach | H W59.1 (the sentence on questions nobody has asked) | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not used, and whether a transport is faithful on a contract does not depend on anyone's accepting it (Part I). |\n"
"  | Reach, if W34.1 as edited is dropped | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |\n", b)
b = rep(
"  | Surprise and problems | C W35.1-W35.3 |",
"  | Surprise and problems, if W59.1 is dropped | H W59.1 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it. |\n"
"  | Surprise and problems | C W35.1-W35.3 |", b)
(S / "block_W38.1.md").write_text(b, encoding="utf-8")
print("ok", len(b))
