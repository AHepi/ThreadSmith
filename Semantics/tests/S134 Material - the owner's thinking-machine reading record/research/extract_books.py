"""Recreate page-labelled text and small reading chunks from the original books."""
from pathlib import Path
from pypdf import PdfReader
import argparse, json, hashlib

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('input_directory',type=Path)
    args=parser.parse_args()
    root=Path(__file__).parent
    (root/'source').mkdir(exist_ok=True)
    (root/'chunks').mkdir(exist_ok=True)
    books=[]
    for name,slug in [('How the Mind Works','how_the_mind_works'),('Learnability and Cognition','learnability_and_cognition')]:
        paths=list(args.input_directory.glob(name+'*.pdf'))
        if len(paths)!=1: raise RuntimeError(f'Expected one original file for {name}; found {len(paths)}')
        path=paths[0]
        pages=[{'file_page':i+1,'text':page.extract_text() or ''} for i,page in enumerate(PdfReader(path).pages)]
        (root/'source'/f'{slug}.json').write_text(json.dumps(pages,ensure_ascii=False))
        chunks=[];buffer='';start=1;end=1
        for page in pages:
            text=f'\n[File page {page["file_page"]}]\n'+page['text']
            if buffer and len(buffer)+len(text)>26000:
                chunks.append({'book':name,'slug':slug,'first_page':start,'last_page':end,'text':buffer});buffer=''
            if not buffer:start=page['file_page']
            buffer+=text;end=page['file_page']
        if buffer:chunks.append({'book':name,'slug':slug,'first_page':start,'last_page':end,'text':buffer})
        for i,chunk in enumerate(chunks):
            chunk['chunk_number']=i+1
            (root/'chunks'/f'{slug}_{i+1:03}.json').write_text(json.dumps(chunk,ensure_ascii=False))
        books.append({'book':name,'slug':slug,'pages':len(pages),'characters':sum(len(p['text']) for p in pages),'chunks':len(chunks),'empty_pages':[p['file_page'] for p in pages if len(p['text'].strip())<30],'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (root/'manifest.json').write_text(json.dumps(books,indent=2))
    print(json.dumps(books,indent=2))

if __name__=='__main__':main()
