"""Unit tests for artifact validators."""
import unittest
import tempfile
import os
from nemo_vlm_processor.validators import validate_saved_artifacts

class TestValidators(unittest.TestCase):
    def test_empty_dir_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(validate_saved_artifacts(tmp))
