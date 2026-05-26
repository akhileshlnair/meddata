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

DATASET_SPECS = [
    {"name": dataset, "config": None, "split": "train"}
    for dataset in DATASETS
] + [
    {"name": "FreedomIntelligence/medical-o1-reasoning-SFT", "config": "en", "split": "train"},
    {"name": "FreedomIntelligence/medical-o1-reasoning-SFT", "config": "zh", "split": "train"},
]


def normalize_row(row: dict, dataset_name: str) -> dict:
    instruction = row.get("instruction") or row.get("prompt") or row.get("Question") or ""
    input_text = row.get("input") or row.get("Question") or ""
    output = row.get("output") or row.get("answer") or row.get("response") or row.get("Response") or ""
    reasoning = row.get("Complex_CoT") or row.get("reasoning") or ""
    return {
        "source_dataset": dataset_name,
        "instruction": instruction if instruction else "Answer this medical question truthfully.",
        "input": input_text,
        "output": output,
        "reasoning": reasoning,
        "raw": row,
    }


def main() -> None:
    for spec in DATASET_SPECS:
        dataset_name = spec["name"]
        config = spec["config"]
        split = spec["split"]
        print(f"loading {dataset_name}" + (f" [{config}]" if config else ""))
        if config:
            dataset = load_dataset(dataset_name, config, split=split)
        else:
            dataset = load_dataset(dataset_name, split=split)
        suffix = f"__{config}" if config else ""
        out_path = OUT_DIR / f"{dataset_name.replace('/', '__')}{suffix}.jsonl"
        with out_path.open("w", encoding="utf-8") as fh:
            for row in dataset:
                fh.write(json.dumps(normalize_row(row, dataset_name), ensure_ascii=False) + "\n")
        print(f"wrote {len(dataset)} rows -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
