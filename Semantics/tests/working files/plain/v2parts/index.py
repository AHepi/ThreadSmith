import re,sys
doc=open('whole v2.md').read()
secs=re.split(r'\n## ',doc)
body={}
for s in secs:
    h=s.split('\n',1)[0]
    m=re.match(r'(\d+)\.',h)
    if m: body[int(m.group(1))]=s
    elif 'one page' in h: body[0]=s
use=[k for k in body if k<=14]
cases52=[
("The forecaster who keeps finding honest limits","narrowings after failures",[r"Bruno"]),
("The tide table with a real bell attached","the answer written in",[r"Carla"]),
("Nadia and the cards she has never seen","construction; \"her own\"",[r"Nadia"]),
("Greta's dough","a limit with a stated reason",[r"Greta"]),
("The fever and the thermometer","reading versus cause",[r"Hana",r"fever"]),
("Salt on the icy step","a coarse account",[r"[Ss]alt on the","Ines"]),
("The float that does two jobs","response patterns",[r"float"]),
("Two thermostats","values are not kinds",[r"thermostat"]),
("The apprentice and the third lock","selection, construction, reuse",[r"apprentice"]),
("The rota","a found question; merit unsettled",[r"Noor",r"rota"]),
("Two plumbers","three attributions; no created knowledge",[r"[Pp]lumbers"]),
("The phrasebook","a narrow lasting use",[r"Kofi",r"phrasebook"]),
("The worn key and the diary","no receipt from the claim itself",[r"worn key",r"diary"]),
("The robot's log and the maker's manual","owning rests on the log",[r"maker's manual"]),
("The one tooth","a small join",[r"one tooth"]),
("The diagram in his hand","no route ran",[r"diagram in his hand"]),
("Two valves in one second","both credited",[r"Two valves"]),
("The expert's question","\"mostly\", unsettled",[r"expert's question"]),
("\"The seal was tight\"","a slot added",[r"seal was tight"]),
("The unused joint setting","a problem inside the range",[r"joint setting"]),
("The test that fitted neither","blame shared; \"mostly\"",[r"fitted neither"]),
("The card nobody can read","history kept, access lost",[r"card nobody"]),
("The routine uploaded that morning","owning versus credit",[r"routine uploaded"]),
("The table with empty columns","a range is what is stated",[r"empty columns"]),
("Where the second compartment used to be","a supplied meaning",[r"second compartment"]),
("Four seconds","occasions not stated",[r"Four seconds"]),
("A premise both routes use","load-bearing as written",[r"premise both routes"]),
("The uncited textbook","no circles",[r"uncited textbook"]),
("Written on the job sheet","occasions stated",[r"job sheet"]),
("Two hands on the test","neither can say \"mostly\"",[r"Two hands"]),
("The technician's whisper","an outside contribution",[r"technician"]),
("New board, old memory","the sameness rule",[r"New board"]),
("Mirrored marks","a recoding",[r"Mirrored marks"]),
("Half from the source, half from the shelf","a patch's history",[r"Half from the source"]),
("The spring nobody mentioned","redundant supports",[r"spring nobody",r"two springs",r"second spring"]),
("The cable that used to be a spring","a different candidate",[r"[Cc]able"]),
("One more commitment","interference",[r"One more commitment",r"room was locked"]),
("The forbidden wire","file 10's proof defeated",[r"forbidden wire"]),
("Owned means capable","a circular definition",[r"Owned means capable"]),
("The same afternoon, three achievements","\"mostly\", unsettled",[r"same afternoon"]),
("The module in the casing","the boundary decides",[r"module in the casing"]),
("The route that started and was stopped","a route that did no work",[r"started and was stopped"]),
]
proposed=[
("The seasons and the sun god","idle, or not",[r"sun god",r"Tomas"]),
("A myth about winter","a candidate, not an account",[r"myth about winter",r"the myth\b"]),
("The tilt and the midnight sun","standing fixed by idea, question and world",[r"midnight sun"]),
("A farmer's rule carried south","a problem outside the range",[r"farmer",r"village rule"]),
("Two bakers","honest limits; not rivals",[r"Two bakers",r"Maya"]),
("The machine that runs forever","a blocking question",[r"runs forever",r"Quentin",r"Pia"]),
("Dark moths","selection; a picture",[r"moths"]),
("Two students, ten drafts each","criticisms and warning signs",[r"Kasia",r"Jana"]),
("The parrot in the lecture hall","relay",[r"parrot"]),
("The domino that never falls","an assumed answer",[r"domino"]),
("Two footbridges on opening day","miss and surprise",[r"footbridge",r"Dov"]),
("The novelist's two demands","a noticed difficulty",[r"Odile",r"novelist"]),
("Keeping count with string","error build-up",[r"goatherd",r"string"]),
("The order of adjectives","an unspoken picture",[r"Ngozi",r"adjectives"]),
("Denying the inner experience","a bare denial",[r"Wren",r"Yuri",r"inner experience"]),
("The planets tonight and a thousand years ago","a calculation run backwards",[r"Priya",r"planets"]),
("Two sealed sorts of matter","a barrier",[r"sealed sorts",r"Bram",r"Asha"]),
("What holds the universe up","not rivals",[r"universe up",r"turtle"]),
("The discarded lamp controller","what survival leaves open",[r"lamp controller",r"Ivo"]),
]
theory=[
("The pole and its shadow",[r"\bpole\b"]),
("Two balances",[r"balance"]),
("Twenty-three tokens",[r"tokens"]),
("Odd-sized tables",[r"[Oo]dd-sized tables",r"tables example"]),
("Spread-out support",[r"[Ss]pread-out support"]),
("Parallel and priority wiring",[r"priority wiring"]),
("The hidden thing",[r"hidden thing"]),
]
def where(keys):
    res=[]
    for k in sorted(use):
        if any(re.search(p,body[k]) for p in keys):
            res.append(k)
    return res
def fmt(r):
    names=[('one page' if x==0 else str(x)) for x in r]
    if not names: return 'NONE'
    if len(names)==1: return ('Section ' if names[0]!='one page' else 'The ')+names[0]+'.'
    return 'Sections '+', '.join(names)+'.' if names[0]!='one page' else 'One page; sections '+', '.join(names[1:])+'.'
out=[]
out.append(f"**Cases from the book of 52 used here ({len(cases52)})**\n")
for t,d,k in cases52:
    out.append(f"- {t}: {d}. {fmt(where(k))}")
out.append(f"\n**Proposed cases used here ({len(proposed)}: {len(proposed)-1} from the book of 25, and the lamp controller)**\n")
for t,d,k in proposed:
    out.append(f"- {t}: {d}. {fmt(where(k))}")
out.append("\n**The theory's own examples**\n")
for t,k in theory:
    out.append(f"- {t}. {fmt(where(k))}")
print('\n'.join(out))
