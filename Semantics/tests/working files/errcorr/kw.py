import sys,re,glob
book=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); width=int(sys.argv[3]) if len(sys.argv)>3 else 200
base='/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/sources/%s/text/'%book
for f in sorted(glob.glob(base+'*.txt')):
    if 'Index' in f: continue
    t=open(f,encoding='utf-8').read()
    for m in pat.finditer(t):
        pre=t[:m.start()]
        pages=re.findall(r'\[p\.(\d+)\]',pre)
        pg=pages[-1] if pages else '?'
        s=max(0,m.start()-width); e=min(len(t),m.end()+width)
        print('p.%s | %s | %s'%(pg,f.split('/')[-1][:25],t[s:e].replace('\n',' ')))
        print('---')
