# Where each file came from (reply 01, log S122)

*Written by `tools/s122_extract_the_code_blocks_of_the_replies.py`. Every file in this folder is one fenced code block of GPT 6 Astra's reply `tests/S121 Returns from GPT 6 Astra/01 Return - the execution environment as a temporal, neuron-like selector.md`, copied unchanged: the lines between the fences, then one newline. Nothing was added inside any file. Line numbers are those of the reply's content lines. Files named `block-NN ...` had no name in the reply; the others keep the path the reply gives them (its section "Files to save"). Run the script with `--check` to confirm byte for byte. The reply's own SHA-256 list (block 28) is compared with these files in the check of reply 01.*

| File | Reply lines | Fence label | SHA-256 |
|---|---|---|---|
| `block-01 build commands.sh` | 151-157 | bash | 9723e802a93a4cd0fe1c182f849e00c882b0548b7892f1ec210fa85abb4ff60d |
| `block-02 reported selected build output.txt` | 163-175 | text | 3dfdf3fca67016b25a94958dc6654071fcc3464b87c9c2b9dd779d155795e97c |
| `block-03 initial tiny run command.sh` | 181-181 | bash | 791488088da23fb5fc37f7c73dc9a52fe3204e091c25d4ed709284ba5c4adae1 |
| `block-04 final frozen tiny run command.sh` | 187-187 | bash | d2d327a9d87b96ab876332a7a972b9f37ba8d7720e0366c2d29b7c6495f739c6 |
| `block-05 reported output of both full runs.txt` | 193-194 | text | bde23400cfe23b99aedafeeddd191a27191b8a75c51fd3998740e6d10734cd15 |
| `block-06 replay command.sh` | 200-200 | bash | 625099df6a4c2c68822356fd6d11bb909740060ee2cadaafe1bd0e32018b677a |
| `block-07 reported replay output.txt` | 206-207 | text | eedf42005b3e3453c8f44ec7ae426449ceaecacba936825a6837faa2721a2d2a |
| `block-08 fixed command.sh` | 213-213 | bash | dda2b4763589a2dd59a1cdad3b912090e8f3fc7eeeafd4ba24e2bf6c43810fbd |
| `block-09 reported fixed output.txt` | 219-220 | text | 07bf4acd883ca3472b470d85103e8bfaf2891bf8a1f69d8e1d18f4212e290622 |
| `block-10 completed-run resume command.sh` | 226-226 | bash | ccc7f802208924759d78247692685f0659d4a407b62c2c6621309c4bdae0ab7d |
| `block-11 two failed fixture development commands.sh` | 232-233 | bash | cf56ca3856d621612865c5d992226e4effe57ede4bc1510e45d037b26ced6d6c |
| `block-12 reported failure output of each fixture attempt.txt` | 239-240 | text | 026ffbe9ff8d58f97c4a79e1447a5f193224d0122072f6225d31407a80d8075b |
| `block-13 final fixture command.sh` | 246-246 | bash | be7a3def99ef14fe65ea5796c9fa4bb3a8c3fcdc45820b2523436a2f38692cba |
| `block-14 reported final fixture output.txt` | 252-252 | text | df8543e0cfcf722c221058bf7be6951c0e8c1e9605d296ffd947326ab282862a |
| `block-15 reported component probes after version 1.2.txt` | 260-266 | text | f28cca0f162fe84a46f882045ceaa2669b40b73aa142583f468a0d9551b0e47e |
| `block-16 reported independent probes of version 1.1, before the amendment.txt` | 272-281 | text | 13722efa11019575d83876302730743cded4eeea2f14b464f8dfed2dbb890d9f |
| `block-17 reported independent probes after version 1.2.txt` | 287-297 | text | 3570171952d43bea9d9320a23b04757076fd0820611f413b2b7ef5d6fbc23c21 |
| `block-18 reported task label permutation probe.txt` | 303-303 | text | 5d5fd5bb9097244925dce30daadfd0e08e1a858ff07ac48cfed84edcfb89d10e |
| `block-19 reported final integration summaries.txt` | 309-413 | text | c880ddbe2cb1d9fffe9eefe32b3f084f7b80259d9571e160a137e52380161d34 |
| `temporal_selector/selector.py` | 421-517 | python | 19f431daf472fb2053900e0beeb9e125a7aa29cc5df69d00b2571dbb02bb22c9 |
| `temporal_selector/assay.py` | 523-669 | python | b643bf938f72ebfca21725681caa43f7f15b6e47db61e8a84e4531ef24a43cef |
| `temporal_selector/runner.py` | 675-840 | python | ec5c53dbad409ba47604a148ed45ca205a036dd0d6971b249e8b58c9feaaec12 |
| `temporal_selector/summarize.py` | 846-894 | python | da584c20fe34d0c25bef30d7fb61d4475b2964e0ee2cf2b74b8f53f05150027e |
| `temporal_selector/checks.py` | 900-956 | python | dff1e5b5b2c1f0db2bbf97245562aed95d984d6833be63b9de27ab8dc3f45246 |
| `temporal_selector/integration_checks.py` | 962-1015 | python | b0c9d2fcb78bfe38ca3c7530730ff7c928e1187014a0e6905bdef867a9382041 |
| `independent_test.py` | 1021-1202 | python | 3c27658efc123ad0e47987adf8b418822265852d174a09454c61e6830e61d0cc |
| `evidence/additional_check.py` | 1208-1220 | python | ebb761e96736e2a52b000f3a58ce7c387be90854507871b4a745420f6ec9e1cf |
| `block-28 reported file hashes.txt` | 1228-1235 | text | 029ad7d84cb0b1f11de2d0e2d6b81528caf4c43e045670e2e76626d063967f5d |
