"""
What this file does, in plain words.

Rule 3 of the owner's machine (log S135): OBJECT PERMANENCE.
Origin: HANDED IN by the builders (Claude, for the owner, S135); written outside
the machine, run inside it.

The rule in plain words: an object that goes out of sight at the screen is
still there, at its last predicted place, kept behind the screen (its predicted
place moves with its last move but cannot leave the screen or pass the floor).
If its predicted path carries it out of a side or the top of the screen, it is
EXPECTED TO COME OUT there; if it does not appear within two frames, that is a
violation ("did not come out"), and it is then held at rest behind the screen.
An object that appears at the screen's edge is matched to a held one of the
same colour (the nearest); if none of that colour is held, that is a violation
("a different one came out"). When the screen lifts, a held object not found
is a violation ("was not there").

Capacity, declared by the builders: at most THREE individual hidden objects
are held at once, each with its place and colour. When a fourth goes behind,
the oldest is dropped, and the drop is logged.

Rule 3 also lets the machine keep an AMOUNT for a region it can no longer see
(what went out of sight is still there). With rule 3 switched off, nothing out
of sight is kept: neither individual objects nor amounts.
"""

import math

ORIGIN = ('HANDED IN', 'Rule 3, object permanence: written by the builders (Claude, for the owner, S135) '
          'outside the machine and run inside it; its capacity of three is the builders\' choice; '
          'the machine did not form it.')
PLAIN_WORDS = ('An object that goes out of sight behind the screen is still there, at its last predicted place, '
               'and is expected to come out where its path leads; at most three are held one by one.')

CAPACITY = 3
GRACE_FRAMES = 2
FLOOR_ROW = 15


class HiddenObject:
    """One object held behind the screen: its colour, size, predicted outline and move."""

    def __init__(self, track, frame_index, screen):
        self.colour = track.colour
        self.size = track.size
        self.outline = list(track.outline)
        self.move = track.last_move
        self.frame_hidden = frame_index
        self.screen = screen
        self.expected_out_at = None
        self.flagged_did_not_come_out = False
        self.from_track_number = track.number

    def centre(self):
        top, bottom, left, right = self.outline
        return ((top + bottom) / 2, (left + right) / 2)


def _fully_behind(outline, screen):
    top, bottom, left, right = outline
    s_top, s_bottom, s_left, s_right = screen
    return s_top <= top and bottom <= s_bottom and s_left <= left and right <= s_right


def hide(held, track, frame_index, screen, capacity=CAPACITY):
    """Holds a track that went out of sight at the screen. Returns the dropped object, if the capacity was exceeded."""
    held.append(HiddenObject(track, frame_index, screen))
    if len(held) > capacity:
        return held.pop(0)
    return None


def step_hidden_objects(held, frame_index):
    """Moves every held object along its predicted path for one frame; returns the violations ("did not come out")."""
    violations = []
    for h in held:
        if h.flagged_did_not_come_out:
            continue
        dr, dc = h.move
        top, bottom, left, right = h.outline
        if bottom + dr > FLOOR_ROW:
            dr = 0
        new_outline = [top + dr, bottom + dr, left + dc, right + dc]
        if _fully_behind(new_outline, h.screen):
            h.outline = new_outline
            continue
        # its path leads out of the screen: it is expected to come out
        if h.expected_out_at is None:
            h.expected_out_at = frame_index
            h.outline = new_outline
        elif frame_index - h.expected_out_at >= GRACE_FRAMES:
            violations.append(('did not come out', {'colour': h.colour, 'expected at frame': h.expected_out_at}))
            h.flagged_did_not_come_out = True
            h.move = (0, 0)
            s_top, s_bottom, s_left, s_right = h.screen
            height, width = bottom - top, right - left
            new_left = min(max(left, s_left), s_right - width)
            new_top = min(max(top, s_top), s_bottom - height)
            h.outline = [new_top, new_top + height, new_left, new_left + width]
    return violations


def come_out(held, seen_object):
    """An object appeared at the screen's edge: returns the held object it is (same colour, nearest), removed from the held list, or None."""
    same_colour = [h for h in held if h.colour == seen_object.colour]
    if not same_colour:
        return None
    nearest = min(same_colour, key=lambda h: (math.dist(h.centre(), seen_object.centre), h.frame_hidden))
    held.remove(nearest)
    return nearest


def check_after_the_lift(held, revealed_objects):
    """When the screen lifts: every held object should be among those revealed (by colour). Returns the violations."""
    remaining = [o.colour for o in revealed_objects]
    violations = []
    for h in held:
        if h.colour in remaining:
            remaining.remove(h.colour)
        else:
            violations.append(('was not there', {'colour': h.colour}))
    return violations
