import string
import sys
from pathlib import Path
from typing import Optional

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore
from textblob import TextBlob  # type: ignore

from techminer2 import CorpusField
from techminer2._internals import stdout_to_stderr


def _process_row(row: pd.Series) -> Optional[str]:

    phrases: list[str] = []

    if not pd.isna(row[CorpusField.ABS_TOK.value]):
        phrases.extend(
            [
                str(phrase)
                for phrase in list(
                    TextBlob(row[CorpusField.ABS_TOK.value]).noun_phrases  # type: ignore
                )
            ]
        )

    if not pd.isna(row[CorpusField.DOC_TITLE_TOK.value]):
        phrases.extend(
            [
                str(phrase)
                for phrase in list(
                    TextBlob(row[CorpusField.DOC_TITLE_TOK.value]).noun_phrases  # type: ignore
                )
            ]
        )
    if not phrases:
        return None

    punctuation = set(string.punctuation.replace("_", ""))
    phrases = [
        term for term in phrases if not any(char in term for char in punctuation)
    ]

    phrases = list(dict.fromkeys(phrases))
    result = "; ".join(phrases)

    return result


def extract_textblob_phrases(root_directory: str) -> int:

    database_file = Path(root_directory) / "ingest" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        dataframe[CorpusField.TEXTBLOB.value] = dataframe.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )
        sys.stderr.write("\n")

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    phrases = dataframe[CorpusField.TEXTBLOB.value].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases
