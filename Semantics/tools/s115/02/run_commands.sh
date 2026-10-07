# NOTE (S115, added by Claude): Astra's two commands: make the files, then run the 5,000-update suite (6 runs, at most 3 Avida processes).
# Copied unchanged from GPT 6 Astra's reply 02 (tests/S115 Returns from GPT 6 Astra/02 Return - evaluation inside the program population.md); only these note lines were added.
python3 make_experiments.py
python3 stock_avida_evaluation/run_suite.py --avida /absolute/path/to/avida --output results_5000
