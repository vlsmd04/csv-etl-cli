import os
import yaml
from pathlib import Path


def load_config(config_path: str = "config.yaml") -> dict:
    config = {}

    if Path(config_path).exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

    # Environment variables override YAML
    config["input_path"] = os.getenv("INPUT_PATH", config.get("input_path"))
    config["output_path"] = os.getenv("OUTPUT_PATH", config.get("output_path"))
    config["log_level"] = os.getenv("LOG_LEVEL", config.get("log_level", "INFO"))
    config["partition_column"] = os.getenv(
        "PARTITION_COLUMN", config.get("partition_column", "date")
    )

    return config