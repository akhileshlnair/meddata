#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from datasets import load_dataset


ROOT = Path(__file__).resolve().parents[1]


def first_present(row: dict[str, Any], keys: tuple[str, ...]) -> Any:
    for key in keys:
        value = row.get(key)
        if value not in (None, "", [], {}):
            return value
    return None


def normalize_row(dataset_name: str, row: dict[str, Any]) -> dict[str, Any]:
    if row.get("query") and (row.get("answer") or row.get("thinking") or row.get("reasoning")):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["query"],
            "answer": row.get("answer"),
        }
        if row.get("reasoning") not in (None, "", [], {}):
            record["reasoning"] = row["reasoning"]
        if row.get("thinking") not in (None, "", [], {}):
            record["thinking"] = row["thinking"]
        if row.get("id_in_dataset") not in (None, "", [], {}):
            record["id_in_dataset"] = row["id_in_dataset"]
        return record

    if row.get("description") and row.get("transcription"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["description"],
            "answer": row["transcription"],
        }
        for key in ("medical_specialty", "sample_name", "keywords"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("questions") and row.get("answers"):
        questions = row["questions"]
        answers = row["answers"]
        question = None
        if isinstance(questions, list) and questions:
            first = questions[0]
            question = first[0] if isinstance(first, list) and first else first
        answer = None
        if isinstance(answers, list) and answers:
            answer = answers[0]
        record = {"source_dataset": dataset_name}
        if question is not None:
            record["question"] = question
        if answer is not None:
            record["answer"] = answer
        for key in ("questions", "answers"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("messages"):
        record: dict[str, Any] = {
            "source_dataset": dataset_name,
            "messages": row["messages"],
        }
        for key in ("model", "question", "problem"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    question = first_present(row, ("question", "problem", "prompt", "instruction"))
    answer = first_present(row, ("answer", "response", "output", "Complex_CoT", "text"))

    if question is not None or answer is not None:
        record = {"source_dataset": dataset_name}
        if question is not None:
            record["question"] = question
        if answer is not None:
            record["answer"] = answer
        for key in ("instruction", "input", "output", "label", "score", "model", "related_diseases"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("raw_text_content"):
        return {"source_dataset": dataset_name, "text": row["raw_text_content"], "raw": row}

    if row.get("text"):
        return {"source_dataset": dataset_name, "text": row["text"], "raw": row}

    return {"source_dataset": dataset_name, "raw": row}


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror a SFT-oriented medical dataset.")
    parser.add_argument("--dataset", required=True, help="Hugging Face dataset id.")
    parser.add_argument("--out-dir", required=True, help="Relative output directory for JSONL.")
    parser.add_argument("--split", default="train", help="Dataset split to mirror.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum rows to write.")
    parser.add_argument("--progress-every", type=int, default=50_000, help="Print progress every N rows.")
    args = parser.parse_args()

    out_dir = (ROOT / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.dataset.replace('/', '__')}.jsonl"

    stream = load_dataset(args.dataset, split=args.split, streaming=True)
    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for row in stream:
            fh.write(json.dumps(normalize_row(args.dataset, row), ensure_ascii=False) + "\n")
            written += 1
            if args.limit is not None and written >= args.limit:
                break
            if args.progress_every and written % args.progress_every == 0:
                print(f"written {written} rows")

    print(f"wrote {written} rows -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
