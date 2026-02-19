from __future__ import annotations

from collections import defaultdict
from pathlib import Path


def list_example_directories(examples_dir: str | Path = "examples") -> list[str]:
    """Return directory names inside examples/ excluding names starting with '_'."""
    root = Path(examples_dir)
    return sorted(
        entry.name
        for entry in root.iterdir()
        if entry.is_dir() and not entry.name.startswith("_")
    )


def process_file(directory_name: str, examples_dir: str | Path = "examples") -> dict[str, list[str]]:
    """Group values by the comma-separated item that contains 'Univer'."""
    file_path = (
        Path(examples_dir) / directory_name / "refine" / "thesaurus" / "organizations.the.txt"
    )
    if not file_path.exists():
        return {}

    grouped_values: dict[str, list[str]] = defaultdict(list)
    for raw_line in file_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue

        if not raw_line[:1].isspace():
            continue

        value = raw_line.strip()
        parts = [part.strip() for part in value.split(",")]
        university_items = [part for part in parts if "Univer" in part]
        for university_item in university_items:
            grouped_values[university_item].append(value)

    return dict(grouped_values)


def process_all_example_directories(
    examples_dir: str | Path = "examples", report_file: str | Path = "report.txt"
) -> None:
    """Iterate over example directories, group values, and write keys report."""
    grouped_values: dict[str, list[str]] = defaultdict(list)
    for directory_name in list_example_directories(examples_dir):
        file_groups = process_file(directory_name, examples_dir)
        for university_item, values in file_groups.items():
            grouped_values[university_item].extend(values)

    report_lines = sorted({key.strip() for key in grouped_values if key.strip()})

    report_path = Path(report_file)
    report_path.write_text("\n".join(report_lines) + ("\n" if report_lines else ""), encoding="utf-8")


if __name__ == "__main__":
    process_all_example_directories()
