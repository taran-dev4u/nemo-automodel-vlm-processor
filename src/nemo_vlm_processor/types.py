"""Type definitions for VLM processor serialization."""
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass

@dataclass
class ProcessorConfig:
    model_type: str
    trust_remote_code: bool = True
    image_token: str = "<image>"
