# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib
import sys

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore


def internal__preprocess_raw_textblob_phrases(root_dir):
    """Run importer."""

    sys.stderr.write("INFO  Creating 'raw_textblob_phrases' column\n")
    sys.stderr.flush()

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    dataframe["raw_textblob_phrases"] = pd.NA

    for index, row in dataframe.iterrows():

        phrases = []

        if not pd.isna(row["tokenized_abstract"]):
            phrases += [
                phrase for phrase in TextBlob(row["tokenized_abstract"]).noun_phrases
            ]

        if not pd.isna(row["tokenized_document_title"]):
            phrases += [
                phrase
                for phrase in TextBlob(row["tokenized_document_title"]).noun_phrases
            ]

        phrases = [term for term in phrases if "." not in term]
        phrases = [term for term in phrases if "(" not in term]
        phrases = [term for term in phrases if ")" not in term]
        phrases = [term for term in phrases if "[" not in term]
        phrases = [term for term in phrases if "]" not in term]
        phrases = [term for term in phrases if "%" not in term]
        phrases = [term for term in phrases if "&" not in term]
        phrases = [term for term in phrases if "!" not in term]
        phrases = [term for term in phrases if "'" not in term]
        phrases = [term for term in phrases if '"' not in term]
        phrases = [term for term in phrases if "+" not in term]
        phrases = [term for term in phrases if "<" not in term]
        phrases = [term for term in phrases if ">" not in term]
        phrases = [term for term in phrases if "=" not in term]
        #
        # phrases = [term for term in phrases if not term.endswith(" et al")]
        # phrases = [term for term in phrases if term != "et al"]
        #
        if phrases == []:
            continue

        phrases = set(phrases)
        #
        #
        dataframe.at[index, "raw_textblob_phrases"] = "; ".join(phrases)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


#
