# build_w16.py - plan W16's builder, frozen in the plan's Appendix B. It sends nothing and
# reads no key. It builds the system message and the three user messages (one per lens; the
# same bytes go to both families) from the plan's Appendix A and the repository's files; it
# refuses if any source, or any message it builds, differs from the hash the plan froze; and
# with --out DIR it writes what it built and a manifest. Run:
#   /home/user/.venvs/threadsmith/bin/python build_w16.py "<path of the W16 plan>" [--out DIR]
import hashlib
import json
import os
import sys

FENCE = "`" * 3
SKILL_DIR = "HV Skill/authority/33/hard-to-vary/"
SKILL_FILES = [  # the rig's order (rig.SKILL_FILES), with each file's sha256 at freezing
    ("SKILL.md", "ac7a36814421f8adb1df925ac23343dd530de690cefcfc7877f6a66e183f42fd"),
    ("references/the-idea-in-depth.md", "eb19f2dbd7563121183726528540214c03df4ef7db22586f61022a90b7f51562"),
    ("references/question-bank.md", "8256d45ba2fe59ded89e4e23a26e9dd9b00d111177ddf1803fbc1d417e82c56a"),
    ("references/by-domain.md", "c632d4d82c1bb407f362b6697c0f973547e09112687d8a32b0c3892293a9a153"),
    ("references/building.md", "995c5d631809509234df72500a7d852265a1cbb0ad38bdeef437bddf4a71eb7a"),
    ("references/testing-against-cases.md", "ba3462d4dc1e9d3b58bd2194ffb594f7ec77951383d2bd3484af27c27b63f4d9"),
    ("references/reporting.md", "4d032633d4fd8878f46b599b45028a02818a31cc84e43b43f8889915e1c69e68"),
    ("references/word-list.md", "1f09fe7444db59d3843026ed4cdb60624cde42cdf5e198b331daf541fd009b3c"),
]
W = "Workflow/"
H = W + "rigs/W10 harness/"
W10 = W + ("tests/W10 Plan - getting the LLM theory right; the harness, the corpus, the fourth "
           "clause, the instrument, the arms, the cross-examination.md")
MP = H + "instrument/marking-plan.md"
WHOLE = {  # sha256 of each whole file an excerpt is cut from
    W10: "0210a42236d759b41a366397870d324291b8d1a82492904fc856a5c84b7f395c",
    MP: "dc855edde802e7509a38ae3ce372d2d2d5d4526b6466136bbcde14d8d8f3b017",
}
DOCS = [  # (path from the repository root, first line, last line (None: whole), label, sha256 of the bytes sent)
    (H + "stage-B/questioning/W15-draft-as-questioned.md", None, None,
     "the draft under question, W15, copied byte for byte",
     "cff3373b23ec4a91f2ca7266b9c4edc2430d221c26caf8c8cf0f3e84b85138c8"),
    (W + "tests/W14 Plan - stage B, the instrument certified on the 96 reports by two blind Sonnet 5 markers.md",
     None, None, "plan W14, frozen, whole",
     "efcbc3b8b4f246eb906da8e32ade6568d4545a843ae62974719146efa3f540b0"),
    (W10, 37, 43, "plan W10, section 5",
     "f18449f4dc20d26f3a8e3b2bc5ffd2062066b079ee3b02327c9aeeee9f8b8690"),
    (MP, 1, 3, "the marking plan's head, which says which of two differing sections governs",
     "cb473a306dc5fc412cc796901ff76dd4c5e697f27c16b4a3b62500f44724ac70"),
    (MP, 187, 228, "the marking plan's sections 5 and 6",
     "c234b12513779f4c288c9cd978763739f20984a7c1d3c4c003817cf4a95a1131"),
    (MP, 305, 595, "the marking plan's three addenda, sections 13, 14 and 15, whole",
     "bc9e850c9ecc4a2e99a28efaca57cfbfdaf14b1d6edd8417daccab019ad34d8b"),
    (H + "instrument/criteria.json", None, None, "the criteria, version W10-A4-4, whole",
     "76650d901588aa82151a903d1b4496554d2f11b6d6b7ae6f52cb0e57a3162dc2"),
    (H + "marking/stage_b_record96.json", None, None,
     "the governing counts, written by stage_b.py run in place, whole",
     "da347b0f5826de43a376e3608e9cbb114c43c3161100ae8f0b05caf901479a75"),
    (H + "stage-B/independent-check/comparison.md", None, None,
     "the field-by-field comparison of the harness's programs with the independent recompute, whole",
     "f9861791135213e37b9434531c88b71526c36b31b4bc78c039c8a68bea8eeeeb"),
    (H + "stage-B/independent-check/README.md", None, None,
     "the independent recompute's read-me, whole",
     "9ed7659bc1dabe688bbd0301e99dc8acda402c30acffd9b08de25bb8a30d302d"),
]
BLOCKS = ["w16:system-head", "w16:system-tail", "w16:user-head",
          "w16:lens-L1", "w16:lens-L2", "w16:lens-L3", "w16:form"]
LENSES = ["L1", "L2", "L3"]
EXPECTED = {  # the sha256 of every message and message list the plan froze (section 2.4)
    "system": "96d204652e0d1e2a5b34d56307d2debd06064967b8fc2a37d537656b541e2749",
    "user-L1": "4c5c77b39184283186778b0cbb8b99be81f4a5b118da9a53ec18112791467118",
    "user-L2": "1287bb358935000ba1ab5a52b2b72df5432e74885f477461bffd5369709458c9",
    "user-L3": "e55de05efe34ff7269da7497b3355ddd3b7b3b3aa80741fa6bdfea024ebd7a55",
    "messages-L1": "e9d5d64215d663e92f5a2cf048bcae6e0f3b0ee32e954169660e910a9c60cb99",
    "messages-L2": "8351a46b76f0d1f15816dbb952b634fc6d9258b6e4840ef455bde0c4b0402e62",
    "messages-L3": "b25b88b1629e76d8a3157fdbaf881e08809db566bec518ee4bab872ba7641359",
}
KEY_ENV = ("DEEPSEEK_API_KEY", "ATRIA_API_KEY", "MIMO_API_KEY")


def refuse(why):
    sys.stderr.write(f"REFUSED: {why}. Nothing built, nothing written.\n")
    sys.exit(2)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blocks(plan_text):
    """Every fenced block whose opening fence is FENCE + 'w16:<name>', taken from the line after
    the opening fence to the line before the closing fence, exactly."""
    out, lines, i = {}, plan_text.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith(FENCE + "w16:"):
            name = lines[i][len(FENCE):].strip()
            j = i + 1
            while j < len(lines) and lines[j] != FENCE:
                j += 1
            if j == len(lines):
                refuse(f"the block {name} is not closed")
            if name in out:
                refuse(f"the block {name} appears twice")
            out[name] = "\n".join(lines[i + 1:j])
            i = j + 1
        else:
            i += 1
    if sorted(out) != sorted(BLOCKS):
        refuse(f"the plan's blocks are {sorted(out)}, not {sorted(BLOCKS)}")
    for name, text in out.items():
        if not text.strip() or FENCE in text:
            refuse(f"the block {name} is empty or carries a fence")
    return out


def read(repo, path):
    p = os.path.join(repo, path)
    if not os.path.isfile(p):
        refuse(f"{path} is not in the repository")
    return open(p, "rb").read()


def with_newline(text):
    return text if text.endswith("\n") else text + "\n"


def build(repo, plan_text):
    b = blocks(plan_text)
    parts = [b["w16:system-head"], "\n\n"]
    for rel, h in SKILL_FILES:
        data = read(repo, SKILL_DIR + rel)
        if sha(data) != h:
            refuse(f"{SKILL_DIR}{rel} is sha256 {sha(data)}, not {h}")
        parts.append(f"===== BEGIN FILE {SKILL_DIR}{rel} ({len(data)} bytes, sha256 {h}) =====\n")
        parts.append(with_newline(data.decode("utf-8")))
        parts.append(f"===== END FILE {SKILL_DIR}{rel} =====\n\n")
    parts.append(b["w16:system-tail"] + "\n")
    system = "".join(parts)
    docs, sources = [], []
    for n, (path, a, z, label, h) in enumerate(DOCS, 1):
        data = read(repo, path)
        where = ""
        if a is not None:
            if sha(data) != WHOLE[path]:
                refuse(f"{path} is sha256 {sha(data)}, not {WHOLE[path]}")
            lines = data.split(b"\n")
            total = len(lines) - 1 if data.endswith(b"\n") else len(lines)
            if not (1 <= a <= z <= total):
                refuse(f"lines {a} to {z} are not inside {path}'s {total}")
            data = b"".join(line + b"\n" for line in lines[a - 1:z])
            where = f", lines {a} to {z} of {total}"
        if sha(data) != h:
            refuse(f"document {n}, {path}{where}, is sha256 {sha(data)}, not {h}")
        docs.append(f"===== BEGIN DOCUMENT {n} of {len(DOCS)}: {path}{where}: {label} "
                    f"({len(data)} bytes, sha256 {h}) =====\n"
                    + with_newline(data.decode("utf-8"))
                    + f"===== END DOCUMENT {n} of {len(DOCS)} =====\n\n")
        sources.append({"n": n, "path": path, "lines": [a, z] if a is not None else None,
                        "bytes": len(data), "sha256": h})
    users = {L: b["w16:user-head"] + "\n\n" + "".join(docs) + b[f"w16:lens-{L}"] + "\n\n"
             + b["w16:form"] + "\n" for L in LENSES}
    messages = {L: [{"role": "system", "content": system},
                    {"role": "user", "content": users[L]}] for L in LENSES}
    return system, users, messages, sources


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        refuse("usage: build_w16.py PLAN [--out DIR]")
    plan = os.path.abspath(args[0])
    out = args[args.index("--out") + 1] if "--out" in args else None
    repo = os.path.dirname(os.path.dirname(os.path.dirname(plan)))
    system, users, messages, sources = build(repo, open(plan, encoding="utf-8").read())
    for name in KEY_ENV:
        v = os.environ.get(name, "")
        if len(v) >= 12 and (v in system or any(v in u for u in users.values())):
            refuse(f"a built message contains the value of {name}")
    got = {"system": sha(system.encode("utf-8"))}
    for L in LENSES:
        got[f"user-{L}"] = sha(users[L].encode("utf-8"))
        got[f"messages-{L}"] = sha(json.dumps(messages[L], ensure_ascii=False).encode("utf-8"))
    rows = [("system", system)] + [(f"user-{L}", users[L]) for L in LENSES]
    for k, text in rows:
        print(f"{k:12} {len(text):>9,} characters {len(text.encode('utf-8')):>9,} bytes  sha256 {got[k]}")
    for L in LENSES:
        m = json.dumps(messages[L], ensure_ascii=False)
        chars = len(system) + len(users[L])
        print(f"messages-{L:3} {len(m.encode('utf-8')):>9,} bytes as posted  sha256 {got[f'messages-{L}']}"
              f"  (system + user: {chars:,} characters; about {chars // 4:,} to {chars // 3:,} tokens"
              f" at four to three characters a token)")
    print("both families: the same message list per lens, by construction (one list per lens)")
    if EXPECTED:
        bad = [k for k in got if EXPECTED.get(k) != got[k]]
        if bad or sorted(EXPECTED) != sorted(got):
            refuse(f"built messages differ from the plan's frozen hashes: {bad or sorted(EXPECTED)}")
        print("every hash equals the one the plan froze")
    else:
        print("no frozen hashes in this copy: nothing compared")
    if out:
        os.makedirs(out, exist_ok=True)
        files = {"system.txt": system}
        for L in LENSES:
            files[f"user-{L}.txt"] = users[L]
            files[f"messages-{L}.json"] = json.dumps(messages[L], ensure_ascii=False)
        files["manifest.json"] = json.dumps({"plan": plan, "sources": sources, "sha256": got},
                                            ensure_ascii=False, indent=1) + "\n"
        for name, text in files.items():
            with open(os.path.join(out, name), "w", encoding="utf-8", newline="") as f:
                f.write(text)
        print(f"written: {len(files)} files to {out}")


if __name__ == "__main__":
    main()
