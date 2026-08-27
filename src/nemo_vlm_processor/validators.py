"""Artifact directory integrity validators."""
import os

def validate_saved_artifacts(output_dir: str) -> bool:
    if not os.path.exists(output_dir):
        return False
    files = os.listdir(output_dir)
    return any(f.endswith(".json") for f in files)
