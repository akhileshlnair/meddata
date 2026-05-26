#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from datasets import load_dataset


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "derived" / "the_blue_scrubs"
DATASET = "openmed-community/TheBlueScrubs-v1-fixed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror a slice of TheBlueScrubs medical corpus.")
    parser.add_argument("--limit", type=int, default=1_000_000, help="Maximum number of rows to write.")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{DATASET.replace('/', '__')}.jsonl"

    stream = load_dataset(DATASET, split="train", streaming=True)
    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for row in stream:
            text = row.get("text", "")
            record = {
                "source_dataset": DATASET,
                "text": text,
                "raw": row,
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1
            if written >= args.limit:
                break
            if written % 100_000 == 0:
                print(f"written {written} rows")
    print(f"wrote {written} rows -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
