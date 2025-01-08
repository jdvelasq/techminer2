# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace descriptors in abstracts and titles"""

import pathlib
import re

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ..message import message


def internal__highlight_tokens(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    """:meta private:"""

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if source not in dataframe.columns:
        return

    keywords = collect_keywords(root_dir)
    keywords = clean_keywords(keywords)

    dataframe[dest] = (
        dataframe[source].str.lower().str.replace("_", " ").str.replace(" / ", " ")
    )

    for index, row in tqdm(dataframe.iterrows(), total=len(dataframe)):

        if pd.isna(row[dest]):
            continue

        text = row[dest]

        key_terms = [str(phrase) for phrase in TextBlob(text).noun_phrases] + [
            k for k in keywords if k in row[dest]
        ]

        key_terms = list(set(key_terms))

        key_terms = sorted(
            key_terms, key=lambda x: (len(x.split(" ")), x), reverse=True
        )

        if len(key_terms) > 0:
            regex = "|".join([re.escape(phrase) for phrase in key_terms])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

            dataframe.loc[index, dest] = text

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def collect_keywords(root_dir):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    terms = []
    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            terms.append(dataframe[column].dropna().copy())
    terms = pd.concat(terms).reset_index(drop=True)

    return terms


def clean_keywords(terms):

    terms = terms.str.translate(str.maketrans("", "", "\"'#!"))
    terms = terms.str.replace(re.compile(r"\(.*\)"), "", regex=True)
    terms = terms.str.replace(re.compile(r"\[.*\]"), "", regex=True)
    terms = terms.str.translate(str.maketrans("_", " "))
    terms = terms.str.lower()
    terms = terms.str.split("; ")
    terms = terms.explode()
    terms = terms.str.strip()
    terms = terms.drop_duplicates()
    terms = terms.to_list()
    terms = [term for term in terms if len(term) > 1]
    terms = [term for term in terms if not any(char.isdigit() for char in term)]
    terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)
    return terms


#############
