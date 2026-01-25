import string
from pathlib import Path
from typing import Optional

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore
from textblob import TextBlob  # type: ignore

from techminer2._internals import stdout_to_stderr


def _process_row(row: pd.Series) -> Optional[str]:

    phrases: list[str] = []

    if not pd.isna(row["tokenized_abstract"]):
        phrases.extend(TextBlob(row["tokenized_abstract"]).noun_phrases)

    if not pd.isna(row["tokenized_document_title"]):
        phrases.extend(TextBlob(row["tokenized_document_title"]).noun_phrases)

    if not phrases:
        return None

    punctuation = set(string.punctuation.replace("_", ""))
    phrases = [
        term for term in phrases if not any(char in term for char in punctuation)
    ]

    phrases = list(dict.fromkeys(phrases))
    result = "; ".join(phrases)

    return result


def normalize_raw_textblob_phrases(root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    with stdout_to_stderr():
        pandarallel.initialize(progress_bar=True, verbose=2)
        dataframe["raw_textblob_phrases"] = dataframe.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    phrases = dataframe["raw_textblob_phrases"].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases
