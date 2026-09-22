#!/bin/sh
# Put s(CASP) where the two drivers expect it (Lesson 53). Tested 21 September 2026
# on Ubuntu 24.04: SWI-Prolog 9.0.4 from apt, s(CASP) 1.1.4 from its makers' repository.
set -e
apt-get update -q && apt-get install -y -q swi-prolog
rm -rf /tmp/sCASP && git clone -q --depth 1 https://github.com/SWI-Prolog/sCASP.git /tmp/sCASP
cd /tmp/sCASP
# The Makefile's last step ("swipl qlf ...") fails on SWI-Prolog 9.0.4. The scasp
# executable is already built by then, so the failure is ignored on purpose.
make > /tmp/scasp_make.log 2>&1 || true
test -x /tmp/sCASP/scasp || { echo "scasp was not built; see /tmp/scasp_make.log"; exit 1; }
mkdir -p /home/claude/sCASP && ln -sf /tmp/sCASP/scasp /home/claude/sCASP/scasp
/home/claude/sCASP/scasp --version
echo "Now the smoke test, from the folder 'rigs/rig 1 - arguments':"
echo "  python3 patched/run_check.py ledger_A.pl /tmp/raw_log_smoke.txt"
echo "Expected: the report in tools/smoke_expected_report_A.txt (a contradiction about the plant by the door, a BECAUSE that follows)."
echo "Older bundles used ledger_T05B.pl and tools/smoke_expected_report_T05B.txt instead; either is a valid smoke test where its ledger is present."
