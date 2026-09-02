# NVIDIA NeMo Automodel Contributions

Contributions to **NVIDIA NeMo Automodel** ([NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel)) for Vision-Language Models (VLMs) and parameter-efficient fine-tuning (PEFT).

## Key Contributions

- **VLM Processor Serialization Mock Tests (PR #3379 - Merged):** Created mock test fixtures verifying VLM processor save/load cycles without downloading large GPU weights in CI.
- **Qwen2.5-Omni PEFT LoRA Namespaces (PR #3700):** Fixed adapter state dict key prefixes ensuring HuggingFace Hub compatibility.
