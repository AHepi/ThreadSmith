# S104 round 2 (maths): quotation check.
# Every quotation of the text under review is checked against the line it names.
# A quotation may join fragments with " … "; the fragments must occur in that order on the line.
import hashlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.join(HERE, "..", "..", "tests", "103 The semantics, standing alone, after round 1.md")
MD5 = "f31ebb1f050783f1a84f6136cec20fcd"


def load_text():
    raw = open(TEXT, "rb").read()
    got = hashlib.md5(raw).hexdigest()
    if got != MD5:
        sys.exit("text under review changed: md5 %s, expected %s" % (got, MD5))
    return raw.decode("utf-8").split("\n")


LINES = load_text()


def check(line, quote):
    """Return None if the quotation stands on the line, else a message."""
    if not (1 <= line <= len(LINES)):
        return "L%d: no such line" % line
    src = LINES[line - 1]
    pos = 0
    for frag in [f.strip() for f in quote.split("…")]:
        if not frag:
            continue
        i = src.find(frag, pos)
        if i < 0:
            return "L%d: not found in order: %r" % (line, frag[:90])
        pos = i + len(frag)
    return None


QUOTE_MD = re.compile(r"^> L(\d+) \| (.*)$")


def check_markdown(path):
    bad, n = [], 0
    for k, row in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        m = QUOTE_MD.match(row)
        if m:
            n += 1
            msg = check(int(m.group(1)), m.group(2))
            if msg:
                bad.append("%s:%d %s" % (os.path.basename(path), k, msg))
    return n, bad


if __name__ == "__main__":
    total, bad = 0, []
    for name in sorted(os.listdir(HERE)):
        if name.endswith(".md"):
            n, b = check_markdown(os.path.join(HERE, name))
            total += n
            bad += b
    print("quotations checked in the .md files:", total)
    for b in bad:
        print("  BAD", b)
    print("all found" if not bad else "%d not found" % len(bad))
