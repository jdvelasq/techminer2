from pathlib import Path


def s01_extract_abstract_suffixes(root_directory: str) -> int:

    from .....rev import ExtractAbstractSuffixes

    text = (
        ExtractAbstractSuffixes()
        .having_n_chars(130)
        .where_root_directory(root_directory=root_directory)
        .run()
    )

    filepath = Path(root_directory) / "refine" / "word_lists" / "abstract_suffixes.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        for t in text:
            f.write(t + "\n")

    return len(text)
