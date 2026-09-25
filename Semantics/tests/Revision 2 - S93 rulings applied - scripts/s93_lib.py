"""s93_lib.py - shared helpers for applying the S93 rulings to the revision 2 change list.

Every ruled text is cut from its ruling file by program (never retyped), and every replacement in the change
list asserts that the old text occurs exactly once.
"""
import pathlib
import subprocess
import sys

REPO = pathlib.Path('/home/user/ThreadSmith')
SEM = REPO / 'Semantics'
RULINGS = SEM / 'results' / 'S93 reading rulings'
CHANGE_LIST_REL = 'Semantics/tests/Revision 2 - change list, draft of 23 September.md'
NOTE_REL = 'Semantics/tests/Revision 2 - revision note, draft of 23 September.md'
TOOL = SEM / 'tools' / 's89_apply_changes.py'

RULING_FILES = {
    'X03': 'ruling S93 X03 W19.1.md',
    'X04': 'ruling S93 X04 W35.1.md',
    'X05': 'ruling S93 X05 W35.2.md',
    'X06': 'ruling S93 X06 W20.1.md',
    'X09': 'ruling S93 X09 W59.1 Rivals.md',
    'X10': 'ruling S93 X10 W59.1 Problems.md',
    'X11': 'ruling S93 X11 proposed.md',
    'X14': 'ruling S93 X14 W60.1.md',
    'X17': 'ruling S93 X17 W7.5.md',
    'X18': 'ruling S93 X18 W38.1.md',
}


def git_show(rel_path, rev='HEAD'):
    return subprocess.run(['git', 'show', '%s:%s' % (rev, rel_path)], cwd=str(REPO), capture_output=True,
                          check=True).stdout.decode('utf-8')


def ruling(item):
    return (RULINGS / RULING_FILES[item]).read_text(encoding='utf-8')


def fence_after(text, marker, fence='````', start_marker=None):
    """The exact text inside the first fence (```` + 'text', any indentation) after the line holding marker.

    If start_marker is given, the search for marker begins at start_marker's first occurrence.
    """
    base = 0
    if start_marker is not None:
        if text.count(start_marker) < 1:
            raise SystemExit('start marker not found: %r' % start_marker)
        base = text.index(start_marker)
    position = text.find(marker, base)
    if position < 0:
        raise SystemExit('marker not found: %r' % marker)
    lines = text[position:].split('\n')
    index = 1
    while index < len(lines):
        stripped = lines[index].lstrip(' ')
        if stripped == fence + 'text':
            indent = lines[index][:len(lines[index]) - len(stripped)]
            break
        index += 1
    else:
        raise SystemExit('no fence after marker %r' % marker)
    content = []
    index += 1
    while lines[index] != indent + fence:
        line = lines[index]
        if line and not line.startswith(indent):
            raise SystemExit('fence content not indented as its fence, after %r' % marker)
        content.append(line[len(indent):])
        index += 1
    return '\n'.join(content)


def line_with(text, marker, start_marker=None):
    base = text.index(start_marker) if start_marker else 0
    position = text.find(marker, base)
    if position < 0:
        raise SystemExit('marker not found: %r' % marker)
    begin = text.rfind('\n', 0, position) + 1
    end = text.find('\n', position)
    return text[begin:end if end >= 0 else len(text)]


def quoted_on_line(text, marker, opening, closing, start_marker=None, from_line_start=False):
    """On the line holding marker: from just after the first occurrence of opening (searched from the marker, or
    from the start of the line) to the last occurrence of closing (exclusive)."""
    line = line_with(text, marker, start_marker)
    begin = line.index(opening, 0 if from_line_start else line.index(marker)) + len(opening)
    end = line.rindex(closing)
    if end <= begin:
        raise SystemExit('bad quotation on the line of %r' % marker)
    return line[begin:end]


def one(text, old, new, what):
    count = text.count(old)
    if count != 1:
        raise SystemExit('replacement %s: old text occurs %d times' % (what, count))
    return text.replace(old, new)


def entry_span(text, entry_id):
    """(start, end) of an entry's section: from its '### id — ' heading to the next '### ' or '## ' heading."""
    heading = '\n### %s — ' % entry_id
    if text.count(heading) != 1:
        raise SystemExit('entry heading %s occurs %d times' % (entry_id, text.count(heading)))
    start = text.index(heading) + 1
    # skip fenced blocks: find next heading line outside fences
    lines = text[start:].split('\n')
    offset = len(lines[0]) + 1
    in_fence = False
    for line in lines[1:]:
        if line.lstrip(' ').startswith('````'):
            stripped = line.lstrip(' ')
            if not in_fence and stripped.startswith('````text'):
                in_fence = stripped[:len(stripped) - 4]  # the fence string
            elif in_fence and stripped == in_fence:
                in_fence = False
        if not in_fence and (line.startswith('### ') or line.startswith('## ')):
            return start, start + offset
        offset += len(line) + 1
    return start, len(text)


def replace_in_entry(text, entry_id, old, new, what):
    start, end = entry_span(text, entry_id)
    section = text[start:end]
    section = one(section, old, new, '%s in %s' % (what, entry_id))
    return text[:start] + section + text[end:]


def field_block_end(section, field):
    """Index in section just after the last line of a field block (a '- **FIELD:**' line and its indented
    continuation lines), i.e. where the next '- **' field line begins."""
    marker = '\n- **%s:**' % field
    if section.count(marker) != 1:
        raise SystemExit('field %s occurs %d times' % (field, section.count(marker)))
    position = section.index(marker) + 1
    lines = section[position:].split('\n')
    offset = len(lines[0]) + 1
    for line in lines[1:]:
        if line.startswith('- **'):
            return position + offset
        offset += len(line) + 1
    raise SystemExit('field %s runs to the end of its section' % field)


def append_to_check(text, entry_id, check_line):
    """Append '  - <check_line>' as the last sub-bullet of the entry's CHECK field."""
    if not check_line.startswith('S93 cross-examination:'):
        raise SystemExit('CHECK line for %s does not begin "S93 cross-examination:"' % entry_id)
    start, end = entry_span(text, entry_id)
    section = text[start:end]
    at = field_block_end(section, 'CHECK')
    section = section[:at] + '  - ' + check_line + '\n' + section[at:]
    return text[:start] + section + text[end:]
