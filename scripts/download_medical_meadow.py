#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from datasets import load_dataset


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "derived" / "medical_meadow"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DATASETS = [
    "medalpaca/medical_meadow_medical_flashcards",
    "medalpaca/medical_meadow_wikidoc",
    "medalpaca/medical_meadow_wikidoc_patient_information",
    "medalpaca/medical_meadow_medqa",
    "medalpaca/medical_meadow_mediqa",
    "medalpaca/medical_meadow_pubmed_causal",
    "medalpaca/medical_meadow_health_advice",
    "medalpaca/medical_meadow_cord19",
    "medalpaca/medical_meadow_mmmlu",
]


def normalize_row(row: dict, dataset_name: str) -> dict:
    return {
        "source_dataset": dataset_name,
        "instruction": row.get("instruction") or row.get("prompt") or "",
        "input": row.get("input") or "",
        "output": row.get("output") or row.get("answer") or row.get("response") or "",
        "raw": row,
    }


def main() -> None:
    for dataset_name in DATASETS:
        print(f"loading {dataset_name}")
        dataset = load_dataset(dataset_name, split="train")
        out_path = OUT_DIR / f"{dataset_name.replace('/', '__')}.jsonl"
        with out_path.open("w", encoding="utf-8") as fh:
            for row in dataset:
                fh.write(json.dumps(normalize_row(row, dataset_name), ensure_ascii=False) + "\n")
        print(f"wrote {len(dataset)} rows -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
