# NOTE (S115, added by Claude): Astra's command to run the test (section 5).
# Copied unchanged from GPT 6 Astra's reply 07 (tests/S115 Returns from GPT 6 Astra/07 Return - a bounded test runner patch.md); only these note lines were added.
cd bounded-test
../build-bounded/bin/avida -a -c avida.cfg \
  -set RANDOM_SEED 1 -set ANALYZE_FILE analyze.cfg
