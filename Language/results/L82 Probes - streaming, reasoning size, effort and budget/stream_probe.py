import json, os, sys, time, urllib.request
key = os.environ["ATRIA_API_KEY"]; prompt = open(sys.argv[1]).read()
body = {"model": "Atria-Dawn-Preview", "messages": [{"role": "user", "content": prompt}], "max_tokens": 60000, "temperature": 0.2, "stream": True}
req = urllib.request.Request("https://api.atria-asi.ai/v1/chat/completions", data=json.dumps(body).encode(), method="POST", headers={"Authorization": "Bearer " + key, "Content-Type": "application/json", "Accept": "text/event-stream"})
t0 = time.time(); content = reasoning = ""; chunks = 0; last = None; fin = None
with urllib.request.urlopen(req, timeout=600) as r:
    for raw in r:
        line = raw.decode(errors="replace").strip()
        if not line.startswith("data:"): continue
        data = line[5:].strip()
        if data == "[DONE]": break
        try: d = json.loads(data)
        except Exception: continue
        chunks += 1; last = d
        for ch in d.get("choices") or []:
            delta = ch.get("delta") or {}; content += delta.get("content") or ""; reasoning += delta.get("reasoning_content") or ""
            if ch.get("finish_reason"): fin = ch["finish_reason"]
        if chunks % 500 == 0: print("t=%.0fs chunks=%d reasoning=%d content=%d" % (time.time() - t0, chunks, len(reasoning), len(content)), flush=True)
print("DONE t=%.0fs chunks=%d reasoning=%d content=%d finish=%s usage=%s" % (time.time() - t0, chunks, len(reasoning), len(content), fin, (last or {}).get("usage")), flush=True)
open(sys.argv[2], "w").write(content)
