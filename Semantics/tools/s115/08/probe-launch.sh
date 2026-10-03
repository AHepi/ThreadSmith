# NOTE (S115, added by Claude): Astra's launch command for the probe process.
# Copied unchanged from GPT 6 Astra's reply 08 (tests/S115 Returns from GPT 6 Astra/08 Return - a growing supply of problems, using only stock Avida.md); only these note lines were added.
avida -c avida.cfg -a \
  -set ENVIRONMENT_FILE probe-environment.cfg \
  -set ANALYZE_FILE probe-analyze.cfg \
  -set DATA_DIR probe-results
