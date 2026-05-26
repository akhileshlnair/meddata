#!/usr/bin/env python3
from __future__ import annotations

import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEFAULT_EXTS = {".txt", ".jsonl", ".csv"}


def count_lines(path: pathlib.Path) -> int:
    total = 0
    with path.open("rb") as fh:
        for _ in fh:
            total += 1
    return total


def main() -> None:
    total = 0
    files = []
    for path in DATA_DIR.rglob("*"):
        if path.is_file() and path.suffix in DEFAULT_EXTS and "manifests" not in path.parts:
            files.append(path)
    for path in sorted(files):
        lines = count_lines(path)
        total += lines
        print(f"{lines:>12}  {path.relative_to(ROOT)}")
    print(f"{'=' * 12}  total")
    print(f"{total:>12}")


if __name__ == "__main__":
    main()

