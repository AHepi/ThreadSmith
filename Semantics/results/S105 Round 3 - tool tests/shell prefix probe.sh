#!/bin/bash
printf '%s\n' "ARGC=$#" >> /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s105_build/prefix_argv.log
for a in "$@"; do printf 'ARG<<%s>>\n' "$a" >> /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s105_build/prefix_argv.log; done
echo "GUARD-SAW-IT"
