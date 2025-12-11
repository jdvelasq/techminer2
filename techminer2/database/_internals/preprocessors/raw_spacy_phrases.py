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
import spacy
from pandarallel import pandarallel

spacy_nlp = spacy.load("en_core_web_lg")
pandarallel.initialize(progress_bar=True)


def internal__process_row(row):

    phrases = []

    if not pd.isna(row["tokenized_abstract"]):
        phrases += [
            chunk.text for chunk in spacy_nlp(row["tokenized_abstract"]).noun_chunks
        ]

    if not pd.isna(row["tokenized_document_title"]):
        phrases += [
            chunk.text
            for chunk in spacy_nlp(row["tokenized_document_title"]).noun_chunks
        ]

    if phrases == []:
        return pd.NA

    for symbol in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~":
        phrases = [term for term in phrases if symbol not in term]

    phrases = [
        term
        for term in phrases
        if "a" in term or "e" in term or "i" in term or "o" in term or "u" in term
    ]

    phrases = set(phrases)
    phrases = "; ".join(phrases)

    return phrases


def internal__preprocess_raw_spacy_phrases(root_dir):
    """Run importer."""

    sys.stderr.write("INFO: Creating 'raw_spacy_phrases' column\n\n")
    sys.stderr.flush()

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    # dataframe["raw_abstract_spacy_phrases"] = pd.NA
    dataframe["raw_abstract_spacy_phrases"] = dataframe.parallel_apply(
        internal__process_row, axis=1
    )
    sys.stderr.write("\n\n")
    sys.stderr.flush()

    # for index, row in dataframe.iterrows():

    #     phrases = []

    #     if not pd.isna(row["tokenized_abstract"]):
    #         phrases += [
    #             chunk.text for chunk in spacy_nlp(row["tokenized_abstract"]).noun_chunks
    #         ]

    #     if not pd.isna(row["tokenized_document_title"]):
    #         phrases += [
    #             chunk.text
    #             for chunk in spacy_nlp(row["tokenized_document_title"]).noun_chunks
    #         ]

    #     if phrases == []:
    #         continue

    #     for symbol in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~":
    #         phrases = [term for term in phrases if symbol not in term]

    #     phrases = [
    #         term
    #         for term in phrases
    #         if "a" in term or "e" in term or "i" in term or "o" in term or "u" in term
    #     ]

    #     phrases = set(phrases)

    #     #
    #     #
    #     dataframe.at[index, "raw_spacy_phrases"] = "; ".join(phrases)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


#
