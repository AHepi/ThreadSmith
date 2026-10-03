"""
What this file does, in plain words.

This is the tiny world the machine lives in (log S135, the owner's machine).
It is a 16 by 16 grid of cells. Each cell holds one number: 0 is empty, 1 to 8
are the colours of objects, 9 is the screen. Objects are blobs of one colour
that move at most one cell per frame. The screen is a rectangle that can come
down (it is drawn over whatever is behind it) and lift (it is gone).

The world makes SCENES from a seed. Nobody writes a scene by hand: the kind of
scene and every number in it are drawn from the seed. A scene is a list of
frames (what the machine sees, nothing else) and a truth log (what really
happened, kept only for scoring; the machine never reads it).

Kinds of scene:
  walk          objects move in the open, bounce, sometimes turn or jump
  pass behind   an object walks across behind the screen (it comes out, or
                stays behind, or, in tests only, vanishes or comes out as a
                different one)
  amounts       objects rest on the stage, the screen comes down, a group is
                added from the top, sometimes a group walks out, the screen
                lifts (in tests only, the lift can show one more or one fewer
                than are really there: the infant studies' impossible event)
"""

import random

GRID_SIZE = 16
EMPTY = 0
SCREEN_COLOUR = 9
BUILDING_COLOURS = [1, 2, 3, 4, 5, 6]
TEST_ONLY_COLOURS = [7, 8]
SCREEN_TOP, SCREEN_BOTTOM, SCREEN_LEFT, SCREEN_RIGHT = 6, 15, 3, 12
SHAPES_WHILE_BUILDING = [(1, 1)]
SHAPES_IN_TESTS = [(1, 1), (1, 1), (2, 2), (1, 2), (2, 1)]


class WorldObject:
    """One true object: its own number, colour, shape (height, width) and top-left cell."""

    def __init__(self, true_number, colour, shape, row, column):
        self.true_number = true_number
        self.colour = colour
        self.height, self.width = shape
        self.row = row
        self.column = column

    def cells(self):
        return [(self.row + r, self.column + c) for r in range(self.height) for c in range(self.width)]

    def copy(self):
        return WorldObject(self.true_number, self.colour, (self.height, self.width), self.row, self.column)


def inside_screen(row, column):
    return SCREEN_TOP <= row <= SCREEN_BOTTOM and SCREEN_LEFT <= column <= SCREEN_RIGHT


def render(objects, screen_down):
    """The frame the machine sees: a tuple of 16 rows of 16 numbers, and the map of which true object owns each visible cell."""
    grid = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
    owner = {}
    for world_object in objects:
        for (r, c) in world_object.cells():
            if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                grid[r][c] = world_object.colour
                owner[(r, c)] = world_object.true_number
    if screen_down:
        for r in range(SCREEN_TOP, SCREEN_BOTTOM + 1):
            for c in range(SCREEN_LEFT, SCREEN_RIGHT + 1):
                grid[r][c] = SCREEN_COLOUR
                owner.pop((r, c), None)
    return tuple(tuple(row) for row in grid), owner


class Scene:
    """A scene: frames for the machine; truth for scoring only."""

    def __init__(self, kind, label):
        self.kind = kind
        self.label = label
        self.frames = []
        self.truth_per_frame = []
        self.events = []
        self.facts = {}

    def add_frame(self, objects, screen_down):
        frame, owner = render(objects, screen_down)
        self.frames.append(frame)
        self.truth_per_frame.append({
            'owner_of_visible_cell': owner,
            'objects': [(o.true_number, o.colour, o.row, o.column, o.height, o.width) for o in objects],
            'screen_down': screen_down,
            'true_amount_behind_screen': sum(1 for o in objects if all(inside_screen(r, c) for (r, c) in o.cells())) if screen_down else None,
        })


def _cells_with_gap(row, column, height, width):
    return {(row + r, column + c) for r in range(-1, height + 1) for c in range(-1, width + 1)}


def pack_on_stage(shapes, already_taken_cells, rng):
    """Places objects of the given shapes on the stage (inside the screen's rectangle) with an empty cell between any two."""
    places = []
    taken = set(already_taken_cells)
    candidate_corners = [(r, c) for r in range(SCREEN_TOP, SCREEN_BOTTOM + 1) for c in range(SCREEN_LEFT, SCREEN_RIGHT + 1)]
    rng.shuffle(candidate_corners)
    candidate_corners.sort(key=lambda rc: (rc[0] % 2, rc[1] % 2))  # prefer an even lattice, so many fit
    for (height, width) in shapes:
        placed = False
        for (r, c) in candidate_corners:
            cells = {(r + dr, c + dc) for dr in range(height) for dc in range(width)}
            if not all(inside_screen(rr, cc) for (rr, cc) in cells):
                continue
            if cells & taken:
                continue
            places.append((r, c))
            taken |= _cells_with_gap(r, c, height, width)
            placed = True
            break
        if not placed:
            return None
    return places


def _choose_shapes(rng, count, shapes_allowed):
    return [rng.choice(shapes_allowed) for _ in range(count)]


def _choose_colours(rng, count, colours_allowed):
    return [rng.choice(colours_allowed) for _ in range(count)]


def amounts_scene(rng, before, added, taken_away, impossible=None, colours=BUILDING_COLOURS,
                  shapes=SHAPES_WHILE_BUILDING, delay_before_group=None, lift=True, total_frames=None,
                  label='amounts'):
    """
    Objects rest on the stage; the screen comes down; a group of `added` objects appears at the top in
    one row and descends behind the screen; optionally a group of `taken_away` objects walks out from
    behind the screen, one above another, and leaves at a side edge; the screen lifts.
    `impossible` may be None, 'one more' or 'one fewer' (the lift shows that many more or fewer).
    Returns None if the objects do not fit (the caller draws again).
    """
    assert taken_away <= before + added
    for _attempt in range(20):
        result = _try_amounts_scene(rng, before, added, taken_away, impossible, colours, shapes,
                                    delay_before_group, lift, total_frames, label)
        if result is not None:
            return result
        shapes = [(1, 1)]
    return None


def _try_amounts_scene(rng, before, added, taken_away, impossible, colours, shapes, delay_before_group,
                       lift, total_frames, label):
    scene = Scene('amounts', label)
    next_number = [1]

    def new_object(colour, shape, row, column):
        o = WorldObject(next_number[0], colour, shape, row, column)
        next_number[0] += 1
        return o

    # the group added from the top: one row, an empty cell between neighbours, inside the screen's columns
    group_shapes = _choose_shapes(rng, added, shapes)
    group_columns = []
    column = SCREEN_LEFT
    for (height, width) in group_shapes:
        if column + width - 1 > SCREEN_RIGHT:
            return None
        group_columns.append(column)
        column += width + 1
    spare = SCREEN_RIGHT - (column - 2)
    shift = rng.randint(0, max(0, spare)) if added else 0
    group_columns = [c + shift for c in group_columns]
    group_colours = _choose_colours(rng, added, colours)

    before_shapes = _choose_shapes(rng, before, shapes)
    before_places = pack_on_stage(before_shapes, set(), rng)
    if before_places is None:
        return None
    before_objects = [new_object(colour, shape, r, c) for colour, shape, (r, c) in
                      zip(_choose_colours(rng, before, colours), before_shapes, before_places)]
    taken_cells = set()
    for o in before_objects:
        taken_cells |= _cells_with_gap(o.row, o.column, o.height, o.width)
    resting_places = pack_on_stage(group_shapes, taken_cells, rng)
    if resting_places is None:
        return None
    group_objects = [new_object(colour, shape, 0, c) for colour, shape, c in zip(group_colours, group_shapes, group_columns)]

    # who walks out: chosen from those present; they come out on one side, one above another
    present = before_objects + group_objects
    leaving = rng.sample(present, taken_away) if taken_away else []
    side = rng.choice(['left', 'right'])
    leaving_rows = []
    row = SCREEN_TOP
    for o in leaving:
        if row + o.height - 1 > SCREEN_BOTTOM:
            return None
        leaving_rows.append(row)
        row += o.height + 1

    if delay_before_group is None:
        delay_before_group = rng.randint(1, 4)
    objects = list(before_objects)
    scene.add_frame(objects, screen_down=False)
    scene.add_frame(objects, screen_down=False)
    scene.events.append((2, 'screen comes down', {}))
    scene.add_frame(objects, screen_down=True)
    for _ in range(delay_before_group):
        scene.add_frame(objects, screen_down=True)
    if added:
        scene.events.append((len(scene.frames), 'group appears at the top', {'amount': added}))
        objects = objects + group_objects
        while any(o.row < SCREEN_TOP for o in group_objects):
            scene.add_frame(objects, screen_down=True)
            for o in group_objects:
                o.row += 1
        scene.events.append((len(scene.frames), 'group goes behind the screen', {'amount': added}))
        scene.add_frame(objects, screen_down=True)
        for o, (r, c) in zip(group_objects, resting_places):
            o.row, o.column = r, c
    scene.add_frame(objects, screen_down=True)
    if taken_away:
        scene.add_frame(objects, screen_down=True)
        for o, r in zip(leaving, leaving_rows):
            o.row = r
            o.column = SCREEN_LEFT - o.width if side == 'left' else SCREEN_RIGHT + 1
        scene.events.append((len(scene.frames), 'group comes out', {'amount': taken_away, 'side': side}))
        step = -1 if side == 'left' else 1
        while any(0 <= o.column + dc < GRID_SIZE for o in leaving for dc in range(o.width)):
            scene.add_frame(objects, screen_down=True)
            for o in leaving:
                o.column += step
        objects = [o for o in objects if o not in leaving]
        scene.add_frame(objects, screen_down=True)
    true_after = before + added - taken_away
    if total_frames is not None:
        while len(scene.frames) < total_frames - (3 if lift else 0):
            scene.add_frame(objects, screen_down=True)
    shown = list(objects)
    if lift:
        if impossible == 'one fewer':
            if not shown:
                return None
            shown = shown[:-1]
            scene.events.append((len(scene.frames), 'impossible: one taken secretly', {}))
        elif impossible == 'one more':
            taken = set()
            for o in shown:
                taken |= _cells_with_gap(o.row, o.column, o.height, o.width)
            place = pack_on_stage([(1, 1)], taken, rng)
            if place is None:
                return None
            shown = shown + [new_object(rng.choice(colours), (1, 1), place[0][0], place[0][1])]
            scene.events.append((len(scene.frames), 'impossible: one added secretly', {}))
        scene.events.append((len(scene.frames), 'screen lifts', {}))
        scene.add_frame(shown, screen_down=False)
        scene.add_frame(shown, screen_down=False)
        scene.add_frame(shown, screen_down=False)
    if total_frames is not None and len(scene.frames) != total_frames:
        return None
    scene.facts = {'before': before, 'added': added, 'taken away': taken_away, 'true after': true_after,
                   'shown after': len(shown) if lift else None, 'impossible': impossible, 'lift': lift,
                   'delay before group': delay_before_group}
    return scene


def pass_behind_scene(rng, variant='comes out', two=False, colours=BUILDING_COLOURS, shapes=SHAPES_WHILE_BUILDING,
                      label='pass behind'):
    """
    The screen is up over an empty stage, comes down, and one object (or two, one above the other) walks
    across behind it. Variants: 'comes out', 'stays behind', and for tests only 'vanishes', 'different one'.
    """
    scene = Scene('pass behind', label)
    count = 2 if two else 1
    chosen_shapes = _choose_shapes(rng, count, shapes)
    rows = []
    row = rng.randint(SCREEN_TOP, SCREEN_TOP + 2)
    for (height, width) in chosen_shapes:
        rows.append(row)
        row += height + 1 + rng.randint(0, 2)
    if row - 1 > SCREEN_BOTTOM + 1:
        rows = [SCREEN_TOP + 2 * i for i in range(count)]
        chosen_shapes = [(1, 1)] * count
    direction = rng.choice([1, -1])
    walkers = []
    for i, ((height, width), r) in enumerate(zip(chosen_shapes, rows)):
        start_column = -width + 1 if direction == 1 else GRID_SIZE - 1
        walkers.append(WorldObject(i + 1, rng.choice(colours), (height, width), r, start_column))
    objects = []
    scene.add_frame(objects, screen_down=False)
    scene.events.append((1, 'screen comes down', {}))
    scene.add_frame(objects, screen_down=True)
    objects = list(walkers)
    stop_column = rng.randint(SCREEN_LEFT + 2, SCREEN_RIGHT - 3)
    changed = False
    frames_walked = 0
    while objects and frames_walked < 40:
        scene.add_frame(objects, screen_down=True)
        frames_walked += 1
        for o in list(objects):
            fully_hidden = all(inside_screen(r, c) for (r, c) in o.cells())
            if variant in ('stays behind', 'vanishes') and fully_hidden and (
                    (direction == 1 and o.column >= stop_column) or (direction == -1 and o.column <= stop_column)):
                if variant == 'vanishes' and o in objects:
                    objects.remove(o)
                    scene.events.append((len(scene.frames), 'impossible: vanished behind the screen', {'true number': o.true_number}))
                continue
            if variant == 'different one' and fully_hidden and not changed and (
                    (direction == 1 and o.column >= stop_column) or (direction == -1 and o.column <= stop_column)):
                new_colour = rng.choice([c for c in colours if c != o.colour])
                replacement = WorldObject(o.true_number + 100, new_colour, (o.height, o.width), o.row, o.column)
                objects[objects.index(o)] = replacement
                o = replacement
                changed = True
                scene.events.append((len(scene.frames), 'impossible: a different one continues', {}))
            o.column += direction
        objects = [o for o in objects if any(0 <= c < GRID_SIZE for (_, c) in o.cells())]
        if variant in ('stays behind', 'vanishes') and all(
                all(inside_screen(r, c) for (r, c) in o.cells()) and
                ((direction == 1 and o.column >= stop_column) or (direction == -1 and o.column <= stop_column))
                for o in objects):
            if variant == 'vanishes':
                for o in objects:
                    scene.events.append((len(scene.frames), 'impossible: vanished behind the screen', {'true number': o.true_number}))
                objects = []
            # long enough for the expected way out to pass, with its grace
            for _ in range(14):
                scene.add_frame(objects, screen_down=True)
            break
    scene.add_frame(objects, screen_down=True)
    scene.events.append((len(scene.frames), 'screen lifts', {}))
    scene.add_frame(objects, screen_down=False)
    scene.add_frame(objects, screen_down=False)
    true_after = len(objects)
    scene.facts = {'before': 0, 'added': count, 'taken away': count if variant in ('comes out', 'different one') else 0,
                   'true after': true_after, 'shown after': true_after, 'impossible': None if variant in ('comes out', 'stays behind') else variant,
                   'variant': variant, 'lift': True}
    return scene


def walk_scene(rng, number_of_objects, colours=BUILDING_COLOURS, shapes=SHAPES_WHILE_BUILDING, frames=24,
               chance_of_turn=0.08, chance_of_jump=0.0, label='walk'):
    """Objects move in the open (no screen), bounce off walls and each other, sometimes turn, sometimes jump."""
    scene = Scene('walk', label)
    distinct_colours = rng.sample(colours, min(number_of_objects, len(colours)))
    objects, moves = [], {}
    taken = set()
    for i in range(number_of_objects):
        shape = rng.choice(shapes)
        for _ in range(200):
            r = rng.randint(1, GRID_SIZE - 1 - shape[0])
            c = rng.randint(1, GRID_SIZE - 1 - shape[1])
            cells = {(r + dr, c + dc) for dr in range(shape[0]) for dc in range(shape[1])}
            if not cells & taken:
                break
        o = WorldObject(i + 1, distinct_colours[i % len(distinct_colours)], shape, r, c)
        taken |= _cells_with_gap(r, c, shape[0], shape[1])
        objects.append(o)
        moves[o.true_number] = rng.choice([(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)])
    scene.add_frame(objects, screen_down=False)
    for t in range(1, frames):
        for o in objects:
            kind = 'straight'
            move = moves[o.true_number]
            if rng.random() < chance_of_jump and 3 <= o.row <= 11 and 3 <= o.column <= 11:
                others = set()
                for p in objects:
                    if p is not o:
                        others |= _cells_with_gap(p.row, p.column, p.height, p.width)
                for _ in range(100):
                    r = rng.randint(2, GRID_SIZE - 3 - o.height)
                    c = rng.randint(2, GRID_SIZE - 3 - o.width)
                    if abs(r - o.row) + abs(c - o.column) >= 6 and not ({(r + a, c + b) for a in range(o.height) for b in range(o.width)} & others):
                        o.row, o.column = r, c
                        kind = 'jump'
                        break
                scene.events.append((t, kind, {'true number': o.true_number}))
                continue
            if rng.random() < chance_of_turn:
                move = rng.choice([(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0) and (dr, dc) != move])
                kind = 'turn'
            new_row, new_column = o.row + move[0], o.column + move[1]
            if new_row < 0 or new_row + o.height > GRID_SIZE:
                move = (-move[0], move[1]); kind = 'bounce'
            if new_column < 0 or new_column + o.width > GRID_SIZE:
                move = (move[0], -move[1]); kind = 'bounce'
            new_row, new_column = o.row + move[0], o.column + move[1]
            others = set()
            for p in objects:
                if p is not o:
                    others |= {(p.row + a, p.column + b) for a in range(p.height) for b in range(p.width)}
            mine = {(new_row + a, new_column + b) for a in range(o.height) for b in range(o.width)}
            if mine & others or not (0 <= new_row and new_row + o.height <= GRID_SIZE and 0 <= new_column and new_column + o.width <= GRID_SIZE):
                # blocked by another object: it stays this frame and picks a new direction
                kind = 'blocked'
                new_row, new_column = o.row, o.column
                move = rng.choice([(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)])
            o.row, o.column = new_row, new_column
            if kind != 'straight':
                scene.events.append((t, kind, {'true number': o.true_number}))
            moves[o.true_number] = move
        scene.add_frame(objects, screen_down=False)
    scene.facts = {'lift': False}
    return scene


def random_still_frame(rng, allow_same_colour_touching):
    """A single frame of random blobs, for the recognition test; returns the frame, the true number of objects, and whether two of one colour touch."""
    objects = []
    occupied = set()
    for i in range(rng.randint(1, 8)):
        shape = rng.choice(SHAPES_IN_TESTS)
        colour = rng.choice(BUILDING_COLOURS + TEST_ONLY_COLOURS)
        for _ in range(100):
            r = rng.randint(0, GRID_SIZE - shape[0])
            c = rng.randint(0, GRID_SIZE - shape[1])
            cells = {(r + a, c + b) for a in range(shape[0]) for b in range(shape[1])}
            if cells & occupied:
                continue
            o = WorldObject(i + 1, colour, shape, r, c)
            touching_same = any(p.colour == colour and (_cells_with_gap(p.row, p.column, p.height, p.width) & cells) for p in objects)
            if touching_same and not allow_same_colour_touching:
                continue
            objects.append(o)
            occupied |= cells
            break
    frame, _ = render(objects, screen_down=False)
    touching = False
    for i, p in enumerate(objects):
        for q in objects[i + 1:]:
            if p.colour == q.colour:
                pc = set(p.cells())
                if any((r + dr, c + dc) in pc for (r, c) in q.cells() for (dr, dc) in ((0, 1), (0, -1), (1, 0), (-1, 0))):
                    touching = True
    return frame, len(objects), touching


def building_schedule(seed=1350, number_of_scenes=120, largest_amount=None):
    """The building schedule: about half amounts scenes, a quarter pass behind, a quarter walk; an honest world."""
    rng = random.Random(seed)
    scenes = []
    while len(scenes) < number_of_scenes:
        draw = rng.random()
        if draw < 0.5:
            before = rng.randint(0, 4)
            added = rng.randint(1, 3)
            taken = rng.randint(0, min(2, before + added))
            if largest_amount is not None and (before > largest_amount or before + added > largest_amount):
                continue
            scene = amounts_scene(rng, before, added, taken, label='building amounts')
        elif draw < 0.75:
            scene = pass_behind_scene(rng, variant=rng.choice(['comes out', 'stays behind']), two=rng.random() < 0.3,
                                      label='building pass behind')
        else:
            scene = walk_scene(rng, rng.randint(1, 4), chance_of_turn=0.05, label='building walk')
        if scene is not None:
            scenes.append(scene)
    return scenes
