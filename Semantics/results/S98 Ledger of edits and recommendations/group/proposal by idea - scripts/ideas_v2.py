# The one adjustment to the "by idea" lens, made after measuring version 1.
# 1. Cue weights are scaled by how rare the cue is in the sentences of the ledger and the latest text
#    (inverse document frequency, divided by the median, kept between 0.4 and 1.6): words the theory
#    uses everywhere ("argument", "contract", "declared", "rules out") say little about which idea a
#    sentence carries.  The first cue of each idea, the one that names it, keeps at least its full weight.
# 2. The cue of 'ruling' made of the words the S95 scrub replaced ("true", "established", "fits" ...) is
#    narrowed to the words about ruling out and holding a claim ("refut", "reject", "verdict", "justif",
#    "certif"): the others stood in sentences of every idea.
# 3. Sentences that speak about the other ideas as a whole (Part XIV, Part XV, Part 0 "What is imported",
#    the front matter) carry their own idea whatever ideas they name: their home weight is 6, not 3, and a
#    change all of whose sentences stand there goes to that idea (the idea its words name is kept in "also").
# 4. A change that alters only punctuation, emphasis, a Part or Argument pointer, a tag number, or the
#    label Derivation/Proof to Argument/"Why this and not its denial" changes no idea: it goes to the
#    group 'form', and the idea of its sentence is kept in "also".
import math, re, collections, statistics

D = 6.0
DOMINANT = [("Front", "", ""), ("Part 0", "What is imported", ""), ("Part XIV ", "", ""), ("Part XV ", "", "")]
LAB = {'derivation', 'derivations', 'argument', 'arguments', 'proof', 'proofs', 'why', 'this', 'and', 'not', 'its',
       'denial', 'part', 'parts', 'see', 'in', 'of', 'the'}
NUM = re.compile(r'^(?:[ivx]+|\d+[a-z]?)$')

def toks(s):
    return re.findall(r"[A-Za-z]+|\d+", s or "")

def form_only(r):
    o, n = r["old"], r["new"]
    if not o or not n or n.startswith("[no wording") or r["scope"] in ("term", "whole text"):
        return False
    a = collections.Counter(t.lower() for t in toks(o)); b = collections.Counter(t.lower() for t in toks(n))
    d = (a - b) + (b - a)
    if not d:
        return True
    return all(t in LAB or NUM.match(t) for t in d)

def apply(X, texts):
    # 2
    X.IDEAS = [(k, n, r, [((r"refut|\breject|verdict|justif|certif", w) if rx.startswith(r"\btrue\b") else (rx, w)) for rx, w in cues])
               for k, n, r, cues in X.IDEAS]
    X.IDEAS.append(("form", "Form only: punctuation, emphasis, pointers and labels",
                    "changes that alter no wording of an idea: punctuation, bold or italics, a Part or Argument pointer, a tag number, or the labels `Derivation` and `Proof` renamed",
                    []))
    X.KEYS = [k for k, *_ in X.IDEAS]
    comp = {k: [(re.compile(rx) if "\\\\" in rx else re.compile(rx, re.I), w) for rx, w in cues] for k, n, r, cues in X.IDEAS}
    # 1
    N = len(texts)
    idf = {}
    for k, cues in comp.items():
        for rx, w in cues:
            df = sum(1 for t in texts if rx.search(t))
            idf[(k, rx.pattern)] = math.log(N / max(df, 1))
    med = statistics.median(idf.values())
    X.IDF = {key: max(0.4, min(1.6, v / med)) for key, v in idf.items()}
    for k, cues in comp.items():  # the cue that names the idea keeps at least its full weight
        if cues:
            X.IDF[(k, cues[0][0].pattern)] = max(1.0, X.IDF[(k, cues[0][0].pattern)])
    X.COMPILED = {k: [(rx, w * X.IDF[(k, rx.pattern)]) for rx, w in cues] for k, cues in comp.items()}
    # 3
    for key in list(X.HOME_LABEL):
        if any(key[0] == p and key[1].startswith(h) and key[2].startswith(l) for p, h, l in DOMINANT):
            X.HOME_LABEL[key] = [(i, D) for i, w in X.HOME_LABEL[key]]
    X.form_only = form_only
    def dominant_home(part, heading, label):
        pk = X.part_key(part)
        for p, h, l in DOMINANT:
            if pk == p and heading.startswith(h) and label.startswith(l):
                hm = X.home(part, heading, label)
                return hm[0][0] if hm else None
        return None
    X.DOMINANT_HOME = dominant_home
