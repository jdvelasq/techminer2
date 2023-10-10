"""Change comma by semicolon in keywords for cells bad specified."""

import pathlib

import pandas as pd

from ._message import message

KEYWORDS_MAX_LENGTH = 60


def repair_bad_separators_in_keywords(root_dir):
    """Repair keywords with bad separators in the processed CSV files.
    In Scopus, keywords are separated by semicolons. However, some records
    contain keywords separated by commas.
    keywords.

    :meta private:
    """
    message("Repairing bad separators in keywords")
    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        for column in ["raw_index_keywords", "raw_authors_keywords"]:
            if column in data.columns:
                data[column] = data[column].map(
                    lambda x: x.replace(",", ";")
                    if isinstance(x, str)
                    and ";" not in x
                    and len(x) > KEYWORDS_MAX_LENGTH
                    else x
                )
        data.to_csv(file, index=False, encoding="utf-8", compression="zip")
