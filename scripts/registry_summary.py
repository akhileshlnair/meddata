#!/usr/bin/env python3
from __future__ import annotations

import csv
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "manifests" / "datasets.csv"


def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    by_priority: dict[str, int] = {}
    for row in rows:
        priority = row.get("priority")
        if not priority:
            continue
        by_priority[priority] = by_priority.get(priority, 0) + 1

    print(f"datasets: {len(rows)}")
    for priority in sorted(by_priority, key=lambda value: int(value)):
        print(f"priority {priority}: {by_priority[priority]}")


if __name__ == "__main__":
    main()
