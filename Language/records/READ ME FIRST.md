# Language - the record of this thread

From 21 September 2026 the Language project keeps its own record here, in the same four files as the shared record at the repository root: project story (the log), Decisions (the owner's words), Lessons (only failures), Status (the summary). The owner asked for it after two chats, writing the one shared record at once, collided on an entry number twice in a day (shared log 58).

## How the two records relate
- **Before this folder existed**, everything about the language is in the shared record, which now sits in this same folder under its original name: the four files "Checked reasoning language - project story / Decisions / Lessons / Status", complete to log 59, and the read-me of the bundles they came in. Logs 01 to 44 there are the language, the rigs, the paragraphs and the rulebooks; the three Language entries made after the repository was set up, 45, 46 and 58, are copied into the project story here verbatim so it reads on its own; the copies are marked.
- **From here on**, a Language entry is written in this folder only. To keep the number readable against the shared sequence and still unable to collide with it, an entry here carries the letter L and the next number in the shared sequence at the time of writing: the first new entry here is L60, and a file made under it is named "L60 ...". The letter says the thread; the number says roughly when.
- **The shared record is not updated after 21 September.** It was moved into this folder from the repository root when the owner asked for nothing project-specific to sit outside the project folders; nothing in it was changed.

## Read in this order
1. This file.
2. **Language - Status.md**: the short summary, dated bullets, rebuilt from the log at each entry.
3. **Language/authority/L64 Scope - the contract the language claims, second version.md**: the contract every test since L65 is run under, and "L77 Table for the owner" in tests/, which says what each check computes.
4. **Language - project story.md**: the log, L60 onward; "What each patch gave up" is in the shared story beside it, from log 21.
5. The latest plan and results in `tests/` and `results/` (the numbers in Status): as of 23 September, plan L82 (fourteenth version) and results L84 with its two markings, then "L76 Method review" for how the method itself was tested, and `records/Language - Handover log.md` for where things stand between entries.
6. `/RESEARCH-CONVENTIONS.md` at the repository root: the rules this record keeps.

## Terms and names a fresh reader needs
- **The language** is file 38; **the translator's task** is file 39; the theory they rest on is file 11 (Semantics/authority). A **ledger** is a text translated into numbered lines, each with a **standing** (CLAIMED what the sentence asserts; GIVEN what it takes for granted; SUPPOSED in a named what-if case; TOLD in a named world, what a story, note or report says), a content of one of fourteen kinds (a **Thing line** names a thing and its response to a press; BECAUSE claims a cause; SINCE claims a reason to expect; MAKES and SHOWS are the two kinds of general line; a **what-if** withdraws a line or makes a fact not so), a mark (said, filled in, usual case) and a sentence number. What the language cannot write goes to **the bin**; the **gauge** at the foot of a report counts marks and bin entries.
- **The rigs**: rig 1 (arguments, `run_check.py` and `checker_rules.pl`) and rig 2 (causes, `check2.py` and `laws.pl`), on s(CASP). **Findings** a report prints: contradiction, follows, jump, circle, no connection, cannot tell, a what-if holds or fails, and others listed in 38 line 111.
- **The four sources of error** (decision L4): the text is out of scope; the translator (a language model) erred; the checker erred; the read-back from report to prose erred. L64 section 6 is their table.
- **F04, F09, F15** are findings of the other model's audit of 38 and 39 (results 45), numbered there; F09 (an actual fact rides into a what-if) and F15 (a BECAUSE and its exact denial raise no contradiction) are confirmed failures of the language, held for the owner's word. **R06** and **"02"** are items from that audit the owner has not ruled on; both are defined in results 45.
- **Astra Pro** and **Astra Ultra** (decision L9) are the two outside agents: Pro reads and audits and cannot execute; Ultra executes and returns zips, with no repository attached. Both are fresh every time.
- **The instruments**: `tools/sameness.py` (compares two ledgers by wording), `tools/consequences.py` (what follows from a ledger, and what changes when a line is removed), the gauge, the read-back test (a reader given reports only), and the blind plants of L66.

## Traps
- Reading the project story here as the whole history of the language. Logs 01 to 44 are in the shared files beside it and are not copied into it.
- Editing a copied entry. The copies are the shared record's text; a correction is a new entry.
- Numbering a new file by the shared record's last number alone. Use this log's L-number.
