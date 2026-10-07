# S107 round 4, area 3 (B14, W6, S1): the formal core that FC14 and FC32.new1 read, found in one place.
# Before round 4 each claim kept its own list of places and fell back to older cores: from a copy of the program
# away from the S106 folder both read the formal core after round 3 without saying so, and in the readers' sandbox
# (maths/formal core, now.md beside model/) FC14 found none and FC32.new1 raised FileNotFoundError.
# Now: one list, tried in order; the first place holding the file is read, and its name and md5 are printed by the
# claims; no older core is read in its place; if none is found, the claim part that reads it is not tested.
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))  # the model/ folder
NAME = "formal core, after S106.md"  # the formal core this program formalizes
PLACES = (
    ("beside the program's folder (the committed layout)", os.path.join(HERE, "..", "..", NAME)),
    ("its committed folder, from a copy of the program under results/",
     os.path.join(HERE, "..", "..", "..", "S106 The written-in test taken out", NAME)),
    ("maths/ beside model/ (the readers' sandbox)", os.path.join(HERE, "..", "maths", "formal core, now.md")),
)


def formal_core():
    """(path, md5) of the formal core the claims read; (None, the places tried) when none is found."""
    for _, p in PLACES:
        if os.path.isfile(p):
            with open(p, "rb") as f:
                return os.path.normpath(p), hashlib.md5(f.read()).hexdigest()
    return None, "; ".join("%s: %s" % (w, os.path.normpath(p)) for w, p in PLACES)


def describe(path, md5):
    return "%s (md5 %s)" % (os.path.basename(path), md5)
