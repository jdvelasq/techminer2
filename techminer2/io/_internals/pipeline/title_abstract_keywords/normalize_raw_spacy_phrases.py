import string
from pathlib import Path
from typing import Optional

import pandas as pd  # type: ignore
import spacy
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr

spacy_nlp = spacy.load("en_core_web_lg")


def _process_row(row: pd.Series) -> Optional[str]:

    phrases: list[str] = []

    if not pd.isna(row["tokenized_abstract"]):
        phrases.extend(
            chunk.text for chunk in spacy_nlp(row["tokenized_abstract"]).noun_chunks
        )

    if not pd.isna(row["tokenized_document_title"]):
        phrases.extend(
            chunk.text
            for chunk in spacy_nlp(row["tokenized_document_title"]).noun_chunks
        )

    if not phrases:
        return None

    punctuation = set(string.punctuation.replace("_", ""))
    phrases = [
        term for term in phrases if not any(char in term for char in punctuation)
    ]

    vowels = set("aeiou")
    phrases = [term for term in phrases if any(char in vowels for char in term)]

    phrases = list(dict.fromkeys(phrases))
    phrases_str = "; ".join(phrases)

    return phrases_str


def normalize_raw_spacy_phrases(root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    with stdout_to_stderr():
        pandarallel.initialize(progress_bar=True)
        dataframe["raw_spacy_phrases"] = dataframe.parallel_apply(  # type: ignore
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

    phrases = dataframe["raw_spacy_phrases"].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases
