# S111 build notes, and Avida's rules as read from its source

*Log S111. Written 29 September 2026 by the one Opus 5.5 agent of log S111. The Avida source and binary stay in the scratch space and are not in the repository; the lines below point into the source at commit 47f13dad (paths under `avida-core/`), so that a reader without the source can see which of Avida's rules the measures lean on. Short excerpts only.*

## The build

- Source: `github.com/devosoft/avida` at commit 47f13dad ("Merge pull request #95 from mmore500/whole-genome-duplication"), shallow clone; submodule `libs/apto` at its pinned commit 02e18980071d237f1ea4641f3f35cae469e2ed38, fetched with `git submodule update --init --depth 1 libs/apto`. `libs/backward-cpp` and `documentation` not fetched (not needed).
- Commands, in `avida/cbuild/`: `AVIDA_DISABLE_BACKTRACE=1 timeout 300 cmake -DCMAKE_BUILD_TYPE=Release ../` then `timeout 1800 nice make -j 3`. Both exited 0 (about 3 minutes). g++ 13.3.0, cmake 3.28.3, Ubuntu 24.04.
- **No patch and no extra compiler flag.** 285 compiler warnings (mostly the deprecated `std::binary_function`), no error. The only setting: the environment variable `AVIDA_DISABLE_BACKTRACE=1`, which Avida's own `build_avida` script uses as its fallback; it leaves out the backtrace library.
- Result: `cbuild/bin/avida`, "Avida 2.14.0, release build".
- One timing run before the plan was written: the default ancestor, seed 1, default settings, 3,000 updates in 104 seconds, 3,594 organisms at the end. Used only to choose run lengths.
- The analysis scripts use Python 3 and `numpy` (installed with `pip` for the alignment in `tools/s111_measure_the_worlds_over_time.py`).

## Avida's rules the measures lean on

| rule | where in the source | what it says |
|---|---|---|
| A copy error is made by the world, at the moment of copying one instruction | `source/cpu/cHardwareCPU.cc` 7139-7146, `Inst_HeadCopy` | `if (m_organism->TestCopyMut(ctx) ...) { read_inst = m_inst_set->GetRandomInst(ctx); ...}`: with the copy error probability, the instruction written is a random one from the set (which can be the same instruction). The organism's instruction asks for a copy; the error is the world's. |
| The random instruction is drawn from the whole set, evenly | `source/cpu/cInstSet.cc` 83-88 | a weighted draw over the set; all weights are equal in the default set. |
| Death by age | `source/main/cOrganism.cc` 223-231 | with `DEATH_METHOD 2` (the default), an organism may execute at most `AGE_LIMIT` (20) times its genome length in instructions, then it is removed. With `DEATH_METHOD 0` (control K3, K4) nothing dies of age. |
| Where an offspring goes | `avida.cfg`: `BIRTH_METHOD 0`, `PREFER_EMPTY 1` | a random cell next to the parent, an empty one first; otherwise whoever is there is replaced. |
| Processor time | `avida.cfg`: `BASE_MERIT_METHOD 4`; `environment.cfg` | merit is proportional to the smaller of the executed and the copied length, multiplied by 2^(task value) for each task performed (`type=pow`); the scheduler hands out instructions in proportion to merit. |
| "Viable" in the test processor | `source/cpu/cTestCPU.cc` 282-313 | a program is viable if, run alone, it divides and its offspring is identical to it ("copied true"), or its offspring's line cycles back to it. No mutations are applied there. |
| `if-label` | `source/cpu/cHardwareCPU.cc` 6914-6920 | reads the label after it and executes the next instruction only if the last instructions copied are its complement: how the copy loop finds the end. It compares, but only to stop; no instruction of the default set repairs a copied instruction. |
| `nop-X` | `source/cpu/cHardwareCPU.cc` 89 (`"True no-operation instruction: does nothing"`, flags 0: no NOP flag) | added as a 27th instruction only for the analysis runs and the control worlds; it does nothing and is not read as part of a label. |
| `SAMPLE_OFFSPRING` | `source/analyze/cAnalyze.cc` 1604-1690 | in the test processor, with the world's mutation rates copied in (`test_info.MutationRates().Copy(...GetMutRates())`), one gestation per sample; the offspring genomes are counted. |
| `num_breed_true` in `count.dat` | `source/main/cStats.cc` 1099 | the births in the update whose offspring is identical to its parent. |
