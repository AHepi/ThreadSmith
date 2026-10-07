git clone https://github.com/devosoft/avida.git /workspace/scratch/e7208be14540/avida-source
git checkout 47f13dad
git rev-parse HEAD
git submodule update --init libs/apto libs/backward-cpp
python -m cmake -S . -B cbuild -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_BUILD_TYPE=Release
python -m cmake --build cbuild --target avida -j 3 > cbuild/build.log 2>&1
./cbuild/bin/avida -v
