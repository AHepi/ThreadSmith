"""
What this file does, in plain words.

Rule 2 of the owner's machine (log S135): DISPLACEMENT.
Origin: HANDED IN by the builders (Claude, for the owner, S135); written outside
the machine, run inside it.

The rule in plain words: an object seen at a new place is the same object
moved, if it has the same colour and is the nearest such object to where that
object was expected, within a bounded step (3 cells; 2.5 in the design, raised when a diagonal bounce, 2.83 cells from the predicted place, was found unmatched). Each tracked object
carries its last move; its next place is predicted as its place plus its last
move. When the object is found away from the predicted place, that is a
VIOLATION of the prediction (the theory's D12.7), and it is logged. An object
that cannot be matched, and was not at the screen or at an edge of the world,
has vanished in plain sight (a violation); a new object away from the screen
and the edges has appeared from nowhere (a violation). Objects entering or
leaving at an edge, and every object in the first frame of a scene, are not
violations.

How a move is read: the move of an object is read from the edges of its
outline; when the screen hides part of it, the edge the screen does not clip
gives the move (the larger of the two edge moves).
"""

import math

ORIGIN = ('HANDED IN', 'Rule 2, displacement: written by the builders (Claude, for the owner, S135) '
          'outside the machine and run inside it; the machine did not form it.')
PLAIN_WORDS = ('An object seen at a new place is the same object moved (same colour, nearest to where it was '
               'expected, within 3 cells); its next place is its place plus its last move; a miss is a violation.')

BOUNDED_STEP = 3.0  # 2.5 in the design; raised to 3.0 in building: a diagonal bounce moves the object 2.83 cells from its predicted place


class Track:
    """One object the machine is following from frame to frame."""

    def __init__(self, number, seen_object, frame_index):
        self.number = number
        self.colour = seen_object.colour
        self.size = seen_object.size
        self.centre = seen_object.centre
        self.outline = (seen_object.top, seen_object.bottom, seen_object.left, seen_object.right)
        self.cells = seen_object.cells
        self.last_move = (0, 0)
        self.has_moved_once = False
        self.first_frame = frame_index
        self.came_from_behind_the_screen = False

    def predicted_centre(self):
        return (self.centre[0] + self.last_move[0], self.centre[1] + self.last_move[1])


def _edge_move(old_low, old_high, new_low, new_high):
    low, high = new_low - old_low, new_high - old_high
    if low == high:
        return low
    if abs(low) == abs(high):
        return 0
    return low if abs(low) > abs(high) else high


def match_objects_to_tracks(tracks, seen_objects, bounded_step=BOUNDED_STEP):
    """Greedy matching, nearest first: same colour, within the bounded step of the predicted place.
    Returns (pairs of (track, seen object), unmatched tracks, unmatched seen objects)."""
    candidates = []
    for ti, track in enumerate(tracks):
        predicted = track.predicted_centre()
        for oi, seen in enumerate(seen_objects):
            if seen.colour != track.colour:
                continue
            distance = math.dist(predicted, seen.centre)
            if distance <= bounded_step:
                candidates.append((distance, ti, oi))
    candidates.sort()
    used_tracks, used_objects, pairs = set(), set(), []
    for distance, ti, oi in candidates:
        if ti in used_tracks or oi in used_objects:
            continue
        used_tracks.add(ti)
        used_objects.add(oi)
        pairs.append((tracks[ti], seen_objects[oi]))
    unmatched_tracks = [t for i, t in enumerate(tracks) if i not in used_tracks]
    unmatched_objects = [o for i, o in enumerate(seen_objects) if i not in used_objects]
    return pairs, unmatched_tracks, unmatched_objects


def move_track(track, seen_object):
    """Moves the track to the object's new place; returns (the move, the prediction error in cells, violated?)."""
    top, bottom, left, right = track.outline
    move = (_edge_move(top, bottom, seen_object.top, seen_object.bottom),
            _edge_move(left, right, seen_object.left, seen_object.right))
    error = max(abs(move[0] - track.last_move[0]), abs(move[1] - track.last_move[1]))
    violated = error >= 1 and track.has_moved_once
    track.last_move = move
    track.has_moved_once = True
    track.centre = seen_object.centre
    track.outline = (seen_object.top, seen_object.bottom, seen_object.left, seen_object.right)
    track.cells = seen_object.cells
    track.size = max(track.size, seen_object.size)
    return move, error, violated


def at_an_edge_of_the_world(outline, grid_size=16, floor_is_an_edge=False):
    """True when the outline touches the top, left or right edge (the doors of the world)."""
    top, bottom, left, right = outline
    return top <= 0 or left <= 0 or right >= grid_size - 1 or (floor_is_an_edge and bottom >= grid_size - 1)


def predicted_to_leave_the_world(track, grid_size=16):
    """True when the track's predicted place takes it beyond the top, left or right edge."""
    top, bottom, left, right = track.outline
    dr, dc = track.last_move
    return top + dr < 0 or left + dc < 0 or right + dc > grid_size - 1 or (top <= 0 and dr < 0) or \
        (left <= 0 and dc < 0) or (right >= grid_size - 1 and dc > 0)
