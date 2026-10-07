# Where each file came from (reply 02, log S122)

*Written by `tools/s122r02_extract_the_code_blocks_of_reply_02.py`. Every file in this folder is one fenced code block of GPT 6 Astra's reply `tests/S121 Returns from GPT 6 Astra/02 Return - programs that need history.md`, copied unchanged: the lines between the fences, then one newline (the reply's own extractor writes files the same way). Nothing was added inside any file. Line numbers are those of the reply's content lines. Files the reply names (`<!-- artifact: ... -->`) keep its path; the others are named `block-NN ...`. Run the script with `--check` to confirm byte for byte.*

*The reply gives one hash: the combined patch's SHA-256 `2c0457b79294a6f0c8562588a31e48149dcc4f71c8650e8a1982fc0e62975ef6`. `history/full.patch` here matches it. The reply's own extractor (block 06), run on the reply, gives the same ten named files byte for byte.*

| File | Reply lines | Fence label | SHA-256 |
|---|---|---|---|
| `block-01 example training reaction.txt` | 61-61 | text | 55e21637e354589b625dc70d94f579cb1dbbcb8ebdd58e32cbb5051df3f9ff58 |
| `history/full.patch` | 76-399 | diff | 2c0457b79294a6f0c8562588a31e48149dcc4f71c8650e8a1982fc0e62975ef6 |
| `block-03 order specimen.org` | 417-424 | text | 717764719659b7e1e726a6e4764e5985a7f8bbaa17b4b21c52c7203ee435b935 |
| `block-04 interval specimen, W=2.org` | 430-438 | text | a2af420bdc9ce905a3e73b804384b4e40b4aadf4364119dff45850fab555cc91 |
| `block-05 sequence specimen.org` | 444-452 | text | e9d8d638110007d4a6a4b9721ada341b11fcff56fd0a01b78a72fe15b2c3f639 |
| `block-06 the reply's own extractor.sh` | 483-492 | bash | 717bb2621cf24450a2bb178f703ba5dc844e31daf6347377266f1b1a1ae990f1 |
| `block-07 build and test commands.sh` | 498-515 | bash | 1ee564759f4fd71b077854ac3a997d423ef3f318563d934952cb68ab0447f9b1 |
| `block-08 400-update run commands.sh` | 525-527 | bash | 6c3b1a790c5ee095e30f5c3227933e311a851ad5d7f2bc10a2369f8f5d44b2ed |
| `block-09 reported comparison output.txt` | 533-540 | text | 60a7db70cd3a34110e40cbe4ed094738858518f024ec6deafbb550bbeab74f72 |
| `block-10 reported final run line.txt` | 546-546 | text | 1201b357886d1a6a6cf07f9b05bb26b5160155dfd696e2bd80f695ada653d021 |
| `block-11 reported final build lines.txt` | 588-589 | text | 8559ab26c3a90c9b2419f8489d795fb39278c62159aa294aa7f1246076163a5a |
| `block-12 reported earlier build failures.txt` | 595-599 | text | b87494ad81641ec1e1a701a7883f45b12fec5b2069d1498ca237faba47e26f8d |
| `block-13 reported final history-harness output.txt` | 607-648 | text | e9ed448bc8e2f634acac0b8a602eaf568e0a7e9f0c4c480dd8ed982c52e21f19 |
| `block-14 reported anticipation-regression output.txt` | 654-668 | text | 9fb9e567dd49267c3d10ea2109c21e5272ba26e262d1b1f1fe690426dba8bf99 |
| `history/spec-v1.txt` | 683-683 | text | d743d33021b3b4c00c63c4d063ce1c5070e8076a500d5365998761326afdc41f |
| `history/setup.py` | 690-699 | python | 63beb7a6702e07d31c2f5dfb23e66a6ffcb35fe3f1569d07d470575d13060f29 |
| `history/check.cc` | 706-828 | cpp | 3f4222f950344014ba565dbf74c1859c2f64cfc52a2e49c71ff62fe0ecf44621 |
| `history/build.py` | 835-843 | python | ca1e360a644349b842f4cab0f780aa347c87d4a51b93b8a4177d141ff54bbafb |
| `work/setup_tests.py` | 850-879 | python | bfac79652233d7dc1147a85ae6aff7a27340ac533b623bc35516df6630e888bd |
| `work/build_test.py` | 886-895 | python | b6198c7180c055ae87d7c7edf84b84628d67955b09c200f20ef645d0aea81eb8 |
| `tests/check.cc` | 902-1043 | cpp | 89c70b860b8166283a6b6c743215012796e92f290a02b8e5827b03d24787a5a1 |
| `work/compare.py` | 1050-1062 | python | de2f10bfc5ba5957ecabc517cd51be7577f87e3136062cb64c9e005c029cd810 |
| `history/test-first.log` | 1069-1105 | text | fc1f11e7436138ce6dc534a8fd93a112f7839fb2f55bdc5d66d45f9a872c7426 |
