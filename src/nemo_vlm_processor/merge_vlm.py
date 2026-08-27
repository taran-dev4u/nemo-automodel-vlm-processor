"""
VLM Processor Artifact Serialization Module for NVIDIA NeMo Automodel.
Handles automated AutoProcessor extraction and saving with AutoTokenizer fallback.
"""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def save_model_processor_artifacts(
    model_name_or_path: str,
    output_dir: str,
    trust_remote_code: bool = True
) -> str:
    """
    Save processor artifacts for VLMs or fallback to tokenizer for text-only models.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        from transformers import AutoProcessor
        logger.info(f"Attempting to load AutoProcessor for {model_name_or_path}")
        processor = AutoProcessor.from_pretrained(
            model_name_or_path,
            trust_remote_code=trust_remote_code
        )
        processor.save_pretrained(output_dir)
        logger.info(f"Successfully saved VLM processor artifacts to {output_dir}")
        return output_dir
    except (ValueError, KeyError, AttributeError, Exception) as proc_err:
        logger.warning(
            f"AutoProcessor load failed for {model_name_or_path}: {proc_err}. "
            "Falling back to AutoTokenizer."
        )
        try:
            from transformers import AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained(
                model_name_or_path,
                trust_remote_code=trust_remote_code
            )
            tokenizer.save_pretrained(output_dir)
            logger.info(f"Successfully saved fallback tokenizer artifacts to {output_dir}")
            return output_dir
        except Exception as tok_err:
            logger.error(f"Failed to save tokenizer artifacts: {tok_err}")
            raise RuntimeError(f"Could not serialize processor or tokenizer: {tok_err}") from tok_err
