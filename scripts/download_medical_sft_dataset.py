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


def infer_data_format(data_files: list[str]) -> str:
    suffixes = {Path(path).suffix.lower() for path in data_files}
    if suffixes <= {".json", ".jsonl", ".ndjson"}:
        return "json"
    if suffixes <= {".parquet"}:
        return "parquet"
    if suffixes <= {".arrow"}:
        return "arrow"
    raise ValueError(f"Unsupported local data file format(s): {sorted(suffixes)}")


def normalize_row(dataset_name: str, row: dict[str, Any]) -> dict[str, Any]:
    if row.get("full_question") and row.get("options"):
        choices: list[Any] = []
        if isinstance(row["options"], dict):
            for key in sorted(row["options"].keys(), key=lambda item: int(item) if str(item).isdigit() else str(item)):
                value = row["options"][key]
                if value not in (None, "", [], {}):
                    choices.append(value)
        answer = row.get("correct_option")
        answer_key = str(answer) if answer not in (None, "", [], {}) else None
        if answer_key and isinstance(row["options"], dict):
            answer_value = row["options"].get(answer_key)
            if answer_value not in (None, "", [], {}):
                answer = answer_value
        if isinstance(answer, int):
            if isinstance(row["options"], dict):
                mapped_answer = row["options"].get(str(answer))
                if mapped_answer not in (None, "", [], {}):
                    answer = mapped_answer
            if answer in (None, "", [], {}):
                answer = choices[answer - 1] if 1 <= answer <= len(choices) else answer
        record = {
            "source_dataset": dataset_name,
            "question": row["full_question"],
            "choices": choices,
        }
        if answer not in (None, "", [], {}):
            record["answer"] = answer
        if row.get("full_answer") not in (None, "", [], {}):
            record["full_answer"] = row["full_answer"]
        if row.get("full_answer_no_ref") not in (None, "", [], {}):
            record["full_answer_no_ref"] = row["full_answer_no_ref"]
        if answer_key and isinstance(row.get("explanations"), dict):
            explanation = row["explanations"].get(answer_key)
            if isinstance(explanation, dict) and explanation.get("text") not in (None, "", [], {}):
                record["explanation"] = explanation["text"]
        if row.get("type") not in (None, "", [], {}):
            record["type"] = row["type"]
        if row.get("year") not in (None, "", [], {}):
            record["year"] = row["year"]
        if row.get("lang") not in (None, "", [], {}):
            record["lang"] = row["lang"]
        if row.get("question_id_specific") not in (None, "", [], {}):
            record["question_id_specific"] = row["question_id_specific"]
        return record

    answer_keys = ("answer_a", "answer_b", "answer_c", "answer_d", "answer_e")
    if row.get("clinical_case") and row.get("question") and any(row.get(key) not in (None, "", [], {}) for key in answer_keys):
        choices = [row[key] for key in answer_keys if row.get(key) not in (None, "", [], {})]
        correct = row.get("correct_answers")
        answer = None
        if isinstance(correct, str) and correct:
            correct_letters = [part.strip().upper() for part in correct.replace(",", " ").split() if part.strip()]
            correct_texts = []
            for letter in correct_letters:
                idx = ord(letter[0]) - ord("A")
                if 0 <= idx < len(choices):
                    correct_texts.append(choices[idx])
            if correct_texts:
                answer = "\n".join(correct_texts)
        record = {
            "source_dataset": dataset_name,
            "instruction": f"{row['clinical_case']}\n\nQuestion: {row['question']}",
            "choices": choices,
        }
        if answer not in (None, "", [], {}):
            record["answer"] = answer
        if row.get("task") not in (None, "", [], {}):
            record["task"] = row["task"]
        if row.get("medical_subject") not in (None, "", [], {}):
            record["medical_subject"] = row["medical_subject"]
        if row.get("question_type") not in (None, "", [], {}):
            record["question_type"] = row["question_type"]
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        return record

    if row.get("clinical_case") and row.get("question") and row.get("answer") not in (None, "", [], {}):
        record = {
            "source_dataset": dataset_name,
            "instruction": f"{row['clinical_case']}\n\nQuestion: {row['question']}",
            "answer": row["answer"],
        }
        if row.get("cc_question_number") not in (None, "", [], {}):
            record["cc_question_number"] = row["cc_question_number"]
        if row.get("medical_subject") not in (None, "", [], {}):
            record["medical_subject"] = row["medical_subject"]
        if row.get("question_type") not in (None, "", [], {}):
            record["question_type"] = row["question_type"]
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        return record

    if row.get("enonce") and row.get("propositions"):
        choices = []
        answers = []
        for prop in row["propositions"]:
            text = prop.get("proposition")
            if text not in (None, "", [], {}):
                choices.append(text)
                if prop.get("correct"):
                    answers.append(text)
        record = {
            "source_dataset": dataset_name,
            "instruction": row["enonce"],
            "choices": choices,
        }
        if answers:
            record["answer"] = "\n".join(answers)
        if row.get("item") not in (None, "", [], {}):
            record["item"] = row["item"]
        if row.get("matiere") not in (None, "", [], {}):
            record["matiere"] = row["matiere"]
        if row.get("type") not in (None, "", [], {}):
            record["type"] = row["type"]
        if row.get("_id") not in (None, "", [], {}):
            record["id"] = row["_id"]
        return record

    if row.get("question") and row.get("options") and row.get("answer"):
        choices = row["options"] if isinstance(row["options"], list) else []
        record = {
            "source_dataset": dataset_name,
            "instruction": row["question"],
            "choices": choices,
            "answer": row["answer"],
        }
        if row.get("responses") not in (None, "", [], {}):
            record["responses"] = row["responses"]
        return record

    if row.get("Question_formatted") and row.get("Options"):
        choices = []
        if isinstance(row["Options"], dict):
            for key in sorted(row["Options"].keys()):
                value = row["Options"][key]
                if value not in (None, "", [], {}):
                    choices.append(f"{key}: {value}")
        answer = row.get("Final_answer")
        if isinstance(answer, str) and answer:
            answer = answer.strip()
        if isinstance(row.get("data"), dict):
            data = row["data"]
            if isinstance(data.get("Correct Answer"), str) and data["Correct Answer"]:
                answer = data["Correct Answer"]
            elif isinstance(data.get("Correct Option"), str) and data["Correct Option"]:
                opt = data["Correct Option"].strip().upper()
                mapped = data.get("Options", {}).get(opt) if isinstance(data.get("Options"), dict) else None
                if mapped not in (None, "", [], {}):
                    answer = f"{opt}: {mapped}"
        record = {
            "source_dataset": dataset_name,
            "instruction": f"{row.get('Context', '')}\n\n{row['Question_formatted']}".strip(),
            "choices": choices,
        }
        if answer not in (None, "", [], {}):
            record["answer"] = answer
        if row.get("subject_name") not in (None, "", [], {}):
            record["subject_name"] = row["subject_name"]
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        return record

    if row.get("dataset_info") and row.get("conversations"):
        for convo in row["conversations"]:
            dialogue = convo.get("dialogue") or []
            messages: list[dict[str, Any]] = []
            for item in dialogue:
                role = item.get("role")
                if role == "customer":
                    mapped_role = "user"
                elif role == "agent":
                    mapped_role = "assistant"
                else:
                    mapped_role = role or "user"
                text = item.get("text")
                if text is None:
                    continue
                messages.append({"role": mapped_role, "content": text})
            if messages:
                record: dict[str, Any] = {
                    "source_dataset": dataset_name,
                    "messages": messages,
                }
                if convo.get("id") not in (None, "", [], {}):
                    record["conversation_id"] = convo["id"]
                if convo.get("domain") not in (None, "", [], {}):
                    record["domain"] = convo["domain"]
                if convo.get("problem") not in (None, "", [], {}):
                    record["problem"] = convo["problem"]
                if convo.get("customer_type") not in (None, "", [], {}):
                    record["customer_type"] = convo["customer_type"]
                return record

    if row.get("sent1") and row.get("sent2") and row.get("ending0") is not None:
        choices = [row.get(f"ending{i}") for i in range(5) if row.get(f"ending{i}") is not None]
        label = row.get("label")
        answer = None
        if isinstance(label, int) and 0 <= label < len(choices):
            answer = choices[label]
        record = {
            "source_dataset": dataset_name,
            "question": f"{row['sent1']} {row['sent2']}",
            "choices": choices,
        }
        if answer is not None:
            record["answer"] = answer
        if row.get("id") not in (None, "", [], {}):
            record["id"] = row["id"]
        if row.get("startphrase") not in (None, "", [], {}):
            record["startphrase"] = row["startphrase"]
        return record

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

    if row.get("question") and row.get("response"):
        return {
            "source_dataset": dataset_name,
            "question": row["question"],
            "answer": row["response"],
        }

    if row.get("messages") and isinstance(row["messages"], list):
        messages = []
        for item in row["messages"]:
            role = item.get("role")
            if role not in {"user", "assistant", "system"}:
                if role in {"patient", "customer", "human"}:
                    role = "user"
                elif role in {"agent", "doctor", "gt"}:
                    role = "assistant"
            content = item.get("content")
            if content is None:
                continue
            messages.append({"role": role or "user", "content": content})
        if messages:
            record: dict[str, Any] = {"source_dataset": dataset_name, "messages": messages}
            if row.get("id") not in (None, "", [], {}):
                record["id"] = row["id"]
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

    if row.get("Context") and row.get("Response"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["Context"],
            "answer": row["Response"],
        }
        return record

    if row.get("user_question") and row.get("assistant_answer"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["user_question"],
            "answer": row["assistant_answer"],
        }
        for key in ("topic", "to_doctor", "prompt"):
            if row.get(key) not in (None, "", [], {}):
                record[key] = row[key]
        return record

    if row.get("question_1") and row.get("question_2") and row.get("label") in (0, 1):
        record = {
            "source_dataset": dataset_name,
            "instruction": (
                "Determine whether the following two medical questions ask the same thing.\n"
                f"Question 1: {row['question_1']}\n"
                f"Question 2: {row['question_2']}"
            ),
            "answer": "Yes" if row["label"] == 1 else "No",
            "label": row["label"],
        }
        if row.get("dr_id") not in (None, "", [], {}):
            record["dr_id"] = row["dr_id"]
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

    if row.get("input") and row.get("output"):
        record = {
            "source_dataset": dataset_name,
            "instruction": row["input"],
            "answer": row["output"],
        }
        if row.get("source") not in (None, "", [], {}):
            record["source"] = row["source"]
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
    parser.add_argument(
        "--data-files",
        nargs="+",
        default=None,
        help="Optional raw data files to load instead of the dataset builder.",
    )
    parser.add_argument("--out-dir", required=True, help="Relative output directory for JSONL.")
    parser.add_argument("--split", default="train", help="Dataset split to mirror.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum rows to write.")
    parser.add_argument("--progress-every", type=int, default=50_000, help="Print progress every N rows.")
    args = parser.parse_args()

    out_dir = (ROOT / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.dataset.replace('/', '__')}.jsonl"

    if args.data_files:
        data_files = args.data_files[0] if len(args.data_files) == 1 else args.data_files
        data_format = infer_data_format(args.data_files)
        use_streaming = data_format == "json"
        stream = load_dataset(data_format, data_files=data_files, split=args.split, streaming=use_streaming)
    elif args.config:
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
