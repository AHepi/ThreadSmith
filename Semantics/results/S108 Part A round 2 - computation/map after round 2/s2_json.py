"""Section 2's edge .json (rule 5), written from the tables of its "variants computed" file (§8, §11), which the stopped
section-2 agent completed; after S56 the one Opus agent writes the .json from them, adding nothing."""
import json, re, sys
from mdtable import tables_under
SEM = "/home/user/ThreadSmith/Semantics/results/"
md = SEM + "S108 Part A round 2 - section 2 - variants computed.md"


def std(s):
    s = s.replace("*", "").strip()
    if s.startswith("computed"):
        return "computed"
    if s.startswith("contradicted"):
        return "contradicted"
    if s.startswith("not settled") or s.startswith("noted"):
        return "not settled by computation"
    raise SystemExit("standing? " + s)


edges = []
for r in tables_under(md, "11."):
    item = r["item [mark]"]
    mark = re.findall(r"\[([^\]]+)\]", item)
    edges.append(dict(id=r["id"], variant=r["variant"], kind=r["kind"], item=item, mark=", ".join(mark),
                      named_by="the reply" if r["id"].startswith("R2E") else "the computing agent (added)",
                      standing=std(r["standing"]), standing_as_written=r["standing"],
                      evidence=r["what shows it / what would settle it"], round1_edge=""))
for r in tables_under(md, "8."):
    rid = r["edge"].split()[0]
    edges.append(dict(id="settles " + rid, variant=r["edge"].split()[1] if len(r["edge"].split()) > 1 else "",
                      kind="settlement of round 1's claimed-only edge", item=r["edge"], mark="",
                      named_by="round 1's map (claimed only)", standing=std(r["standing"]),
                      standing_as_written=r["standing"].replace("*", ""), evidence=r["what shows it"],
                      settlement=r["settlement computed"], round1_edge=rid))
out = {"about": "S108 Part A round 2, section 2: the edges of the round-2 variants (the reply's rows and two added) and the "
                "settlements of round 1's claimed-only edges of the share, as computed (rule 5). Written from §8 and §11 of "
                "the variants-computed file after S56 by the one Opus agent; nothing added to the stopped agent's findings.",
       "file": "S108 Part A round 2 - section 2 - variants computed.md", "status": "complete except the whole-suite runs "
       "(see the file's §6 and the addendum)", "edges": edges,
       "counts": {k: sum(1 for e in edges if e["standing"] == k) for k in ("computed", "contradicted", "not settled by computation")}}
json.dump(out, open(SEM + "S108 Part A round 2 - section 2 - variants computed.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(out["counts"], len(edges))
