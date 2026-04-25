from pathlib import Path


def s02_extract_abstract_prefixes(root_directory: str) -> int:

    from .....rev import ExtractAbstractPrefixes

    text = (
        ExtractAbstractPrefixes()
        .having_n_chars(130)
        .where_root_directory(root_directory=root_directory)
        .run()
    )

    filepath = Path(root_directory) / "refine" / "word_lists" / "abstract_prefixes.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        for t in text:
            f.write(t + "\n")

    return len(text)
