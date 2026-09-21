"""Pull the 25 cases out of file 43 into two files kept apart:
passages.json (what the reader is sent) and keys.json (never sent)."""
import re, json, sys
src = sys.argv[1]
t = open(src, encoding="utf-8").read()
pat = re.compile(r"\*\*(C?\d+)\. (.+?)\*\*\n\*Passage:\* (.+?)\n\*Key:\* (.+?)\n", re.S)
passages, keys = [], []
for m in pat.finditer(t):
    cid, head, passage, key = m.groups()
    bits = [b.strip() for b in head.split(". ")]
    name = bits[0]; domain = bits[1] if len(bits) > 1 else ""; role = ". ".join(bits[2:]).rstrip(".")
    passages.append({"id": cid, "name": name, "passage": passage.strip()})
    keys.append({"id": cid, "name": name, "domain": domain, "role": role, "key": key.strip(),
                 "kind": "control" if cid.startswith("C") else "contested"})
assert len(passages) == 25, len(passages)
json.dump(passages, open("passages.json", "w"), indent=1, ensure_ascii=False)
json.dump(keys, open("keys.json", "w"), indent=1, ensure_ascii=False)
print(len(passages), "cases;", sum(k["kind"]=="control" for k in keys), "controls")
for k in keys: print(k["id"], "|", k["name"], "|", k["role"])
