# NOTE (S115, added by Claude): Astra's launch command for one evolution run (set SEED first).
# Copied unchanged from GPT 6 Astra's reply 08 (tests/S115 Returns from GPT 6 Astra/08 Return - a growing supply of problems, using only stock Avida.md); only these note lines were added.
: "${SEED:?Set SEED to the matched original run seed}"
avida -c avida.cfg -set RANDOM_SEED "$SEED"
