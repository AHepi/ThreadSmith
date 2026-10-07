# S96 note - GLM 5.3 as an outside reader, quick research

Written 26 September 2026 by one Claude agent (Opus 5.5) on the owner's question "Should I use GLM 5.3 instead?" (decision S22). Web and project records only; nothing was sent to any model; the S96 run was not touched.

## 1. What GLM 5.3 is

- A real model under that name: **GLM-5.3**, by Z.ai (formerly Zhipu AI, Beijing), released 14 August 2026, open weights two weeks later ([The Decoder](https://the-decoder.com/zhipu-ai-releases-glm-5-3-claims-its-the-strongest-open-weights-coding-model/), [NIST](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities), [GitHub](https://github.com/zai-org/GLM-5)).
- Context 1M tokens; output up to 128K ([Z.ai docs](https://docs.z.ai/guides/llm/glm-5.3)).
- Thinking is always on. `reasoning_effort` takes only `low`, `high`, `max` (default `max`); "any other input will result in an error", so **"medium" is refused** ([Z.ai thinking docs](https://docs.z.ai/guides/capabilities/thinking)).
- OpenAI-style chat completions, model `glm-5.3`, reasoning in `reasoning_content`; $1.40 per million input tokens, $4.40 per million output ([Z.ai pricing](https://docs.z.ai/guides/overview/pricing)).
- Results: the maker publishes mostly coding, agent and security scores, plus "HLE with tools" 62.5 ([Hugging Face](https://huggingface.co/zai-org/GLM-5.3)); I found no result on reasoning over long documents without tools. Artificial Analysis: 45 on its index at `max`, second of 115 open-weight models of its size, "very verbose" (210M tokens against a median of 140M), 71.5 tokens a second, below the median ([Artificial Analysis](https://artificialanalysis.ai/models/glm-5-3)).
- Reliability: no maker figures; guides report streams cut by client timeouts on `max` passes ([Digital Applied](https://www.digitalapplied.com/blog/glm-5-3-api-opens-thinking-no-longer-optional)). Not found: any independent count of disconnects or of answers lost to runaway reasoning.

## 2. What the project's record says

- **S83's third auditor** was DeepSeek (`deepseek-v4-pro`, the owner's third key). Its blind verdicts matched as often as the others' (43, 42, 46 of 52 for DeepSeek, Atria, Mimo), but it reported no holes, by choice according to its own reasoning (holes found by no other reader: 0, 1, 6). It was not added: a good score did not make a willing critic.
- **Mimo** reasoned to its 131,072-token ceiling with no answer at high and at medium (lessons S7, S11, S13); medium was taken but did not bind. Split parts come back (S20); in S96 its four parts came back within 40 minutes.
- **Atria** (ceiling 65,536) failed on large single calls (S90), disconnects near 1,802 seconds (S21), lost ten of 33 attempts in S93 to no HTTP status; S96 part 2 is past 2 h 40 min.
- **Tools**: providers in `tools/s80_call.py` `PROVIDERS`; effort in `s80_common.EFFORT`, levels `("low", "medium", "high")`; ceilings in `MAX_TOKENS_CEILING`. The request shape (`thinking` plus `reasoning_effort`) and the reader of `reasoning_content` already match Z.ai's.

## 3. Gains and losses

Gains: a 128K ceiling (twice Atria's); 1M context; low price (a full 128K-token answer to a 13,000-word part costs about $0.60); open weights, so other hosts exist; a fourth lab.

Losses and risks:
- **No medium.** Decision S17 sets medium for Atria and Mimo only; for GLM the owner must choose `low` or `high` (lesson S16). At `high`, its verbosity resembles Mimo's runaway reasoning.
- **Speed**: at 71.5 tokens a second, a 128K-token attempt takes about 30 minutes.
- **Willingness to challenge**: unknown; DeepSeek shows no benchmark answers it.
- **Independence**: GLM, Mimo and DeepSeek all come from Chinese labs trained hard on coding; whether GLM misses what Mimo misses is unknown. Swapping Atria for GLM could narrow the spread of readers.

## 4. Recommendation

**Not instead of either, for now: pilot GLM 5.3 beside Atria and Mimo on one part, and decide from that pilot whether it replaces Atria.** Mimo stays: it found the most holes no other reader found (S83) and comes back quickly when split. Atria is the slow, disconnect-prone reader, so it is the one GLM might replace.

What it takes:
1. A Z.ai API key from the owner, kept in the scratchpad like the others.
2. The owner's word on effort: `high` suggested (`low` likely too shallow; `max` the most verbose).
3. After the S96 run ends: a `"glm"` entry in `PROVIDERS` (Z.ai's chat URL for the key's plan, `glm-5.3`, a key variable), `"glm": "high"` in `EFFORT["audit"]`, and a ceiling probed as in S83 (docs: 128K).
4. One S93 part (about 13,000 words, already answered by both) sent at full size, with its reading rule committed first (lesson S12) and a watcher outside the agent (S14); one Opus agent compares the three replies against the text, as in S83. The rule names in advance what would support replacing Atria, for instance: GLM finishes inside its ceiling in under an hour, names holes, and finds at least one valid hole neither other reader found.

The pilot settles whether GLM finishes at full size, how long it takes, and whether it names and adds holes. It leaves open: one part is one sample (Mimo's two blind readings of one text differed on 36 of 52 rows), disconnect rates over many calls, and overlap with Mimo's misses.
