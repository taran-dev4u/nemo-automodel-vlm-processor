# NVIDIA NeMo Automodel — VLM Processor Serialization & LoRA Merge

[![CI](https://github.com/taran-dev4u/nemo-automodel-vlm-processor/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/nemo-automodel-vlm-processor/actions/workflows/ci.yml)
[![Upstream PR Merged](https://img.shields.io/badge/NVIDIA--NeMo%2FAutomodel-PR%20%233379%20Merged-green?logo=github)](https://github.com/NVIDIA-NeMo/Automodel/pull/3379)
[![Upstream PR Open](https://img.shields.io/badge/NVIDIA--NeMo%2FAutomodel-PR%20%233700-blue?logo=github)](https://github.com/NVIDIA-NeMo/Automodel/pull/3700)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-867%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/NVIDIA-NeMo/Automodel)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Production open-source package and test suite extending [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel). This implementation ensures seamless artifact serialization for Vision-Language Models (VLMs) and proper PEFT LoRA adapter namespace structuring.

---

## 🎯 Background & Problem Statement

1. **VLM Processor Serialization (PR #3379):** When merging LoRA weights into base Vision-Language Models (such as Gemma-VLM, Llama-Vision, Qwen-VL) using `tools/merge_lora.py`, saving only tokenizers or model weights causes downstream inference runtime failures. Multi-modal models require **image processors and chat templates** bundled inside the saved processor directory (`preprocessor_config.json`, `processor_config.json`).
2. **Qwen2.5-Omni PEFT Adapter Namespace (PR #3700):** When saving LoRA adapter checkpoints on `qwen2_5_omni`, keys start with `base_model.model.`. This fix correctly places the `thinker.` prefix inside the PEFT namespace (`base_model.model.thinker...`) enabling external Hugging Face PEFT loading.

---

## 💡 Solution Architecture

This module implements:
1. **Automated VLM Processor Extraction:** Checks for multi-modal processor availability via `AutoProcessor.from_pretrained()` with `trust_remote_code=True`.
2. **Graceful Fallback:** Falls back to `AutoTokenizer` when non-VLM models are processed, ensuring 100% backward compatibility.
3. **PEFT Adapter Namespace Formatting:** Nesting module prefixes inside `base_model.model.` for seamless Hugging Face Hub interoperability.
4. **Dependency-Safe Unit Testing:** Author of dependency-isolated mock unit tests validating round-trip serialization without requiring heavy multi-gigabyte GPU model downloads in CI.

---

## 🏛️ Upstream Pull Requests

- **Repository:** [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel)
- **Pull Request #3379:** [test(tools): add focused mock coverage for VLM processor serialization](https://github.com/NVIDIA-NeMo/Automodel/pull/3379) — **Merged upstream** by NVIDIA maintainers.
- **Pull Request #3700:** [fix(qwen2_5_omni): place thinker prefix inside base_model.model on PEFT saves](https://github.com/NVIDIA-NeMo/Automodel/pull/3700) — **Open / In Review**.

---

## 📄 License

Licensed under the Apache License, Version 2.0.

<!-- sync: 1787836801.5746934 -->

<!-- priority_sync: 1787836827.1593142 -->

<!-- demo_verified_sync: 1787840480.5781407 -->

<!-- permanent_lock: 1787962116.8350842 -->
