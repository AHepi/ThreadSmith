# Runtime and smoke evidence

Written by: OpenAI Codex

Execution date: 21 September 2026 (UTC).

| Component | Identity |
| --- | --- |
| Python | 3.12.14 |
| SWI-Prolog | 9.0.4 for x86_64-linux |
| s(CASP) | 1.1.4 on SWI-Prolog 9.0.4 |
| s(CASP) executable | `/home/claude/sCASP/scasp` resolving to `/tmp/sCASP/scasp` |
| s(CASP) SHA-256 | `2110e60890a766b1a630dba595f4e9752f01662ebd5301d61af1fba685fa2ad7` |
| s(CASP) repository commit | `2dfbdb9cb41f8b9198f19289bab73dd72efad46a` |
| Patched rig-1 driver | `eff1dee15bebc9771040d52e3e27a75f3b383328d119c7c6e204e0b671b7751b` |
| Patched rig-1 rules | `7f10c6f40f8618d1be5bcfb2cf1e57d149160b03c6f3fd16ac936fdf71d4d16e` |
| Frozen rig-1 driver | `38394806ad7676de0c648a4fcdd2cd9596310cdfb5a105935a73beaec3b12f98` |
| Frozen rig-1 rules | `c075fa9d9e253b911d4cec765024f892b8defd2a68b74edc8cb43a31f1c066dd` |
| Patched rig-2 driver | `046bcfa2b1804ae25d2b4c99019f3615a68e2288e68106bc4e75948ea9b46e84` |
| Patched rig-2 laws | `01ab202374729f89fb41bd727fb2b8f16484738261182249f86cb2b7b1608104` |
| Frozen rig-2 driver | `896244b6bdd916bcd39462a98642de830a86b319c9cbf68f0162d6363138783a` |
| Frozen rig-2 laws | `995704fc52b254a18e049960fe5b66165207942b198c1feb343c341d83465e73` |

The patched rig-1 T05-B smoke report matches the supplied expected report after removing only the variable `Slowest question` time (`0.04` observed versus `0.05` expected). Patched and frozen rig 2 also printed the expected C1 substantive verdict. All four exact reports, raw logs, wrapper stderr files and exits are preserved in `smoke/`.

The smoke proves that the executable and historical drivers were invoked and produced their expected top-level prose. It does not prove that every internal query succeeded. The raw smoke logs contain missing-predicate errors which the drivers suppress. That distinction is carried into every later execution summary: a wrapper exit of zero, `NO FAULT FOUND`, `Fine`, or a gauge-only report is never promoted to a clean semantic answer when the bearing raw query errored.
