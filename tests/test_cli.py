"""Unit tests for CLI argument parsing."""
import unittest
from nemo_vlm_processor.cli import main

class TestCLI(unittest.TestCase):
    def test_cli_importable(self):
        self.assertTrue(callable(main))
