# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace descriptors in abstracts and titles"""

import glob
import os
import pathlib
import re

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ..message import message


def preprocessing__highlight_descriptors(root_dir):
    """:meta private:"""

    message("Replacing descriptors in abstracts and titles")
    _replace_hypen_by_space_in_title_column(root_dir)
    terms = _collect_descriptors(root_dir)
    terms = _prepare_descriptors(terms)
    _replace_descritors_on_database(root_dir, terms)


def _replace_hypen_by_space_in_title_column(root_dir):
    message('Replacing "-" by " " in `title` column')

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )
    #
    dataframe["document_title"] = (
        dataframe["document_title"]
        .astype(str)
        .apply(lambda x: x.translate(str.maketrans("-", " ")))
        .apply(lambda x: x.translate(str.maketrans("_", " ")))
    )
    #
    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def _collect_descriptors(root_dir):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    terms = []
    for column in [
        "raw_nlp_phrases",
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            terms.append(dataframe[column].dropna().copy())
    terms = pd.concat(terms)

    return terms


def _prepare_descriptors(terms):
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
    terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)
    return terms


def _replace_descritors_on_database(root_dir, terms):
    #
    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    for index, row in tqdm(dataframe.iterrows(), total=len(dataframe)):
        #
        descriptors = [
            d
            for d in terms
            if (isinstance(row["document_title"], str) and d in row["document_title"])
            or (isinstance(row["abstract"], str) and d in row["abstract"])
        ]

        descriptors_with_length = [(d, len(d.split(" "))) for d in descriptors]
        lengths = sorted(set(l for _, l in descriptors_with_length), reverse=True)

        new_title = str(row["document_title"])
        new_abstract = str(row["abstract"])

        for length in lengths:

            descriptors = [d for d, l in descriptors_with_length if l == length]
            descriptors = sorted(descriptors, reverse=False)

            descriptors = [re.escape(d) for d in descriptors]
            descriptors += [d + r"(?:'s)" for d in descriptors]  # apostrophe
            descriptors += [d + r":" for d in descriptors]  # colon
            descriptors += [r"\(" + d + r"\)" for d in descriptors]  # parenthesis
            descriptors = "|".join(descriptors)
            regex = re.compile(
                r"\b(" + descriptors + r")\b",
                flags=re.IGNORECASE,
            )

            new_title = re.sub(
                regex,
                lambda z: z.group().upper().replace(" ", "_"),
                new_title,
            )

            new_abstract = re.sub(
                regex,
                lambda z: z.group().upper().replace(" ", "_"),
                new_abstract,
            )

        dataframe.loc[index, "document_title"] = new_title
        dataframe.loc[index, "abstract"] = new_abstract

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
