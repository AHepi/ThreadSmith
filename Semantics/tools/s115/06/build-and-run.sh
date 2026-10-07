# NOTE (S115, added by Claude): Astra's build and run commands for the four miniature designs. Run only in a COPY of the Avida source.
# Copied unchanged from GPT 6 Astra's reply 06 (tests/S115 Returns from GPT 6 Astra/06 Return - independent review of the first reply.md); only these note lines were added.
git -C avida submodule update --init libs/apto
git -C avida apply ../mini-all.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S avida -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5
AVIDA_DISABLE_BACKTRACE=1 cmake --build build --target avida -j 3
python3 setup.py avida small-runs
python3 smoke.py build/bin/avida small-runs small-smoke
(cd small-runs/B2 && ../../build/bin/avida -c avida.cfg)
