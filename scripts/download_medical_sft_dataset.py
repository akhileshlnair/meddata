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
    if row.get("question") and row.get("correct_answer"):
        record = {
            "source_dataset": dataset_name,
            "question": row["question"],
            "answer": row["correct_answer"],
        }
        if row.get("correct_option") not in (None, "", [], {}):
            record["correct_option"] = row["correct_option"]
        return record

    if row.get("prompt") and (row.get("completion") or row.get("answer_idx")):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["prompt"],
        }
        if row.get("completion") not in (None, "", [], {}):
            record["answer"] = row["completion"]
        if row.get("prompt_type") not in (None, "", [], {}):
            record["prompt_type"] = row["prompt_type"]
        if row.get("answer_idx") not in (None, "", [], {}):
            record["answer_idx"] = row["answer_idx"]
        if row.get("choices") not in (None, "", [], {}):
            record["choices"] = row["choices"]
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        return record

    if row.get("question") and row.get("answer") and row.get("document_source"):
        record = {
            "source_dataset": dataset_name,
            "question": row["question"],
            "answer": row["answer"],
        }
        for key in (
            "document_source",
            "document_url",
            "category",
            "umls_cui",
            "umls_semantic_types",
            "umls_semantic_group",
            "question_focus",
            "question_type",
            "synonyms",
        ):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("conversations"):
        messages: list[dict[str, Any]] = []
        for item in row["conversations"]:
            role = item.get("from")
            if role == "human":
                mapped_role = "user"
            elif role in {"gt", "assistant"}:
                mapped_role = "assistant"
            else:
                mapped_role = role or "user"
            content = item.get("value") or item.get("content")
            if content is None:
                continue
            if item.get("system") and mapped_role == "user":
                messages.append({"role": "system", "content": item["system"]})
            messages.append({"role": mapped_role, "content": content})
        record: dict[str, Any] = {"source_dataset": dataset_name, "messages": messages}
        if row.get("image") not in (None, "", [], {}):
            record["image"] = row["image"]
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        return record

    if row.get("dialogue"):
        messages: list[dict[str, Any]] = []
        current_role = None
        buffer: list[str] = []
        for raw_line in str(row["dialogue"]).splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith("Patient:"):
                if current_role and buffer:
                    messages.append({"role": current_role, "content": " ".join(buffer).strip()})
                current_role = "user"
                buffer = [line[len("Patient:"):].strip()]
            elif line.startswith("Doctor:"):
                if current_role and buffer:
                    messages.append({"role": current_role, "content": " ".join(buffer).strip()})
                current_role = "assistant"
                buffer = [line[len("Doctor:"):].strip()]
            else:
                buffer.append(line)
        if current_role and buffer:
            messages.append({"role": current_role, "content": " ".join(buffer).strip()})
        if messages:
            record: dict[str, Any] = {"source_dataset": dataset_name, "messages": messages}
            if row.get("description") not in (None, "", [], {}):
                record["description"] = row["description"]
            if row.get("id") not in (None, "", [], {}):
                record["id"] = row["id"]
            return record

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
        for key in ("medical_specialty", "sample_name", "keywords", "derived_keywords", "transcription_length", "normalized_length", "complexity_score"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("instruction") and row.get("task_output"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["instruction"],
            "answer": row["task_output"],
        }
        for key in (
            "description",
            "medical_specialty",
            "sample_name",
            "keywords",
            "derived_keywords",
            "transcription_length",
            "normalized_length",
            "complexity_score",
        ):
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

    if row.get("instruction") and row.get("output"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["instruction"],
            "answer": row["output"],
        }
        if row.get("input") not in (None, "", [], {}):
            record["input"] = row["input"]
        return record

    if isinstance(row.get("text"), str) and "### Human:" in row["text"] and "### Assistant:" in row["text"]:
        text = row["text"]
        human_marker = "### Human:"
        assistant_marker = "### Assistant:"
        human_start = text.find(human_marker)
        assistant_start = text.find(assistant_marker)
        if human_start != -1 and assistant_start != -1 and assistant_start > human_start:
            user_text = text[human_start + len(human_marker):assistant_start].strip()
            assistant_text = text[assistant_start + len(assistant_marker):].strip()
            return {
                "source_dataset": dataset_name,
                "messages": [
                    {"role": "user", "content": user_text},
                    {"role": "assistant", "content": assistant_text},
                ],
            }

    if row.get("raw_text_content"):
        return {"source_dataset": dataset_name, "text": row["raw_text_content"], "raw": row}

    if row.get("text"):
        return {"source_dataset": dataset_name, "text": row["text"], "raw": row}

    return {"source_dataset": dataset_name, "raw": row}


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror a SFT-oriented medical dataset.")
    parser.add_argument("--dataset", required=True, help="Hugging Face dataset id.")
    parser.add_argument("--config", default=None, help="Optional Hugging Face dataset config name.")
    parser.add_argument("--out-dir", required=True, help="Relative output directory for JSONL.")
    parser.add_argument("--split", default="train", help="Dataset split to mirror.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum rows to write.")
    parser.add_argument("--progress-every", type=int, default=50_000, help="Print progress every N rows.")
    args = parser.parse_args()

    out_dir = (ROOT / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.dataset.replace('/', '__')}.jsonl"

    if args.config:
        stream = load_dataset(args.dataset, args.config, split=args.split, streaming=True)
    else:
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
