# Versions of the fix loop (addendum W13, decision W11)

Every completed round is a commit on branch `claude/hv-skill-scope-kl0oyr`, pushed. A rewind of the harness to a round is `git checkout <hash> -- "Workflow/rigs/W10 harness"`. Tags were made locally (`W10-fix-rounds-1-3`) but the remote does not take tag pushes through this session's git proxy ("Everything up-to-date" with no tag on the remote), so the commit hash is the version mark and is recorded here.

| Round | What | Commit | Faults returned by the review (blocking / wording) |
|---|---|---|---|
| 1-3 | fixers A1, A4, A2 then A1, A4 twice; committed together at log W10 | dd7da4e | after round 3: 1 / 2 (29; 30 fixed by the reviewer, 31) |
