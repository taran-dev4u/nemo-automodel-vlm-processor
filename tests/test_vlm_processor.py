"""Unit tests for VLM processor serialization."""

import unittest
from unittest.mock import MagicMock, patch

from nemo_vlm_processor.merge_vlm import save_model_processor_artifacts

class TestVLMProcessorSerialization(unittest.TestCase):
    """Test suite for VLM processor artifact saving."""

    @patch("transformers.AutoProcessor.from_pretrained")
    def test_vlm_processor_saved_successfully(self, mock_from_pretrained):
        mock_processor = MagicMock()
        mock_from_pretrained.return_value = mock_processor

        out_dir = "/tmp/test_vlm_output"
        res = save_model_processor_artifacts("nvidia/dummy-vlm-model", out_dir)

        mock_from_pretrained.assert_called_once_with("nvidia/dummy-vlm-model", trust_remote_code=True)
        mock_processor.save_pretrained.assert_called_once_with(out_dir)
        self.assertEqual(res, out_dir)

    @patch("transformers.AutoProcessor.from_pretrained", side_effect=ValueError("No processor found"))
    @patch("transformers.AutoTokenizer.from_pretrained")
    def test_fallback_to_tokenizer_on_text_model(self, mock_tok_from_pretrained, mock_proc_from_pretrained):
        mock_tokenizer = MagicMock()
        mock_tok_from_pretrained.return_value = mock_tokenizer

        out_dir = "/tmp/test_tok_output"
        res = save_model_processor_artifacts("nvidia/dummy-text-model", out_dir)

        mock_proc_from_pretrained.assert_called_once()
        mock_tok_from_pretrained.assert_called_once_with("nvidia/dummy-text-model", trust_remote_code=True)
        mock_tokenizer.save_pretrained.assert_called_once_with(out_dir)
        self.assertEqual(res, out_dir)

if __name__ == "__main__":
    unittest.main()
