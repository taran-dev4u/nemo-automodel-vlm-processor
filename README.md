# NVIDIA NeMo Automodel — VLM Processor Serialization & LoRA Merge

[![CI](https://github.com/taran-dev4u/nemo-automodel-vlm-processor/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/nemo-automodel-vlm-processor/actions/workflows/ci.yml)
[![Upstream PR](https://img.shields.io/badge/NVIDIA--NeMo%2FAutomodel-PR%20%233379%20Merged-green?logo=github)](https://github.com/NVIDIA-NeMo/Automodel/pull/3379)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-867%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/NVIDIA-NeMo/Automodel)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Production open-source package and test suite extending [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel). This implementation ensures seamless artifact serialization for Vision-Language Models (VLMs) during standalone LoRA adapter weight merges.

---

## 🎯 Background & Problem Statement

When merging LoRA weights into base Vision-Language Models (such as Gemma-VLM, Llama-Vision, Qwen-VL) using `tools/merge_lora.py`, saving only tokenizers or model weights causes downstream inference runtime failures. Multi-modal models require **image processors and chat templates** bundled inside the saved processor directory (`preprocessor_config.json`, `processor_config.json`).

Without processor serialization, loading the merged checkpoint with `AutoProcessor.from_pretrained()` raises `KeyError` or defaults to un-calibrated image normalizations.

---

## 💡 Solution Architecture

This module implements:
1. **Automated VLM Processor Extraction:** Checks for multi-modal processor availability via `AutoProcessor.from_pretrained()` with `trust_remote_code=True`.
2. **Graceful Fallback:** Falls back to `AutoTokenizer` when non-VLM models are processed, ensuring 100% backward compatibility.
3. **Dependency-Safe Unit Testing:** Author of dependency-isolated mock unit tests validating round-trip serialization without requiring heavy multi-gigabyte GPU model downloads in CI.

---

## 🏛️ Upstream Merged Pull Request

- **Repository:** [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel)
- **Pull Request:** [#3379 — test(tools): add focused mock coverage for VLM processor serialization](https://github.com/NVIDIA-NeMo/Automodel/pull/3379)
- **Status:** **Merged upstream** by NVIDIA core maintainers.

---

## 📄 License

Licensed under the Apache License, Version 2.0.
