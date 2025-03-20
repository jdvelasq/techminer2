# flake8: noqa
"""Disambiguate author names using Scopus Author(s) ID."""

import pathlib
import sys

import pandas as pd  # type: ignore

from ....._internals.log_message import internal__log_message


def _load_authors_data(root_dir):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )
    authors_data = dataframe[["authors", "authors_id"]]
    authors_data = authors_data.dropna()
    return authors_data


def _generate_author_and_author_id_dataframe(authors_data):

    authors_data = authors_data.copy()

    # Combine authors and authors_id into a single column
    authors_data = authors_data.assign(
        authors_and_ids=authors_data.authors + "#" + authors_data.authors_id
    )
    authors_data = authors_data[["authors_and_ids"]]

    # Split the combined column into separate author and author_id pairs
    authors_data.authors_and_ids = authors_data.authors_and_ids.str.split("#")
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: (x[0].split(";"), x[1].split(";"))
    )
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: list(zip(x[0], x[1]))
    )

    # Explode the list of tuples into separate rows
    authors_data = authors_data.explode("authors_and_ids")

    # Strip whitespace from author and author_id
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: (x[0].strip(), x[1].strip())
    )

    # Reset index and split the tuples into separate columns
    authors_data = authors_data.reset_index(drop=True)
    authors_data["author"] = authors_data.authors_and_ids.apply(lambda x: x[0])
    authors_data["author_id"] = authors_data.authors_and_ids.apply(lambda x: x[1])

    # Drop the combined column and remove duplicates
    authors_data = authors_data.drop(columns=["authors_and_ids"])
    authors_data = authors_data.drop_duplicates()

    return authors_data


def _build_dict_names(dataframe):

    dataframe = dataframe.sort_values(by=["author"])
    dataframe = dataframe.assign(counter=dataframe.groupby(["author"]).cumcount())
    dataframe = dataframe.assign(
        author=dataframe.author + "/" + dataframe.counter.astype(str)
    )
    dataframe.author = dataframe.author.str.replace("/0", "")
    author_id2name = dict(zip(dataframe.author_id, dataframe.author))

    return author_id2name


def _repair_names(root_dir, author_id2name):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    dataframe = dataframe.assign(authors=dataframe.authors_id.copy())
    dataframe["authors"] = dataframe["authors"].str.split(";")
    dataframe["authors"] = dataframe["authors"].map(
        lambda x: [author_id2name[id.strip()] for id in x],
        na_action="ignore",
    )
    dataframe["authors"] = dataframe["authors"].str.join("; ")

    dataframe.to_csv(
        database_file, sep=",", encoding="utf-8", index=False, compression="zip"
    )


def internal__preprocess_author_names(root_dir):
    """Disambiguate author names using Scopus Author(s) ID."""

    sys.stderr.write("INFO  Disambiguating author names\n")
    sys.stderr.flush()

    authors_data = _load_authors_data(root_dir)
    dataframe = _generate_author_and_author_id_dataframe(authors_data)
    author_id2name = _build_dict_names(dataframe)
    _repair_names(root_dir, author_id2name)
