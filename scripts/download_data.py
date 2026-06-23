#!/usr/bin/env python3
"""Download Kaggle AI Recruitment Pipeline Dataset."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
DATASET = "yaswanthkumary/ai-recruitment-pipeline-dataset"
TARGET = DATA_DIR / "recruitment_pipeline.csv"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if TARGET.exists():
        print(f"Dataset already exists: {TARGET}")
        return

    print(f"Downloading {DATASET} from Kaggle...")
    print("Requires: pip install kaggle  +  ~/.kaggle/kaggle.json credentials")
    print()

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "kaggle",
                "datasets",
                "download",
                "-d",
                DATASET,
                "-p",
                str(DATA_DIR),
                "--unzip",
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("\nAutomatic download failed.")
        print("Manual steps:")
        print(f"  1. Download from https://www.kaggle.com/datasets/{DATASET}")
        print(f"  2. Save CSV as: {TARGET}")
        sys.exit(1)

    # Find downloaded CSV (name may vary)
    csvs = list(DATA_DIR.glob("*.csv"))
    if not csvs:
        print("No CSV found after download.")
        sys.exit(1)

    if not TARGET.exists():
        shutil.move(str(csvs[0]), str(TARGET))
        print(f"Saved to {TARGET}")
    else:
        print(f"Ready: {TARGET}")


if __name__ == "__main__":
    main()
