# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import glob
import os.path
import pathlib
import re

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._dtypes import DTYPES


def transformations__extract_noun_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    # Register tqdm pandas progress bar
    tqdm.pandas()

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        dtype=DTYPES,
    )

    if source not in dataframe.columns:
        return

    dataframe[dest] = dataframe[source].progress_apply(extract_noun_phrases_from_record)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def extract_noun_phrases_from_record(text):
    #
    # extract noun phrases
    if not isinstance(text, str):
        return pd.NA

    # New
    text = text.lower()
    text = text.replace("_", " ")
    text = text.replace(" / ", " ")
    #
    noun_phrases = [str(phrase) for phrase in TextBlob(text).noun_phrases]
    #
    #
    noun_phrases = [phrase for phrase in noun_phrases if not phrase.startswith("//")]
    noun_phrases = [phrase.replace("'", "") for phrase in noun_phrases]
    noun_phrases = [
        phrase for phrase in noun_phrases if not re.search(r"[^\w\s]", phrase)
    ]
    noun_phrases = [phrase for phrase in noun_phrases if phrase not in ""]
    #
    #
    noun_phrases = sorted(noun_phrases, key=lambda x: len(x.split(" ")), reverse=True)

    #
    # transform noun phrases to upper cases and replace space with underscore
    if len(noun_phrases) > 0:
        regex = "|".join([re.escape(phrase) for phrase in noun_phrases])
        regex = re.compile(r"\b(" + regex + r")\b")
        text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    noun_phrases = [
        phrase.replace("_", "").strip().replace("  ", " ").upper().replace(" ", "_")
        for phrase in noun_phrases
    ]
    noun_phrases = "; ".join(noun_phrases)
    noun_phrases = noun_phrases.upper()

    return noun_phrases
