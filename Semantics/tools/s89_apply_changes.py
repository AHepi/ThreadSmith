"""s89_apply_changes.py: make a draft of revision 2 of the theory by applying the change list to file 11.

What it does, in order:

1. Reads file 11 from Semantics/authority/ (the one file there whose name starts with "11 ") and refuses
   unless its md5 is 5e494c1095d920d128b9a79de378f923. It never writes into authority/.
2. Reads the change list (by default "Semantics/tests/Revision 2 - change list, draft of 23 September.md")
   and parses every entry under its heading "## The entries".
3. Checks the entries against file 11 and refuses on any mismatch:
   - the OLD text of every applied entry occurs in file 11 exactly once;
   - no two applied OLD texts overlap;
   - the stated file-11 line of every entry is the line its text begins (and ends) on;
   - every record-only locator, every held anchor and every layer-2 locator occurs in file 11 exactly once;
   - no held anchor is overlapped by an applied entry;
   - every entry whose expected ruling is CLAIM carries a declaration.
4. Applies the entries in file-11 order. First the entries that change the theory text are applied alone,
   which gives the theory text of the draft. Then the slots of the three meta entries (the note, the note of
   sources and departures, and the revision record) are filled from the change list: the date, N, M, K, the
   declarations, layer 1 of the record and the last column of layer 2. Then every applied entry is applied
   to file 11.
5. Checks the result and refuses if any check fails:
   - walking file 11 and the result together shows that the result is file 11 with exactly the listed
     replacements and nothing else;
   - every changed line of the result lies inside an entry;
   - no slot is left unfilled;
   - cutting the three meta blocks between their marker lines gives back the theory text of step 4;
   - the theory text carries none of the withheld words, and the note and record name no case, place,
     item, round or model.
6. Writes the result to the path given on the command line (by default a file in the system's temporary
   folder). With --theory-output it also writes the theory text, the three meta blocks cut.

With --self-test it also plants an unlisted one-character edit in a copy of the result, and a one-character
edit inside a new text, and confirms that the check refuses both while the clean result passes.

Usage:
    python3 Semantics/tools/s89_apply_changes.py [output path] [--change-list PATH] [--date TEXT]
                                                  [--theory-output PATH] [--self-test]
"""
import argparse
import difflib
import hashlib
import pathlib
import re
import sys
import tempfile

REPOSITORY = pathlib.Path(__file__).resolve().parent.parent.parent
AUTHORITY_FOLDER = REPOSITORY / "Semantics" / "authority"
DEFAULT_CHANGE_LIST = REPOSITORY / "Semantics" / "tests" / "Revision 2 - change list, draft of 23 September.md"
DEFAULT_OUTPUT = pathlib.Path(tempfile.gettempdir()) / "s89 revision 2 draft.md"
FILE_11_MD5 = "5e494c1095d920d128b9a79de378f923"
DEFAULT_DATE = "draft, not frozen"

FENCE = "````"
MARKERS = {
    "NOTE": ("<!-- META:NOTE BEGIN -->", "<!-- META:NOTE END -->"),
    "SOURCES": ("<!-- META:SOURCES BEGIN -->", "<!-- META:SOURCES END -->"),
    "RECORD": ("<!-- META:RECORD BEGIN -->", "<!-- META:RECORD END -->"),
}
DECLARATION_LINE = "- File 11, line {line}: {declaration}"
LAYER_ONE_ENTRY = (
    "**R2-{number:02d}.** {part}, {heading}, {line}.\n"
    "\n"
    "Reason: {reason}. Expected ruling: {kind}.\n"
    "\n"
    "Old:\n"
    "\n"
    "```text\n"
    "{old}\n"
    "```\n"
    "\n"
    "New:\n"
    "\n"
    "```text\n"
    "{new}\n"
    "```\n"
    "\n"
    "What a reader can now conclude that file 11 left unconcluded: {conclude}"
)
CONCLUSION_WHEN_NOT_CLAIM = {
    "WORDING": "nothing; the change is one of wording.",
    "ORDER": "nothing; the change is one of order.",
}
# Words that must not reach a tested reader: they are checked in the theory text, the meta blocks cut.
WITHHELD_IN_THEORY = ["META:", "@@", "Revision 2", "revision record", "file 13", "Deutsch", "Marletto"]
# Names that must not appear in the note or the record outside quoted theory text.
WITHHELD_IN_NOTE_AND_RECORD = re.compile(
    r"\b(?:O\d{1,2}|N\d{1,2}|M\d{1,2}|W\d{1,2}|S\d{2}|XR\d+|C\d{1,2})\b|Mimo|Atria|Claude|"
    r"DeepSeek|Pinker|\bround\b|determination|worklist|\baudit")


class Refusal(Exception):
    """Raised on any mismatch. Nothing is written when it is raised."""


# ------------------------------------------------------------------------------------------ reading
def find_file_11():
    candidates = sorted(AUTHORITY_FOLDER.glob("11 *.md"))
    if len(candidates) != 1:
        raise Refusal("expected one file starting with '11 ' in %s, found %d" % (AUTHORITY_FOLDER, len(candidates)))
    raw_bytes = candidates[0].read_bytes()
    digest = hashlib.md5(raw_bytes).hexdigest()
    if digest != FILE_11_MD5:
        raise Refusal("file 11 has md5 %s, not %s" % (digest, FILE_11_MD5))
    return raw_bytes.decode("utf-8")


FIELD_LINE = re.compile(r"^- \*\*([A-Z0-9][A-Z0-9 /()-]*):\*\*(?: (.*))?$")


def parse_change_list(change_list_text):
    """Return the entries under '## The entries', each a dictionary of its fields.

    A fenced field (OLD, NEW, LOCATOR, ANCHOR, LAYER-2 ROW, LAYER-2 LOCATORS) holds the exact text between
    its four-backtick fence lines. ANCHOR may occur more than once and is kept as a list.
    """
    if change_list_text.count("\n## The entries\n") != 1:
        raise Refusal("the change list has no single '## The entries' heading")
    section = change_list_text.split("\n## The entries\n", 1)[1]
    lines = section.split("\n")
    entries = []
    current_entry = None
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("## "):
            break
        if line.startswith("### "):
            heading = line[4:]
            if " — " not in heading:
                raise Refusal("entry heading without ' — ': %r" % heading)
            entry_id, title = heading.split(" — ", 1)
            current_entry = {"id": entry_id.strip(), "title": title.strip(), "ANCHOR": []}
            entries.append(current_entry)
            index += 1
            continue
        match = FIELD_LINE.match(line)
        if current_entry is not None and match:
            name, value = match.group(1), match.group(2) or ""
            following = lines[index + 1] if index + 1 < len(lines) else ""
            if following == FENCE + "text":
                closing = index + 2
                while closing < len(lines) and lines[closing] != FENCE:
                    closing += 1
                if closing >= len(lines):
                    raise Refusal("unclosed fence in entry %s, field %s" % (current_entry["id"], name))
                fenced_text = "\n".join(lines[index + 2:closing])
                if name == "ANCHOR":
                    current_entry["ANCHOR"].append((value, fenced_text))
                else:
                    if name in current_entry:
                        raise Refusal("field %s given twice in entry %s" % (name, current_entry["id"]))
                    current_entry[name] = fenced_text
                index = closing + 1
                continue
            if name in current_entry and name != "ANCHOR":
                raise Refusal("field %s given twice in entry %s" % (name, current_entry["id"]))
            current_entry[name] = value
        index += 1
    return entries


# ------------------------------------------------------------------------------------------ positions
def line_number(text, position):
    return text.count("\n", 0, position) + 1


def single_span(text, fragment, what):
    count = text.count(fragment)
    if count != 1:
        raise Refusal("%s occurs %d times in file 11, not once: %r" % (what, count, fragment[:90]))
    start = text.find(fragment)
    return start, start + len(fragment)


def line_label(text, start, end):
    first, last = line_number(text, start), line_number(text, end - 1)
    return str(first) if first == last else "%d–%d" % (first, last)


def part_and_heading(text, position):
    """Name the Part and heading of file 11 in which a position lies.

    The heading is the nearest '## ' heading of the Part above the position (a Part XVI heading is named as
    its derivation), followed by the label of the nearest labelled paragraph at or above the position under
    that heading, if any. With neither, it is the Part's own title.
    """
    line_start = text.rfind("\n", 0, position) + 1
    line_end = text.find("\n", position)
    lines_up_to_position = text[:line_end if line_end != -1 else len(text)].split("\n")
    part_name, part_title, subheading, label = None, None, None, None
    for line in lines_up_to_position:
        if line.startswith("# Part "):
            part_name, _, part_title = line[2:].partition(" — ")
            subheading, label = None, None
        elif line.startswith("## ") and part_name is not None:
            subheading, label = line[3:], None
        else:
            match = re.match(r"\*\*([^*]+?)\.?\*\*|\*([A-Z][a-z]+)\.\*", line)
            if match:
                label = (match.group(1) or match.group(2)).rstrip(".")
    if part_name is None:
        return "front matter", "before Part 0"
    pieces = []
    if subheading:
        derivation = re.match(r"(\d+)\. ", subheading)
        pieces.append("Derivation " + derivation.group(1) if part_name == "Part XVI" and derivation else subheading)
    if label:
        pieces.append(label)
    if not pieces:
        pieces.append(part_title)
    return part_name, ", ".join(pieces)


# ------------------------------------------------------------------------------------------ checks
def check_entries(file_11_text, entries):
    applied, record_only, held = [], [], []
    for entry in entries:
        status = entry.get("STATUS")
        if status == "applied":
            for needed in ("OLD", "NEW", "KIND", "FILE-11 LINE"):
                if needed not in entry:
                    raise Refusal("applied entry %s has no %s" % (entry["id"], needed))
            entry["start"], entry["end"] = single_span(file_11_text, entry["OLD"], "OLD of " + entry["id"])
            stated_line = entry["FILE-11 LINE"]
            found_line = line_label(file_11_text, entry["start"], entry["end"])
            if stated_line != found_line:
                raise Refusal("entry %s states line %s, but its OLD lies on line %s" % (entry["id"], stated_line, found_line))
            entry["ruling"] = entry["KIND"].split()[0].strip(".")
            if entry["ruling"] not in ("CLAIM", "WORDING", "ORDER", "META"):
                raise Refusal("entry %s has an unknown expected ruling %r" % (entry["id"], entry["KIND"]))
            if entry["ruling"] == "CLAIM":
                declaration = entry.get("DECLARATION", "").strip()
                if not declaration or declaration.lower().startswith("none"):
                    raise Refusal("entry %s is expected as CLAIM and has no declaration" % entry["id"])
                if "\n" in declaration:
                    raise Refusal("entry %s has a declaration of more than one line" % entry["id"])
            if entry["ruling"] != "META" and not entry.get("REASON WORD"):
                raise Refusal("entry %s has no REASON WORD" % entry["id"])
            applied.append(entry)
        elif status == "record-only":
            if "LOCATOR" not in entry:
                raise Refusal("record-only entry %s has no LOCATOR" % entry["id"])
            start, end = single_span(file_11_text, entry["LOCATOR"], "locator of " + entry["id"])
            if entry.get("FILE-11 LINE") != line_label(file_11_text, start, end):
                raise Refusal("record-only entry %s states the wrong line" % entry["id"])
            record_only.append(entry)
        elif status == "held":
            if not entry["ANCHOR"]:
                raise Refusal("held entry %s names no anchor" % entry["id"])
            entry["anchor spans"] = [single_span(file_11_text, anchor, "anchor of " + entry["id"])
                                     for _, anchor in entry["ANCHOR"]]
            held.append(entry)
        else:
            raise Refusal("entry %s has an unknown STATUS %r" % (entry["id"], status))
    applied.sort(key=lambda entry: entry["start"])
    for earlier, later in zip(applied, applied[1:]):
        if earlier["end"] > later["start"]:
            raise Refusal("the OLD texts of %s and %s overlap" % (earlier["id"], later["id"]))
    for entry in held:
        for anchor_start, anchor_end in entry["anchor spans"]:
            for other in applied:
                if anchor_start < other["end"] and other["start"] < anchor_end:
                    raise Refusal("held anchor of %s is overlapped by %s" % (entry["id"], other["id"]))
    return applied, record_only, held


def apply_entries(file_11_text, entries_in_order, new_text_of):
    pieces, position = [], 0
    for entry in entries_in_order:
        pieces.append(file_11_text[position:entry["start"]])
        pieces.append(new_text_of(entry))
        position = entry["end"]
    pieces.append(file_11_text[position:])
    return "".join(pieces)


def walk_check(file_11_text, result_text, replacements):
    """Refuse unless result_text is file_11_text with exactly these (start, end, new) replacements."""
    position_in_file_11, position_in_result = 0, 0
    for start, end, new_text in replacements:
        unchanged = file_11_text[position_in_file_11:start]
        if result_text[position_in_result:position_in_result + len(unchanged)] != unchanged:
            first_line = line_number(file_11_text, position_in_file_11)
            raise Refusal("text outside the entries differs from file 11 (after file-11 line %d)" % first_line)
        position_in_result += len(unchanged)
        if result_text[position_in_result:position_in_result + len(new_text)] != new_text:
            raise Refusal("the new text at file-11 line %d is not the entry's NEW" % line_number(file_11_text, start))
        position_in_result += len(new_text)
        position_in_file_11 = end
    if result_text[position_in_result:] != file_11_text[position_in_file_11:]:
        raise Refusal("the text after the last entry differs from file 11")


def hunk_check(file_11_text, result_text, applied):
    """Every changed line of the result lies inside an entry.

    A diff hunk may start or end on a blank line next to an entry, since a line diff can align blank lines
    either way; every non-blank file-11 line a hunk touches must lie inside an entry, and a hunk that touches
    no non-blank line must sit next to one (across blank lines only). One entry may give several hunks.
    """
    file_11_lines = file_11_text.split("\n")
    result_lines = result_text.split("\n")
    spans = [(line_number(file_11_text, entry["start"]), line_number(file_11_text, entry["end"] - 1))
             for entry in applied]

    def inside_an_entry(file_11_line):
        return any(first <= file_11_line <= last for first, last in spans)

    def next_to_an_entry(line_before, line_after):
        while line_before >= 1 and file_11_lines[line_before - 1] == "":
            line_before -= 1
        while line_after <= len(file_11_lines) and file_11_lines[line_after - 1] == "":
            line_after += 1
        return inside_an_entry(line_before) or inside_an_entry(line_after)

    hunks = 0
    for tag, first_11, end_11, first_result, end_result in difflib.SequenceMatcher(
            None, file_11_lines, result_lines, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        hunks += 1
        touched = [line for line in range(first_11 + 1, end_11 + 1) if file_11_lines[line - 1] != ""]
        for file_11_line in touched:
            if not inside_an_entry(file_11_line):
                raise Refusal("file-11 line %d changed and belongs to no entry" % file_11_line)
        if not touched and not next_to_an_entry(first_11, end_11 + 1):
            raise Refusal("a change near file-11 line %d belongs to no entry" % (first_11 + 1))
    return hunks


def cut_meta_blocks(text):
    """Remove the three meta blocks by the cut rule of group M.

    NOTE and SOURCES: every line from the BEGIN line through the END line, and the one blank line after it.
    RECORD: the one blank line before the BEGIN line, and every line from the BEGIN line through the END line.
    """
    lines = text.split("\n")
    positions = {}
    for name, (begin_marker, end_marker) in MARKERS.items():
        for marker in (begin_marker, end_marker):
            if lines.count(marker) != 1:
                raise Refusal("marker %r occurs %d times" % (marker, lines.count(marker)))
        positions[name] = (lines.index(begin_marker), lines.index(end_marker))
    if not (positions["NOTE"][1] < positions["SOURCES"][0] and positions["SOURCES"][1] < positions["RECORD"][0]):
        raise Refusal("the meta blocks are not in the order NOTE, SOURCES, RECORD")
    removed = set()
    for name in ("NOTE", "SOURCES"):
        begin, end = positions[name]
        if lines[end + 1] != "":
            raise Refusal("no blank line after the %s block" % name)
        removed.update(range(begin, end + 2))
    begin, end = positions["RECORD"]
    if lines[begin - 1] != "":
        raise Refusal("no blank line before the RECORD block")
    removed.update(range(begin - 1, end + 1))
    return "\n".join(line for number, line in enumerate(lines) if number not in removed)


# ------------------------------------------------------------------------------------------ slots
def fill_slots(file_11_text, applied, theory_entries, theory_text, date_text):
    """Return {entry id: filled NEW} for the meta entries, and a summary."""
    numbers = {entry["id"]: number for number, entry in enumerate(theory_entries, 1)}
    claim_entries = [entry for entry in theory_entries if entry["ruling"] == "CLAIM"]
    declarations = "\n".join(
        DECLARATION_LINE.format(line=line_number(file_11_text, entry["start"]), declaration=entry["DECLARATION"].strip())
        for entry in claim_entries)
    layer_one = []
    for entry in theory_entries:
        part, heading = part_and_heading(file_11_text, entry["start"])
        conclusion = (entry["DECLARATION"].strip() if entry["ruling"] == "CLAIM"
                      else CONCLUSION_WHEN_NOT_CLAIM[entry["ruling"]])
        layer_one.append(LAYER_ONE_ENTRY.format(
            number=numbers[entry["id"]], part=part, heading=heading,
            line=("lines " if "–" in entry["FILE-11 LINE"] else "line ") + entry["FILE-11 LINE"],
            reason=entry["REASON WORD"].strip(), kind=entry["ruling"], old=entry["OLD"], new=entry["NEW"],
            conclude=conclusion))
    record_entries = [entry for entry in applied if "LAYER-2 LOCATORS" in entry]
    if len(record_entries) != 1:
        raise Refusal("exactly one entry must carry the layer-2 locators")
    record_entry = record_entries[0]
    locators = []
    for locator_line in record_entry["LAYER-2 LOCATORS"].split("\n"):
        row_id, locator = locator_line.split(" ", 1)
        locators.append((row_id, locator))
    table_rows = re.findall(r"(?m)^\| (L2-\d\d) \|", record_entry["NEW"])
    if [row_id for row_id, _ in locators] != table_rows:
        raise Refusal("the layer-2 locators and the layer-2 table rows do not match")
    column = {}
    for row_id, locator in locators:
        start, end = single_span(file_11_text, locator, "layer-2 locator " + row_id)
        meeting = ["R2-%02d" % numbers[entry["id"]] for entry in theory_entries
                   if start < entry["end"] and entry["start"] < end]
        occurrences = theory_text.count(locator)
        if occurrences == 1 and not meeting:
            column[row_id] = "kept"
        elif occurrences == 1:
            column[row_id] = "kept; %s %s text beside it" % (join_names(meeting), "adds" if len(meeting) == 1 else "add")
        elif occurrences == 0 and meeting:
            column[row_id] = "changed by " + join_names(meeting)
        else:
            raise Refusal("layer-2 row %s: locator occurs %d times in the draft, met by %s" % (row_id, occurrences, meeting))
    values = {
        "@@DATE@@": date_text,
        "@@N@@": str(len(claim_entries)),
        "@@M@@": str(len(theory_entries)),
        "@@K@@": str(len(locators)),
        "@@DECLARATIONS@@": declarations,
        "@@LAYER1@@": "\n\n".join(layer_one),
    }
    for row_id, value in column.items():
        values["@@REV2:%s@@" % row_id] = value
    filled = {}
    for entry in applied:
        if entry["ruling"] != "META":
            continue
        new_text = entry["NEW"]
        for slot in re.findall(r"@@[A-Z0-9:-]+@@", new_text):
            if slot not in values:
                raise Refusal("entry %s has a slot the program cannot fill: %s" % (entry["id"], slot))
        for slot, value in values.items():
            new_text = new_text.replace(slot, value)
        if "@@" in new_text:
            raise Refusal("entry %s still has a slot after filling" % entry["id"])
        filled[entry["id"]] = new_text
    summary = dict(N=len(claim_entries), M=len(theory_entries), K=len(locators), column=column,
                   declarations=declarations, numbers=numbers)
    return filled, summary


def join_names(names):
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def names_outside_quoted_text(block_text):
    """The note or record with its fenced theory text removed, for the withheld-name check."""
    return re.sub(r"```text\n.*?\n```", "", block_text, flags=re.S)


# ------------------------------------------------------------------------------------------ build
def build(change_list_path, date_text):
    file_11_text = find_file_11()
    entries = parse_change_list(pathlib.Path(change_list_path).read_text(encoding="utf-8"))
    applied, record_only, held = check_entries(file_11_text, entries)
    theory_entries = [entry for entry in applied if entry["ruling"] != "META"]
    meta_entries = [entry for entry in applied if entry["ruling"] == "META"]
    if len(meta_entries) != 3:
        raise Refusal("expected three meta entries, found %d" % len(meta_entries))
    note_entry = [entry for entry in meta_entries if MARKERS["NOTE"][0] in entry["NEW"]]
    if len(note_entry) != 1:
        raise Refusal("no single meta entry carries the note")
    theory_only = apply_entries(file_11_text, theory_entries, lambda entry: entry["NEW"])
    old_note_with_blank = note_entry[0]["OLD"] + "\n\n"
    if theory_only.count(old_note_with_blank) != 1:
        raise Refusal("file 11's note and the blank line after it are not found once")
    theory_text = theory_only.replace(old_note_with_blank, "", 1)
    filled, summary = fill_slots(file_11_text, applied, theory_entries, theory_text, date_text)
    new_text_of = lambda entry: filled.get(entry["id"], entry["NEW"])  # noqa: E731
    result_text = apply_entries(file_11_text, applied, new_text_of)

    replacements = [(entry["start"], entry["end"], new_text_of(entry)) for entry in applied]
    walk_check(file_11_text, result_text, replacements)
    hunks = hunk_check(file_11_text, result_text, applied)
    if "@@" in result_text:
        raise Refusal("a slot is left in the result")
    if cut_meta_blocks(result_text) != theory_text:
        raise Refusal("cutting the meta blocks does not give back the theory text")
    for word in WITHHELD_IN_THEORY:
        if word in theory_text:
            raise Refusal("the theory text carries the withheld word %r" % word)
    if re.search(r"(?i)\brevision\b", theory_text):
        raise Refusal("the theory text uses the word 'revision'")
    for entry in meta_entries:
        if entry["id"] == "W38.1" or MARKERS["SOURCES"][0] in entry["NEW"]:
            continue
        hits = sorted(set(match.group(0) for match in
                          WITHHELD_IN_NOTE_AND_RECORD.finditer(names_outside_quoted_text(filled[entry["id"]]))))
        if hits:
            raise Refusal("the meta entry %s names %s" % (entry["id"], hits))
    return dict(file_11_text=file_11_text, result_text=result_text, theory_text=theory_text, entries=entries,
                applied=applied, record_only=record_only, held=held, theory_entries=theory_entries,
                replacements=replacements, hunks=hunks, summary=summary)


def self_test(build_result):
    """Plant an unlisted edit and an edit inside a new text; the check must refuse both."""
    file_11_text, result_text = build_result["file_11_text"], build_result["result_text"]
    replacements = build_result["replacements"]
    walk_check(file_11_text, result_text, replacements)
    untouched_position = result_text.find("# Part II")
    planted_outside = result_text[:untouched_position + 3] + "X" + result_text[untouched_position + 4:]
    start, end, chosen_new_text = replacements[len(replacements) // 2]
    inside_position = result_text.find(chosen_new_text) + len(chosen_new_text) // 2
    replacement_character = "#" if result_text[inside_position] != "#" else "%"
    planted_inside = result_text[:inside_position] + replacement_character + result_text[inside_position + 1:]
    outcomes = []
    for name, planted in (("an unlisted edit", planted_outside), ("an edit inside a new text", planted_inside)):
        try:
            walk_check(file_11_text, planted, replacements)
        except Refusal:
            outcomes.append("%s was refused" % name)
        else:
            raise Refusal("self-test: %s was not caught" % name)
    return outcomes


def main(arguments=None):
    parser = argparse.ArgumentParser(description="Apply the revision 2 change list to file 11.")
    parser.add_argument("output", nargs="?", default=str(DEFAULT_OUTPUT),
                        help="where to write the draft (default: %(default)s); never inside Semantics/authority/")
    parser.add_argument("--change-list", default=str(DEFAULT_CHANGE_LIST))
    parser.add_argument("--date", default=DEFAULT_DATE, help="the date written in the note (default: %(default)r)")
    parser.add_argument("--theory-output", default=None, help="also write the theory text, meta blocks cut")
    parser.add_argument("--self-test", action="store_true")
    options = parser.parse_args(arguments)
    outputs = [pathlib.Path(options.output)] + ([pathlib.Path(options.theory_output)] if options.theory_output else [])
    try:
        for output in outputs:
            resolved = output.resolve()
            if resolved == AUTHORITY_FOLDER.resolve() or AUTHORITY_FOLDER.resolve() in resolved.parents:
                raise Refusal("refusing to write inside %s: %s" % (AUTHORITY_FOLDER, output))
        result = build(options.change_list, options.date)
        self_test_outcomes = self_test(result) if options.self_test else []
    except Refusal as refusal:
        print("REFUSED: %s" % refusal)
        print("Nothing was written.")
        return 1
    output = outputs[0]
    output.write_bytes(result["result_text"].encode("utf-8"))
    if options.theory_output:
        pathlib.Path(options.theory_output).write_bytes(result["theory_text"].encode("utf-8"))
    summary = result["summary"]
    ruling_counts = {}
    for entry in result["theory_entries"]:
        ruling_counts[entry["ruling"]] = ruling_counts.get(entry["ruling"], 0) + 1
    result_bytes = result["result_text"].encode("utf-8")
    print("file 11: md5 %s (as required)" % FILE_11_MD5)
    print("entries parsed: %d (applied %d, of which theory %d and meta %d; record-only %d; held %d)" % (
        len(result["entries"]), len(result["applied"]), len(result["theory_entries"]),
        len(result["applied"]) - len(result["theory_entries"]), len(result["record_only"]), len(result["held"])))
    print("theory entries by expected ruling: %s" % ", ".join(
        "%s %d" % (ruling, ruling_counts[ruling]) for ruling in sorted(ruling_counts)))
    print("every OLD, locator and anchor occurs once in file 11; no applied OLDs overlap; no held anchor is touched")
    print("note: N = %d of M = %d changes; layer 2: K = %d places" % (summary["N"], summary["M"], summary["K"]))
    print("result is file 11 with exactly the listed replacements (walk check); %d diff hunks, each inside an entry"
          % result["hunks"])
    print("cut of the three meta blocks gives back the theory text; no withheld word in it; no slot left")
    for outcome in self_test_outcomes:
        print("self-test: %s" % outcome)
    if options.self_test:
        print("self-test: the clean draft passed")
    print("written: %s" % output)
    print("md5: %s" % hashlib.md5(result_bytes).hexdigest())
    print("words: %d (theory text alone: %d)" % (len(result["result_text"].split()), len(result["theory_text"].split())))
    print("lines: %d" % result["result_text"].count("\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
