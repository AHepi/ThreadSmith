"""
What this file does, in plain words.

Rule 1 of the owner's machine (log S135): RECOGNISE OBJECTS.
Origin: HANDED IN by the builders (Claude, for the owner, S135); written outside
the machine, run inside it.

The rule in plain words: a connected region of cells of one colour (cells
touching side by side) is one object. Empty cells are not objects. The screen's
colour is known to the machine as the screen (handed in with this rule), not
as an object. Declared limit: two objects of one colour that touch are seen as
one.
"""

ORIGIN = ('HANDED IN', 'Rule 1, recognise objects: written by the builders (Claude, for the owner, S135) '
          'outside the machine and run inside it; the machine did not form it.')
PLAIN_WORDS = ('A connected region of cells of one colour (touching side by side) is one object. Empty cells '
               'are not objects. The screen colour is the screen, not an object.')

EMPTY = 0
SCREEN_COLOUR = 9


class SeenObject:
    """One object as the machine sees it in one frame: its colour, its cells, its centre and its size."""

    def __init__(self, colour, cells):
        self.colour = colour
        self.cells = frozenset(cells)
        self.size = len(cells)
        self.centre = (sum(r for r, _ in cells) / len(cells), sum(c for _, c in cells) / len(cells))
        self.top = min(r for r, _ in cells)
        self.bottom = max(r for r, _ in cells)
        self.left = min(c for _, c in cells)
        self.right = max(c for _, c in cells)

    def __repr__(self):
        return 'SeenObject(colour=%d, size=%d, centre=(%.1f, %.1f))' % (self.colour, self.size, self.centre[0], self.centre[1])


def recognise_objects(frame):
    """Returns the list of objects in the frame (each a connected region of one colour), in reading order."""
    height, width = len(frame), len(frame[0])
    seen = set()
    objects = []
    for r in range(height):
        for c in range(width):
            colour = frame[r][c]
            if colour in (EMPTY, SCREEN_COLOUR) or (r, c) in seen:
                continue
            region = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                cr, cc = stack.pop()
                region.append((cr, cc))
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in seen and frame[nr][nc] == colour:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            objects.append(SeenObject(colour, region))
    return objects


def find_the_screen(frame):
    """Returns the screen's rectangle (top, bottom, left, right) if the screen is down in this frame, else None."""
    cells = [(r, c) for r, row in enumerate(frame) for c, v in enumerate(row) if v == SCREEN_COLOUR]
    if not cells:
        return None
    return (min(r for r, _ in cells), max(r for r, _ in cells), min(c for _, c in cells), max(c for _, c in cells))
