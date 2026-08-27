"""Unit tests for compatibility layer."""
import unittest
from nemo_vlm_processor.compat import check_transformers_version

class TestCompat(unittest.TestCase):
    def test_version_check(self):
        v = check_transformers_version()
        self.assertIsInstance(v, str)
