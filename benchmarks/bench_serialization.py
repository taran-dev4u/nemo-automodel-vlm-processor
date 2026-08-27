"""Micro-benchmark for artifact serialization latency."""
import time
import tempfile
from unittest.mock import MagicMock, patch
from nemo_vlm_processor.merge_vlm import save_model_processor_artifacts

def run_benchmark():
    with patch("transformers.AutoProcessor.from_pretrained") as mock_p:
        mock_p.return_value = MagicMock()
        with tempfile.TemporaryDirectory() as tmp:
            start = time.perf_counter()
            for _ in range(100):
                save_model_processor_artifacts("dummy/vlm", tmp)
            elapsed = time.perf_counter() - start
            print(f"100 iterations: {elapsed:.4f}s ({elapsed/100*1000:.2f}ms/op)")

if __name__ == "__main__":
    run_benchmark()
