(cd run-stock && ../build-stock/bin/avida -s 119 -set SPECULATIVE 0 > ../stock-run-final.log 2>&1)
(cd run-off && ../build-patched/bin/avida -s 119 -set SPECULATIVE 0 -set ANTICIPATE_MODE -1 > ../off-run-final.log 2>&1)
python3 work/compare.py
