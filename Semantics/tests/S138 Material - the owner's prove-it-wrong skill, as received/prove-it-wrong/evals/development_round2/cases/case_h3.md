We present Athena-7B, a new open-weights language model that achieves 89.2% on the MMLU benchmark and 76.4% on GSM8K, surpassing the previous best open-weights model in its size class (Mistral-Lux-7B at 85.1% and 71.0% respectively) by a comfortable margin. Training used a curated 2.1T token corpus assembled from public web crawls, code repositories, and licensed book data, with a final supervised fine-tuning stage on 50K instruction-response pairs.

We evaluated Athena-7B using the standard lm-evaluation-harness configuration with 5-shot prompting for MMLU and 8-shot chain-of-thought for GSM8K, matching the protocol reported for the baseline models we compare against. All scores are averaged over three evaluation runs with different prompt orderings to reduce variance, and we report the mean along with standard deviation (MMLU: 89.2 ± 0.3; GSM8K: 76.4 ± 0.6). We also release the model weights and evaluation scripts for reproducibility.

Given the consistent margin over the prior state of the art across both benchmarks, we conclude that Athena-7B represents a meaningful advance in reasoning capability for its parameter class, and recommend it as a strong base model for downstream fine-tuning in applications requiring mathematical and general knowledge reasoning.

Task: before this claim is accepted, what must be questioned or tested?
