#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from datasets import load_dataset


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "derived" / "openmed_medical_reasoning_sft_mega"
DATASET = "OpenMed/Medical-Reasoning-SFT-Mega"


def normalize_messages(row: dict) -> dict:
    messages = row.get("messages") or []
    return {
        "source_dataset": DATASET,
        "messages": messages,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror a large SFT-oriented medical reasoning dataset.")
    parser.add_argument("--limit", type=int, default=1_000_000, help="Maximum rows to write.")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{DATASET.replace('/', '__')}.jsonl"

    stream = load_dataset(DATASET, split="train", streaming=True)
    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for row in stream:
            fh.write(json.dumps(normalize_messages(row), ensure_ascii=False) + "\n")
            written += 1
            if written >= args.limit:
                break
            if written % 50_000 == 0:
                print(f"written {written} rows")
    print(f"wrote {written} rows -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
