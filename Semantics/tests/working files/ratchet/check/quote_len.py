import re, sys
for fn in sys.argv[1:]:
    for n, line in enumerate(open(fn, encoding='utf-8'), 1):
        if not re.search(r'\b(D|M) ?p\.|Deutsch|Marletto|p\.\d', line):
            continue
        for q in re.findall(r'["“]([^"”]{3,}?)["”]', line):
            w = len(q.split())
            if w > 20:
                print('%s:%d  %d words: %s' % (fn, n, w, q[:120]))
