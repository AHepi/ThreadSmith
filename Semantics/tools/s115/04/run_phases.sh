# NOTE (added by Claude, 30 September 2026, log S115): the phase commands from
# GPT 6 Astra's reply 04, copied unchanged below. "/absolute/path/to/avida" is the
# reply's placeholder for the stock Avida 2.14.0 binary. The prepared commands for
# this machine are in the check file, section 4.
python3 make_runs.py brief04_runs
python3 make_runs.py --assay brief04_runs /absolute/path/to/avida
python3 make_runs.py --run brief04_runs /absolute/path/to/avida
python3 make_runs.py --snapshots brief04_runs /absolute/path/to/avida
