git clone https://github.com/devosoft/avida.git avida
git -C avida checkout --detach 47f13dadb547fcf10f620ace60247f38b30b8b16
git -C avida submodule update --init libs/apto libs/backward-cpp
git clone avida av_patch
git -C av_patch submodule update --init libs/apto libs/backward-cpp
git -C av_patch apply --check ../history/full.patch
git -C av_patch apply ../history/full.patch
ln -s avida av_src
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake -S avida -B build-stock -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS=-std=gnu++11
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake --build build-stock --target avida -j4
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake -S av_patch -B build-patched -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_CXX_FLAGS=-std=gnu++11
AVIDA_DISABLE_BACKTRACE=1 python3 -m cmake --build build-patched --target avida -j4
python3 work/setup_tests.py
python3 history/setup.py
python3 history/build.py
(cd history/tests && ./check)
python3 work/build_test.py
(cd tests && ./check)
