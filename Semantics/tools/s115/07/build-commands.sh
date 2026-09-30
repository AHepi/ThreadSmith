# NOTE (S115, added by Claude): Astra's build commands (section 5). Run by hand, in a COPY of the Avida source, never in the stock build.
# Copied unchanged from GPT 6 Astra's reply 07 (tests/S115 Returns from GPT 6 Astra/07 Return - a bounded test runner patch.md); only these note lines were added.
git checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git submodule update --init libs/apto
git apply --check bounded-runner.patch
git apply bounded-runner.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S . -B build-bounded \
  -DAVD_CMDLINE=ON -DAVD_GUI_NCURSES=OFF -DAVD_UNIT_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=11
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-bounded --target avida -j 1
mkdir -p bounded-test
cp avida-core/support/config/{avida.cfg,instset-heads.cfg,default-heads.org,environment.cfg,events.cfg} bounded-test/
