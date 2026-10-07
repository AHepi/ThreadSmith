SRC=/workspace/scratch/4213a51f9bba/av_src
BASE=/workspace/scratch/fbaa94d665d5
CMAKE=/root/.local/lib/python3.12/site-packages/cmake/data/bin/cmake
AVIDA_DISABLE_BACKTRACE=1 "$CMAKE" -S "$SRC" -B "$BASE/build" \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_FLAGS=-std=gnu++11 -DAVD_GUI_NCURSES=OFF \
  -DAVD_GUI_PROTOTYPE_TEXT=OFF -DAVD_UNIT_TESTS=OFF -DAPTO_UNIT_TESTS=OFF
AVIDA_DISABLE_BACKTRACE=1 "$CMAKE" --build "$BASE/build" --target avida -j 3
