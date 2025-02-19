# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""

# >>> from techminer2.ingest._homogenize_local_references import homogenize_local_references
# >>> homogenize_local_references(  # doctest: +SKIP
# ...     root_dir="example/", 
# ... )
# -- 001 -- Homogenizing local references
#      ---> 21 local references homogenized

"""

import pathlib
import re
import sys

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ....._internals.log_message import internal__log_message

# TOOD: remove dependency
from .....thesaurus._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)


def internal__preprocess_global_references(root_dir):
    """:meta private:"""

    # sys.stderr.write("\nINFO  Homogenizing global references.")
    sys.stderr.write("\n")
    sys.stderr.flush()

    documents = _create_documents_dataframe(root_dir)
    references = _create_references_dataframe(root_dir)
    thesaurus = _create_thesaurus(documents, references)
    _save_thesaurus(root_dir, thesaurus)
    _apply_thesaurus(root_dir)


def _clean_text(text):
    text = (
        text.str.lower()
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(":", "", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace("'", "", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("  ", " ", regex=False)
    )
    return text


def _create_documents_dataframe(root_dir):

    # loads the dataframe
    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )
    dataframe = dataframe[dataframe.global_citations > 0]
    dataframe = dataframe[["record_id", "document_title", "authors", "year"]]
    dataframe = dataframe.dropna()

    # extracts the first author surname
    dataframe["first_author"] = (
        dataframe["authors"].astype(str).str.split(" ").map(lambda x: x[0].lower())
    )

    # formats the document title field
    dataframe["document_title"] = dataframe["document_title"].astype(str).str.lower()
    dataframe["document_title"] = _clean_text(dataframe["document_title"])

    # formats the authors field
    dataframe["authors"] = _clean_text(dataframe["authors"])

    # formats the year field
    dataframe["year"] = dataframe["year"].astype(str)

    # sorts the dataframe
    dataframe = dataframe.sort_values(by=["record_id"])

    return dataframe.copy()


def _create_references_dataframe(root_dir):

    # loads the dataframe
    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )
    dataframe = dataframe[["raw_global_references"]].dropna()
    dataframe = dataframe.rename({"raw_global_references": "text"}, axis=1)

    dataframe["text"] = dataframe["text"].str.split(";")
    dataframe = dataframe.explode("text")
    dataframe["text"] = dataframe["text"].str.strip()
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.reset_index(drop=True)

    dataframe["key"] = _clean_text(dataframe["text"])

    return dataframe


def _create_thesaurus(main_documents, references):

    thesaurus = {}
    for _, row in tqdm(
        main_documents.iterrows(),
        total=main_documents.shape[0],
        desc="INFO  Homogenizing global references",
    ):

        refs = references.copy()

        # filters by first author
        refs = refs.loc[refs.key.str.lower().str.contains(row.first_author.lower()), :]

        # filters by year
        refs = refs.loc[refs.key.str.lower().str.contains(row.year), :]

        # filters by document title
        refs = refs.loc[
            refs.key.str.lower().str.contains(
                re.escape(row.document_title[:50].lower())
            ),
            :,
        ]

        if len(refs) > 0:
            thesaurus[row.record_id] = sorted(refs.text.tolist())
            references = references.drop(refs.index)

    return thesaurus


def _save_thesaurus(root_dir, thesaurus):

    file_path = pathlib.Path(root_dir) / "thesaurus/global_references.the.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for key in sorted(thesaurus.keys()):
            values = thesaurus[key]
            file.write(key + "\n")
            for value in sorted(values):
                file.write("    " + value + "\n")


def _apply_thesaurus(root_dir):
    # Apply the thesaurus to raw_global_references

    file_path = pathlib.Path(root_dir) / "thesaurus/global_references.the.txt"
    th = internal__load_reversed_thesaurus_as_mapping(file_path=file_path)

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    # creates a list of references
    dataframe["global_references"] = dataframe["raw_global_references"].str.split("; ")

    # replace the oriignal references by the record_id
    dataframe["global_references"] = dataframe["global_references"].map(
        lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
    )
    dataframe["global_references"] = dataframe["global_references"].map(
        lambda x: pd.NA if x == [] else x, na_action="ignore"
    )
    dataframe["global_references"] = dataframe["global_references"].map(
        lambda x: "; ".join(sorted(x)) if isinstance(x, list) else x
    )

    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
