"""check_ledger.py - checks a falsifier ledger written with the prove-it-wrong skill.

What this file does: reads a Markdown file and checks that its falsifier ledger is
complete and consistent, so that no forcing question is skipped silently, no claim
is called checked without a record of what was run, and the answers agree with the
falsifier rows they cite. It prints every problem in plain words and exits with 0
when the ledger passes, 1 when it does not.

Usage:  python3 check_ledger.py LEDGER.md
        python3 check_ledger.py --self-test

The rules (also in references/ledger-format.md, so they can be applied by hand):
  Errors (the ledger fails):
   1. Claim lines, each starting with an ID such as C1 ("C1." "C1:" "- C1" or "**C1**").
   2. A line starting "Source:" saying where the claims were quoted from.
   3. A falsifier table with columns F | Claim | Falsifier | Status | Receipt | Effect on claim.
   4. A forcing-question table with columns Q | Claims | Answer | Where or why
      (a "does not apply" row may list several questions, as "Q2, Q4, Q8"),
      or, in the short form, a line "Short form: ... missing: Q9 (F1), ..." or "missing: none".
   5. Every question Q1 to Q13 answered, and, across each question's rows, every claim
      covered (or "all").
   6. Answers: covered, missing, does not apply (an empty Claims cell means all claims).
      covered needs evidence, and if it cites F rows at least one must be survived, reported
      or outside the claim.
      missing must cite an existing F row whose status is missing, blocked, failed,
      pending or planned. does not apply needs a reason of at least six words.
      reported receipts must quote the source's own words.
   7. Status: survived, reported, failed, missing, blocked, pending, planned, outside the claim.
   8. Each falsifier at least eight words.
   9. survived, failed, reported, blocked, pending and planned need a real receipt
      (not empty, none, -, n/a, tbd). blocked needs at least four words.
  10. failed, missing, blocked and outside the claim need an effect on the claim.
  11. Every claim ID used must have a claim line; every claim must have a falsifier row.
  12. Lines starting "Claim as it stands:" and "Next test:".
  Warnings (printed; the ledger still passes): listed in references/ledger-format.md.
"""
import re
import sys

ANSWERS = {"covered", "missing", "does not apply"}
STATUSES = {"survived", "reported", "failed", "missing", "blocked", "pending", "planned", "outside the claim"}
OPEN = {"missing", "blocked", "failed", "pending", "planned"}
SOUGHT = {"survived", "reported"}
PLACEHOLDERS = {"", "none", "-", "—", "–", "n/a", "na", "tbd", "todo", "?"}
WEAK_EVIDENCE = {"yes", "ok", "okay", "fine", "n/a", "na", "-", "—", "covered", "done", "see above"}
STRONG_WORDS = re.compile(r"\b(verified|confirmed|proven|proved|guaranteed|guarantees|(?:is|was|been|are|now) fixed)\b", re.I)
HEADLINE_WORDS = re.compile(r"\b(never|always|guarantee[sd]?|perfect|proven|works|exact|robust|reliable)\b", re.I)
QUOTED = re.compile(r"[\"“”‘’]|(?<!\w)'|'(?!\w)")
OWN_WORK = re.compile(r"\b(derived|worked out|counted|computed|calculated|from the definitions?|by construction|we ran|ran)\b", re.I)
MEASURABLE = re.compile(r"\d|\b(more|less|fewer|lower|higher|above|below|same|differ|differs|different|differently|disagree|disagrees|still|again|unchanged|vanish|vanishes|disappear|disappears|exceed|exceeds|within|at least|at most|any|none|no |rises|falls|drops|matches|beats|loses|worse|better)\b", re.I)
RECEIPT_SHAPE = re.compile(r"\d|\"|'|`|\.(py|md|txt|log|json|csv|sh)\b|\b(ran|run|printed|output|counted|computed|worked out|derived|measured|rerun)\b", re.I)
VAGUE_ACTOR = re.compile(r"^\s*(someone|anyone|somebody|we|they|others?)\b", re.I)
SELF_RECORD = re.compile(r"\b(log says|logs say|we checked|self[- ]reported|as reported by the author|the claimant says)\b", re.I)
CLAIM_LINE = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?C(\d+)(?:\*\*)?\s*[.:)\-–—]")


def clean(cell):
    return re.sub(r"[*_`]", "", cell).strip()


def split_row(line):
    return [clean(cell) for cell in line.strip().strip("|").split("|")]


def find_tables(lines):
    """Every Markdown table as (header cells, list of (line number, row cells))."""
    tables, index = [], 0
    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("|") and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[index + 1]):
            header = [cell.lower() for cell in split_row(line)]
            rows, index = [], index + 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append((index + 1, split_row(lines[index])))
                index += 1
            tables.append((header, rows))
        else:
            index += 1
    return tables


def column(header, *names):
    for position, title in enumerate(header):
        for name in names:
            if title.startswith(name):
                return position
    return None


def ids_in(text, letter):
    return set(re.findall(rf"\b{letter}(\d+)\b", text))


def starts(line, label):
    return re.match(rf"^\s*(?:[-*]\s*)?(?:\*\*)?{label}", line, re.I) is not None


def check(text):
    errors, warnings = [], []
    lines = text.splitlines()
    tables = find_tables(lines)
    table_lines = {number for _, rows in tables for number, _ in rows}

    claims = set()
    for line in lines:
        match = CLAIM_LINE.match(line)
        if match:
            claims.add(match.group(1))
    if not claims:
        errors.append("No claim lines. Quote each claim word for word on its own line starting C1., C2. and so on.")
    if not any(starts(line, "Source") for line in lines):
        errors.append("No 'Source:' line. Say where the claims were quoted from.")

    falsifier_table = question_table = None
    for header, rows in tables:
        if column(header, "falsifier") is not None and column(header, "status") is not None:
            falsifier_table = (header, rows)
        elif column(header, "answer") is not None and column(header, "q") == 0:
            question_table = (header, rows)

    status_of, claims_of, rows_per_claim, alone = {}, {}, {}, set()
    receipts, open_rows = {}, 0
    if falsifier_table is None:
        errors.append("No falsifier table (columns F | Claim | Falsifier | Status | Receipt | Effect on claim).")
    else:
        header, rows = falsifier_table
        positions = {name: column(header, name) for name in ("f", "claim", "falsifier", "status", "receipt", "effect")}
        missing_columns = [name for name, position in positions.items() if position is None]
        for name in missing_columns:
            errors.append(f"Falsifier table has no '{name}' column.")
        if not missing_columns:
            needs_receipt = {"survived": "what was run and what it printed", "failed": "what was run and what it printed",
                             "reported": "where the claimant says it was run (quote or cite)", "blocked": "who could run it and its pass mark",
                             "pending": "what is running", "planned": "the prediction and the pass mark"}
            for number, cells in rows:
                if len(cells) <= max(positions.values()):
                    errors.append(f"Line {number}: falsifier row has too few cells.")
                    continue
                row_id = cells[positions["f"]]
                match = re.fullmatch(r"F(\d+)", row_id)
                if not match:
                    errors.append(f"Line {number}: falsifier ID '{row_id}' should look like F1.")
                    continue
                key = match.group(1)
                named = ids_in(cells[positions["claim"]], "C")
                if not named:
                    errors.append(f"Line {number}: {row_id} names no claim ID (C1, C2 ...).")
                for claim in named - claims:
                    errors.append(f"Line {number}: {row_id} names C{claim}, which has no claim line.")
                claims_of[key] = named
                for claim in named:
                    rows_per_claim[claim] = rows_per_claim.get(claim, 0) + 1
                if len(named) == 1:
                    alone |= named
                falsifier = cells[positions["falsifier"]]
                if len(falsifier.split()) < 8:
                    errors.append(f"Line {number}: {row_id} falsifier is too short to run. Say what would be observed, where, how measured, and what result counts against the claim.")
                elif not MEASURABLE.search(falsifier):
                    warnings.append(f"Line {number}: {row_id} falsifier has no number, threshold or comparison. Could someone else run it from these words alone?")
                status = cells[positions["status"]].lower()
                status_of[key] = status
                if status not in STATUSES:
                    errors.append(f"Line {number}: {row_id} status '{status}' is not one of {sorted(STATUSES)}.")
                receipt, effect = cells[positions["receipt"]], cells[positions["effect"]]
                if status in needs_receipt and receipt.lower() in PLACEHOLDERS:
                    errors.append(f"Line {number}: {row_id} is '{status}' but its receipt is empty. It must hold {needs_receipt[status]}.")
                if status == "reported" and receipt.lower() not in PLACEHOLDERS and not QUOTED.search(receipt):
                    errors.append(f"Line {number}: {row_id} is 'reported' but its receipt quotes nothing. Quote the source's own words, or the row is missing.")
                if status == "blocked" and receipt.lower() not in PLACEHOLDERS:
                    if len(receipt.split()) < 4:
                        errors.append(f"Line {number}: {row_id} is 'blocked'; say who could run it and its pass mark.")
                    elif VAGUE_ACTOR.match(receipt):
                        warnings.append(f"Line {number}: {row_id} is 'blocked' but names no one in particular. Who exactly could run it?")
                if status in {"survived", "failed"} and receipt.lower() not in PLACEHOLDERS and not RECEIPT_SHAPE.search(receipt):
                    warnings.append(f"Line {number}: {row_id} receipt names no command, file, number or quoted output.")
                if status in {"survived", "failed"} and SELF_RECORD.search(receipt):
                    warnings.append(f"Line {number}: {row_id} receipt rests on someone else's record; that is 'reported', not 'survived'.")
                if status in {"failed", "missing", "blocked", "outside the claim"} and effect.lower() in PLACEHOLDERS:
                    errors.append(f"Line {number}: {row_id} is '{status}' but says nothing about its effect on the claim.")
                if status == "pending":
                    warnings.append(f"Line {number}: {row_id} is still pending. Do not report the claim as checked until it finishes.")
                if status in OPEN - {"planned"}:
                    open_rows += 1
                if receipt.lower() not in PLACEHOLDERS:
                    receipts.setdefault(receipt.lower(), []).append(row_id)
        for claim in sorted(claims):
            if claim not in rows_per_claim:
                errors.append(f"Claim C{claim} has no falsifier row. Name at least one observation that would show it wrong.")
            else:
                if rows_per_claim[claim] > 8:
                    warnings.append(f"Claim C{claim} has {rows_per_claim[claim]} falsifiers. More than eight usually means padding; keep the ones this case makes live.")
                if claim not in alone:
                    warnings.append(f"Claim C{claim} has no falsifier naming it alone.")
        for receipt, ids in receipts.items():
            if len(ids) > 1:
                warnings.append(f"Rows {', '.join(ids)} have the same receipt. Is each really its own test?")
        for claim in sorted(claims):
            mine = [status_of[key] for key, named in claims_of.items() if claim in named]
            if mine and all(status in SOUGHT | {"outside the claim"} for status in mine):
                if not any(starts(line, "Well-tested") and re.search(rf"\bC{claim}\b", line) for line in lines):
                    warnings.append(f"Every falsifier of C{claim} was sought and survived. If that is right, add a 'Well-tested: C{claim} ...' line; if not, look again for what is missing.")

    short_lines = [line for line in lines if starts(line, "Short form")]
    if question_table is None and not short_lines:
        errors.append("No forcing-question table (columns Q | Claims | Answer | Where or why), and no 'Short form:' line.")
    elif question_table is None:
        line = short_lines[0]
        match = re.search(r"missing:\s*(.*)$", line, re.I)
        if not match:
            errors.append("The 'Short form:' line must say 'missing: Q9 (F1), ...' or 'missing: none'.")
        elif match.group(1).strip().lower() not in {"none", "none."}:
            pairs = re.findall(r"Q(\d+)\s*\(\s*F(\d+)\s*\)", match.group(1))
            if not pairs:
                errors.append("The 'Short form:' line lists missing questions without their falsifier rows, as in 'Q9 (F1)'.")
            for question, row in pairs:
                if row not in status_of:
                    errors.append(f"Short form names F{row} for Q{question}, but there is no F{row} row.")
    else:
        header, rows = question_table
        answer_position = column(header, "answer")
        where_position = column(header, "where", "why", "evidence")
        claims_position = column(header, "claim")
        if where_position is None:
            errors.append("Forcing-question table has no 'Where or why' column.")
        coverage = {}
        for number, cells in rows:
            if not cells or not re.fullmatch(r"Q\d+(\s*,\s*Q\d+)*", cells[0]):
                errors.append(f"Line {number}: question ID '{cells[0] if cells else ''}' should look like Q1, or Q2, Q4 for a shared row.")
                continue
            questions = [int(q) for q in re.findall(r"Q(\d+)", cells[0])]
            question = questions[0]
            needed = max(p for p in (answer_position, where_position, claims_position) if p is not None)
            if len(cells) <= needed:
                errors.append(f"Line {number}: Q{question} row has too few cells.")
                continue
            if claims_position is not None:
                field = cells[claims_position]
                covered_claims = set(claims) if field.strip().lower() in {"all", ""} else ids_in(field, "C")
                for claim in ids_in(field, "C") - claims:
                    errors.append(f"Line {number}: Q{question} names C{claim}, which has no claim line.")
            else:
                covered_claims = set(claims)
            for each in questions:
                coverage.setdefault(each, set()).update(covered_claims)
            answer = cells[answer_position].lower()
            if len(questions) > 1 and answer != "does not apply":
                errors.append(f"Line {number}: only 'does not apply' rows may share several questions; give {cells[0]} a row each.")
            where = cells[where_position] if where_position is not None else ""
            cited = ids_in(where, "F")
            for row in cited - set(status_of):
                errors.append(f"Line {number}: Q{question} cites F{row}, which is not in the falsifier table.")
            cited_known = [status_of[row] for row in cited if row in status_of]
            if answer not in ANSWERS:
                errors.append(f"Line {number}: Q{question} answer '{answer}' is not one of {sorted(ANSWERS)}.")
            elif answer == "covered":
                if where.lower() in WEAK_EVIDENCE:
                    errors.append(f"Line {number}: Q{question} is 'covered' but names no evidence.")
                elif not cited and not QUOTED.search(where) and not OWN_WORK.search(where):
                    warnings.append(f"Line {number}: Q{question} is 'covered' without citing a row, a quotation or your own working. Quote the source, or cite the row.")
                elif cited_known and not any(status in SOUGHT | {"outside the claim"} for status in cited_known):
                    errors.append(f"Line {number}: Q{question} is 'covered' but every row it cites is still open ({', '.join(sorted(set(cited_known)))}). Cite a survived, reported or outside-the-claim row, or answer 'missing'.")
            elif answer == "does not apply" and len(where.split()) < 6:
                errors.append(f"Line {number}: Q{question} 'does not apply' needs a reason of at least six words: the failure you considered, and why the exemption rules it out.")
            elif answer == "missing":
                if not cited:
                    errors.append(f"Line {number}: Q{question} is 'missing' but cites no falsifier row (F1, F2 ...).")
                elif cited_known and not any(status in OPEN for status in cited_known):
                    errors.append(f"Line {number}: Q{question} is 'missing' but the rows it cites are not open ({', '.join(sorted(set(cited_known)))}).")
        for question in range(1, 14):
            if question not in coverage:
                errors.append(f"Question Q{question} is not answered. Every question Q1 to Q13 gets covered, missing or does not apply.")
            else:
                for claim in sorted(claims - coverage[question]):
                    errors.append(f"Question Q{question} has no answer for C{claim}. Answer it for every claim, or write 'all'.")

    standing_lines = [line for line in lines if starts(line, "Claim as it stands")]
    if not standing_lines:
        errors.append("No 'Claim as it stands:' line. Restate the claim at the scope its tests reached.")
    if not any(starts(line, "Next test") for line in lines):
        errors.append("No 'Next test:' line. Name one test.")
    standing = " ".join(standing_lines).lower()
    if standing.count("held if") > 3:
        warnings.append("'Claim as it stands' has more than three 'held if'. A claim held only if many things hold says little; say so plainly.")
    for line in lines:
        if starts(line, "Routine checks") and re.search(r"\d|\.(py|md|txt|log|json)\b", line):
            warnings.append("The 'Routine checks:' line has numbers or file names. Case-specific items belong in the ledger.")

    for number, line in enumerate(lines, start=1):
        if number in table_lines or line.strip().startswith(("|", "#")) or CLAIM_LINE.match(line):
            continue
        if any(starts(line, label) for label in ("Claim as it stands", "Routine checks", "Source", "Well-tested")):
            continue
        if open_rows:
            for word in STRONG_WORDS.findall(line):
                warnings.append(f"Line {number}: '{word}' while {open_rows} falsifier(s) are open. Make sure the word is earned.")
        for word in set(w.lower() for w in HEADLINE_WORDS.findall(line)):
            if standing and word not in standing:
                warnings.append(f"Line {number}: '{word}' is in the report but not in 'Claim as it stands'. The headline must follow the ledger.")
    return errors, warnings


def sample():
    rows = "| Q1 | C1 | missing | F1 |\n" + "\n".join(f"| Q{n} | all | does not apply | the failure considered does not arise for this one claim here |" for n in range(2, 14))
    return f"""C1. The planner's exact check **guarantees** every chosen program reaches the goal.
Source: report, summary paragraph.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | In at least one of three scenes outside the supplied model list, the planner says yes and is wrong | missing | none | C1 held only inside the supplied models |
| F2 | C1 | Planner forecasts differ from a separate checker run on at least one candidate | reported | report section 4, "every forecast matched" | none |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
{rows}

Claim as it stands: the planner guarantees success only inside the supplied models.
Next test: run three scenes outside the model list.
"""


def self_test():
    good = sample()
    cases = [
        ("a good ledger passes", good, None),
        ("a missing question is refused", good.replace("| Q1 | C1 | missing | F1 |\n", ""), "Q1"),
        ("a survived row with no receipt is refused", good.replace("| missing | none | C1 held", "| survived | none | C1 held"), "receipt is empty"),
        ("no Next test is refused", good.replace("Next test: run three scenes outside the model list.", ""), "Next test"),
        ("a missing answer citing nothing is refused", good.replace("| Q1 | C1 | missing | F1 |", "| Q1 | C1 | missing | see above |"), "cites no falsifier row"),
        ("covered citing only an open row is refused", good.replace("| Q1 | C1 | missing | F1 |", "| Q1 | C1 | covered | F1 |"), "still open"),
        ("missing citing a reported row is refused", good.replace("| Q1 | C1 | missing | F1 |", "| Q1 | C1 | missing | F2 |"), "not open"),
        ("no Source line is refused", good.replace("Source: report, summary paragraph.\n", ""), "Source"),
        ("a short falsifier is refused", good.replace("In at least one of three scenes outside the supplied model list, the planner says yes and is wrong", "it fails sometimes"), "too short"),
        ("a question not covering every claim is refused", good.replace("C1. The planner", "C2. Planning is faster.\nC1. The planner").replace("| F2 | C1 |", "| F2 | C2 |").replace("| Q1 | C1 | missing | F1 |", "| Q1 | C1 | missing | F1 |"), "no answer for C2"),
        ("a reported row without a quotation is refused", good.replace('report section 4, "every forecast matched"', "report section 4"), "quotes nothing"),
        ("a shared does-not-apply row passes", good.replace("\n".join(f"| Q{n} | all | does not apply | the failure considered does not arise for this one claim here |" for n in range(2, 14)), "| Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13 | all | does not apply | the failure considered does not arise for this one claim here |"), None),
        ("a shared covered row is refused", good.replace("| Q2 | all | does not apply | the failure considered does not arise for this one claim here |\n| Q3 | all | does not apply | the failure considered does not arise for this one claim here |", "| Q2, Q3 | all | covered | F2 as reported |"), "only 'does not apply' rows"),
        ("the short form passes", good.split("| Q | Claims")[0] + "Short form: all 13 questions asked; missing: Q1 (F1)\n\nClaim as it stands: inside the models only.\nNext test: three scenes outside.\n", None),
    ]
    passed = 0
    for name, text, expect in cases:
        errors, _ = check(text)
        ok = (not errors) if expect is None else any(expect in error for error in errors)
        passed += ok
        if not ok:
            print("SELF-TEST FAILED:", name, errors)
    print(f"self-test passed: {passed} of {len(cases)}")
    return passed == len(cases)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return 0 if self_test() else 1
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as handle:
        errors, warnings = check(handle.read())
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"PASSED: 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
