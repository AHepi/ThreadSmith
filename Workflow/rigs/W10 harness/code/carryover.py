"""Arm (c')'s carry-over note: the block the previous call wrote for the next one.

A RULE. W3 section 5: arm (c') is "fresh calls, one per step, each handed a carry-over note
the previous call wrote". W8 part B9 is the part under test, so the note must be the writing
call's own words and nothing of the rig's: this file only cuts the block out of the reply and
hands it on. It never rewrites it, shortens it or fills it in.

The reader is asked (ASK below, added to the user turn by arms.py) to end its reply with the block.
If the block is missing the note is None, `note_missing` goes into the run record, and the
next call is handed nothing in its place. A rig that quietly substituted the summariser here
would make arm (c') into arm (c) and P4.5's "(c') loses fewer cross-step fields than (c)"
would be measuring the rig.
"""
import re

OPEN = "=== CARRY-OVER NOTE ==="
CLOSE = "=== END OF CARRY-OVER NOTE ==="

ASK = (f"\n\nWhen you have finished this step, and after everything else you write, add the block below and "
       f"put in it whatever the next reader needs from you to do the next step. The next reader will be handed "
       f"your block and nothing else of yours.\n{OPEN}\n...your note...\n{CLOSE}\n")


def extract(reply):
    """Return (note, record). note is None when the writing call wrote no block."""
    if not reply:
        return None, {"note_missing": True, "reason": "empty reply"}
    m = re.search(re.escape(OPEN) + r"(.*?)" + re.escape(CLOSE), reply, re.S)
    if not m:
        m2 = re.search(re.escape(OPEN) + r"(.*)$", reply, re.S)     # cut off by a length limit
        if not m2:
            return None, {"note_missing": True, "reason": "no note block in the reply"}
        note = m2.group(1).strip()
        return (note or None), {"note_missing": not bool(note), "unclosed": True,
                                "note_words": len(note.split())}
    note = m.group(1).strip()
    return (note or None), {"note_missing": not bool(note), "unclosed": False,
                            "note_words": len(note.split())}


def strip_note(reply):
    """The reply without the block, for the record of what the step itself said."""
    return re.sub(re.escape(OPEN) + r".*?(" + re.escape(CLOSE) + r"|$)", "", reply or "", flags=re.S).strip()
