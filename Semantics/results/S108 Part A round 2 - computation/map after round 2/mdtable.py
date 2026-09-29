"""Read the markdown tables of a file under a heading: a list of rows (dicts keyed by the header cells)."""
import re


def tables_under(path, heading_prefix):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, on, hdr = [], False, None
    for l in lines:
        if l.startswith("#"):
            on = l.lstrip("#").strip().startswith(heading_prefix)
            hdr = None
            continue
        if not on:
            continue
        if l.startswith("|"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", l.strip())[1:-1]]
            if hdr is None:
                hdr = cells
            elif set(l.replace("|", "").strip()) <= set("-: "):
                continue
            else:
                out.append(dict(zip(hdr, cells)))
        else:
            hdr = None if l.strip() == "" else hdr
    return out
