from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json, hashlib, argparse
from read_books import call_model, ROOT

def verify(question):
    pages = json.loads((ROOT/'source'/f"{question['slug']}.json").read_text())
    selected = [p for p in pages if p['file_page'] in question['pages']]
    text = '\n\n'.join(f"[File page {p['file_page']}]\n{p['text']}" for p in selected)
    if len(text)>29000: raise ValueError('Verification source exceeds the bounded reading size')
    prompt = f'''You are rereading ORIGINAL passages to verify claims for a theory of how to build a thinking machine. The user specifically requires MiMo to read every book reference and know why. Our proposal concerns executable grounded representations, constrained learning and generalization, temporal memory, compositional reasoning, active observations, goal selection and revisable models. This is an engineering theory, not a claim of demonstrated consciousness or a completed general intelligence algorithm.

Book: {question['book']}. Supplied ordinal file pages: {question['pages']}. Only attribute claims to these pages when directly supported. Do not rely on memory of this book or any earlier summary. Do not invent printed page numbers. If a claim is absent, overstrong, conflates domains or is the designer's extension, say so. Historical criticisms of particular neural networks must not be recast as limits on all neural implementations; language-learning results do not automatically establish general learning laws.

Questions to verify:
{question['question']}

Return a concise verdict for each substantive claim, its file-page location, necessary qualification and a faithful paraphrase. Then explain how far the source supports the proposed engineering use and what remains to be invented. Use full names and ordinary prose without abbreviations, mathematical functions or numbered lists. Maximum 800 words.

ORIGINAL SOURCE TEXT:
{text}'''
    out=ROOT/'verification'/f"{question['name']}.json"
    (ROOT/'verification').mkdir(exist_ok=True)
    (ROOT/'verification'/f"{question['name']}_provenance.json").write_text(json.dumps({'book':question['book'],'file_pages':question['pages'],'source_characters':len(text),'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'question':question['question']},indent=2))
    r=call_model(prompt,out,2400)
    return {'name':question['name'],'finish_reason':r['finish_reason'],'usage':r['usage']}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-workers',type=int,choices=[1,2,3],default=3)
    args=parser.parse_args()
    questions=json.loads((ROOT/'verification_questions.json').read_text())
    with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        for r in pool.map(verify,questions): print(json.dumps(r),flush=True)
