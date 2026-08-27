"""Compatibility layer for PyTorch 2.x and Hugging Face Transformers 4.40+."""
import importlib.metadata

def check_transformers_version() -> str:
    try:
        return importlib.metadata.version("transformers")
    except Exception:
        return "0.0.0"
