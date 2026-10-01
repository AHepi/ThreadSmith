git clone https://github.com/devosoft/avida.git av_src
git -C av_src checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git -C av_src submodule update --init libs/apto libs/backward-cpp
git clone av_src av_patch
git -C av_patch submodule update --init libs/apto libs/backward-cpp
git -C av_patch apply --check ../work/anticipation.patch
git -C av_patch apply ../work/anticipation.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S av_src -B build-stock -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS='-std=gnu++11'
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-stock --target avida -j4
AVIDA_DISABLE_BACKTRACE=1 cmake -S av_patch -B build-patched -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS='-std=gnu++11'
AVIDA_DISABLE_BACKTRACE=1 cmake --build build-patched --target avida -j4
python3 work/setup_tests.py
python3 work/build_test.py
(cd tests && ./check)
