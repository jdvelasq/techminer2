# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Apply Thesaurus 
===============================================================================

## >>> from techminer2.prepare.thesaurus.descriptors import apply_thesaurus
## >>> apply_thesaurus( # doctest: +SKIP 
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ... )
--INFO-- Applying `descriptors.the.txt` thesaurus to author/index keywords and abstract/title words

"""
import pathlib

import pandas as pd  # type: ignore

from ..internals.thesaurus__read_reversed_as_dict import (
    thesaurus__read_reversed_as_dict,
)

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # pylint: disable=line-too-long
    print(
        "--INFO-- Applying `descriptors.the.txt` thesaurus to author/index keywords and abstract/title words"
    )

    thesaurus_file = pathlib.Path(root_dir) / THESAURUS_FILE
    thesaurus = thesaurus__read_reversed_as_dict(thesaurus_file)

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    for raw_column, column in [
        ("raw_author_keywords", "author_keywords"),
        ("raw_index_keywords", "index_keywords"),
        ("raw_keywords", "keywords"),
        ("raw_document_title_nlp_phrases", "document_title_nlp_phrases"),
        ("raw_abstract_nlp_phrases", "abstract_nlp_phrases"),
        ("raw_nlp_phrases", "nlp_phrases"),
        ("raw_descriptors", "descriptors"),
    ]:
        if raw_column in dataframe.columns:
            dataframe[column] = dataframe[raw_column].str.split("; ")
            dataframe[column] = dataframe[column].map(
                lambda x: (
                    [thesaurus.get(y.strip(), y.strip()) for y in x]
                    if isinstance(x, list)
                    else x
                )
            )
            dataframe[column] = dataframe[column].map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )
            dataframe[column] = dataframe[column].str.join("; ")

    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
