import re,glob,sys
base='/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/sources/%s/text/'
def load(book):
    raw=''
    for f in sorted(glob.glob(base%book+'*.txt')):
        if 'Index' in f: continue
        raw+=open(f,encoding='utf-8').read()+'\n'
    out=[];pages=[];cur=0
    for m in re.finditer(r'\[p\.(\d+)\]|\s+|[^\s\[]+|\[',raw):
        tok=m.group(0)
        if m.group(1): cur=int(m.group(1)); continue
        if tok.isspace():
            if out and out[-1]!=' ': out.append(' '); pages.append(cur)
            continue
        for ch in tok: out.append(ch); pages.append(cur)
    t=''.join(out)
    return t,t.lower(),pages
books={'D':load('deutsch'),'M':load('marletto')}
doc=open(sys.argv[1],encoding='utf-8').read()
def norm(s):
    return s.replace("'", "’")
nq=0;bad=0
for ln,line in enumerate(doc.split('\n'),1):
    cites=[]
    for m in re.finditer(r'\b(D|M)\s+pp?\.\s?(\d+)(?:[–-](\d+))?',line):
        lo=int(m.group(2)); hi=int(m.group(3)) if m.group(3) else lo
        cites.append((m.group(1),lo,hi))
    # also bare p.N after a D/M context, e.g. "(p.24)"
    for m in re.finditer(r'\(pp?\.(\d+)(?:[–-](\d+))?',line):
        lo=int(m.group(1)); hi=int(m.group(2)) if m.group(2) else lo
        cites.append(('?',lo,hi))
    for m in re.finditer(r'"([^"]{12,})"',line):
        q=m.group(1)
        # strip outer single quotes marks
        parts=[re.sub(r'\s+',' ',x.strip()) for x in q.split('…') if x.strip()]
        words=len([w for w in re.split(r'\s+',q.replace('…',' ')) if re.search(r'\w',w)])
        res={}
        for b,(t,tl,pg) in books.items():
            locs=[];ok=True;ci=False
            for part in parts:
                i=t.find(part)
                if i<0: i=t.find(norm(part))
                if i<0:
                    i=tl.find(part.lower())
                    if i>=0: ci=True
                if i<0: ok=False;break
                locs.append(pg[i]); locs.append(pg[i+len(part)-1])
            if ok: res[b]=(sorted(set(locs)),ci)
        if not res: continue  # not a book quote (theory text etc.)
        nq+=1
        okcite=False
        for b,(pgs,ci) in res.items():
            for (cb,lo,hi) in cites:
                if cb in (b,'?') and all(lo<=p<=hi for p in pgs): okcite=True
        flag=[]
        if not okcite: flag.append('CITE? cites=%s found=%s'%(cites,{k:v[0] for k,v in res.items()}))
        if any(v[1] for v in res.values()): flag.append('CASE-DIFF')
        if words>25: flag.append('TOOLONG %d'%words)
        if flag:
            bad+=1; print('L%d'%ln,'|',q[:90],'|',' ; '.join(flag))
print('book quotes checked',nq,'flagged',bad)
