# NVIDIA NeMo Automodel — VLM Processor Serialization & PEFT LoRA Adapter Namespaces

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-LLM%20%2F%20VLM-red.svg)](https://pytorch.org/)
[![NVIDIA NeMo](https://img.shields.io/badge/NVIDIA-NeMo%20Automodel-76B900.svg)](https://github.com/NVIDIA-NeMo/Automodel)
[![Open Source](https://img.shields.io/badge/Open%20Source-Merged%20%26%20Active%20PRs-green.svg)](https://github.com/NVIDIA-NeMo/Automodel)

---

## 📌 Executive Summary & Open Source Contributions

**NVIDIA NeMo Automodel** is NVIDIA's open-source framework providing high-performance model parallel training, fine-tuning (PEFT/LoRA), and serialization pipelines for Large Language Models (LLMs) and Vision-Language Models (VLMs).

This repository highlights **Upstream Contributions** authored by **Taran Mamidala** to [`NVIDIA-NeMo/Automodel`](https://github.com/NVIDIA-NeMo/Automodel).

---

## 🚀 Key Upstream Engineering Contributions

### 1. Vision-Language Model Processor Serialization Mock Tests ([PR #3379](https://github.com/NVIDIA-NeMo/Automodel/pull/3379) - Merged)
- Built comprehensive unit testing fixtures and mock serialization pipelines verifying VLM multi-modal processors are saved and restored without requiring multi-gigabyte GPU checkpoint downloads in CI.

### 2. Qwen2.5-Omni PEFT LoRA Adapter Key Namespaces ([PR #3700](https://github.com/NVIDIA-NeMo/Automodel/pull/3700))
- Fixed a state dictionary serialization bug where Qwen2.5-Omni LoRA checkpoints improperly placed the `thinker.` prefix outside the `base_model.model` namespace, ensuring seamless HuggingFace Hub compatibility.

---

## 📂 Repository Structure

```
nemo-automodel-vlm-processor/
├── src/nemo_vlm_processor/          # Processor serialization and adapter mappings
├── benchmarks/                      # Serialization benchmark scripts
├── tests/                           # Unit tests with mock VLM models
└── README.md                        # Documentation
```

---

## 👨‍💻 Author & Contributor
- **Author:** Taran Mamidala
- **Upstream Repository:** [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel)
