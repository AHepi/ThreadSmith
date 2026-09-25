import re,glob,sys
base='/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/sources/%s/text/'
def load(book):
    raw=''
    for f in sorted(glob.glob(base%book+'*.txt')):
        if 'Index' in f: continue
        raw+=open(f,encoding='utf-8').read()+'\n'
    # build normalized text with page map
    out=[];pages=[];cur=0
    pos=0
    for m in re.finditer(r'\[p\.(\d+)\]|\s+|[^\s\[]+|\[',raw):
        tok=m.group(0)
        if m.group(1): cur=int(m.group(1)); continue
        if tok.isspace():
            if out and out[-1]!=' ': out.append(' '); pages.append(cur)
            continue
        for ch in tok: out.append(ch); pages.append(cur)
    return ''.join(out),pages
books={'D':load('deutsch'),'M':load('marletto')}
doc=open(sys.argv[1],encoding='utf-8').read()
bad=0
for m in re.finditer(r'"([^"]+)"(\s*\((D|M) pp?\.(\d+)(?:–(\d+))?\))?',doc):
    q=m.group(1); cite=m.group(3); p1=m.group(4); p2=m.group(5)
    parts=[re.sub(r'\s+',' ',x.strip()) for x in q.split('…') if x.strip()]
    words=len([w for w in re.split(r'\s+',q.replace('…',' ')) if re.search(r'\w',w)])
    found={}
    for b,(t,pg) in books.items():
        locs=[]
        ok=True
        for part in parts:
            i=t.find(part)
            if i<0: ok=False;break
            locs.append((pg[i],pg[i+len(part)-1]))
        if ok: found[b]=locs
    status='OK'
    if not found: status='NOTFOUND'
    elif cite:
        if cite not in found: status='WRONGBOOK'
        else:
            lo=int(p1); hi=int(p2) if p2 else lo
            pgs=set()
            for a,c in found[cite]: pgs.add(a); pgs.add(c)
            if not all(lo<=x<=hi for x in pgs): status='PAGE? found %s'%sorted(pgs)
    if words>25: status+=' TOOLONG(%d)'%words
    if status!='OK' or not cite:
        print(status,'|',words,'|',(cite or '-'),p1,p2,'|',q[:110], '|', {k:v[:2] for k,v in found.items()})
    if status.startswith(('NOTFOUND','WRONG','PAGE')) or 'TOOLONG' in status: bad+=1
print('flagged',bad)
