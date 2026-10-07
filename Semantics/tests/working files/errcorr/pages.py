import sys,re,glob
# usage: pages.py book start end
book,start,end=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
base='/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/sources/%s/text/'%book
txt=''
for f in sorted(glob.glob(base+'*.txt')):
    txt+=open(f,encoding='utf-8').read()+'\n'
parts=re.split(r'(\[p\.\d+\])',txt)
cur=None;out=[]
for p in parts:
    m=re.fullmatch(r'\[p\.(\d+)\]',p)
    if m: cur=int(m.group(1)); 
    if cur is not None and start<=cur<=end: out.append(p)
print(''.join(out))
