"""Change comma by semicolon in keywords for cells bad specified."""

import pathlib

import pandas as pd  # type: ignore

from ..._message import message

KEYWORDS_MAX_LENGTH = 60


def preprocessing__raw_author_keywords(root_dir):
    """:meta private:"""
    message("Preprocessing raw_author_keywords")
    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if "raw_authors_keywords" in data.columns:
            data["raw_authors_keywords"] = data["raw_authors_keywords"].map(
                lambda x: (
                    x.replace(",", ";")
                    if isinstance(x, str)
                    and ";" not in x
                    and len(x) > KEYWORDS_MAX_LENGTH
                    else x
                )
            )
        data.to_csv(file, index=False, encoding="utf-8", compression="zip")
