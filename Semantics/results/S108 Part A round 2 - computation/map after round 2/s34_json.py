"""Sections 3 and 4: the edge .json (rule 5), written from the tables of each "variants computed" file (the edges, and
the settlements of round 1's claimed-only edges) by the one Opus agent (S56); nothing added to the files' findings."""
import json, re
from mdtable import tables_under
SEM = "/home/user/ThreadSmith/Semantics/results/"


def std(s):
    s = s.replace("*", "").strip()
    for k, v in (("computed", "computed"), ("contradicted", "contradicted"), ("not settled", "not settled by computation"),
                 ("noted", "not settled by computation"), ("independent", "computed"), ("as e4.40", "computed")):
        if s.startswith(k):
            return v
    raise SystemExit("standing? " + s)


for n, edge_h, settle_h in ((3, "8.", "7."), (4, "7.", "6.")):
    md = SEM + "S108 Part A round 2 - section %d - variants computed.md" % n
    edges = []
    for r in tables_under(md, edge_h):
        item = r["item [mark]"]
        edges.append(dict(id=r["id"], variant=r["variant"], kind=r["kind"], item=item,
                          mark=", ".join(re.findall(r"\[([^\]]+)\]", item)),
                          named_by="the reply" if not r["id"].startswith("N") else "the computing agent (added)",
                          standing=std(r["standing"]), standing_as_written=r["standing"].replace("*", ""),
                          evidence=r["what shows it / what would settle it"], round1_edge=""))
    for r in tables_under(md, settle_h):
        rid = r["edge"].split()[0]
        edges.append(dict(id="settles " + rid, variant=r["edge"].split()[1], kind="settlement of round 1's claimed-only edge",
                          item=r["edge"], mark="", named_by="round 1's map (claimed only)", standing=std(r["standing"]),
                          standing_as_written=r["standing"].replace("*", ""), evidence=r["what shows it"],
                          settlement=r["settlement computed"], round1_edge=rid))
    out = {"about": "S108 Part A round 2, section %d: the edges of the round-2 variants and the settlements of round 1's "
                    "claimed-only edges of the share, as computed (rule 5), from the file's tables." % n,
           "file": "S108 Part A round 2 - section %d - variants computed.md" % n, "status": "complete", "edges": edges,
           "counts": {k: sum(1 for e in edges if e["standing"] == k) for k in ("computed", "contradicted", "not settled by computation")}}
    json.dump(out, open(SEM + "S108 Part A round 2 - section %d - variants computed.json" % n, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(n, out["counts"], len(edges))
