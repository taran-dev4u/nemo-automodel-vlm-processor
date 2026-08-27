"""CLI entry point for standalone VLM processor extraction."""
import argparse
from nemo_vlm_processor.merge_vlm import save_model_processor_artifacts

def main():
    parser = argparse.ArgumentParser(description="Extract and save VLM processor artifacts")
    parser.add_argument("--model", required=True, help="Hugging Face model ID")
    parser.add_argument("--out", required=True, help="Output destination")
    args = parser.parse_args()
    save_model_processor_artifacts(args.model, args.out)

if __name__ == "__main__":
    main()
