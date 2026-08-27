"""Unit tests for logging utilities."""
import unittest
from nemo_vlm_processor.logging_utils import setup_logger

class TestLogging(unittest.TestCase):
    def test_logger_creation(self):
        log = setup_logger("test")
        self.assertIsNotNone(log)
