# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""

>>> from techminer2.ingest.homogenize_local_references import homogenize_local_references
>>> homogenize_local_references(
...     root_dir="data/regtech/"
... )
--INFO-- Homogenizing local references
--INFO-- 27 local references homogenized

"""
import os
import os.path
import pathlib

import pandas as pd

from ..thesaurus_lib import load_system_thesaurus_as_dict_reversed


def homogenize_local_references(root_dir):
    """
    :meta private:
    """

    result = __homogeneize_references(root_dir=root_dir)

    if result:
        __apply_thesaururs(root_dir=root_dir)


def __apply_thesaururs(root_dir):
    #
    # Apply the thesaurus to raw_global_references
    #

    #
    # Loads the thesaurus
    file_path = pathlib.Path(root_dir) / "local_references.txt"
    th = load_system_thesaurus_as_dict_reversed(file_path=file_path)

    #
    # Loadas the main database
    main_file = os.path.join(root_dir, "databases/_main.csv")
    data = pd.read_csv(main_file, encoding="utf-8")

    #
    # Replace raw_global_references
    data["local_references"] = data["raw_global_references"].str.split(";")
    data["local_references"] = data["local_references"].map(
        lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
    )
    data["local_references"] = data["local_references"].map(
        lambda x: ";".join(x) if isinstance(x, list) else x
    )

    data.to_csv(main_file, index=False, encoding="utf-8")


def __homogeneize_references(root_dir):
    #
    # Crates the thesaurus file
    #

    print("--INFO-- Homogenizing local references")

    main_file = os.path.join(root_dir, "databases/_main.csv")

    #
    # Loads raw references from the main database
    data = pd.read_csv(main_file, encoding="utf-8")
    raw_references = data["raw_global_references"].dropna()
    raw_references = raw_references.str.split(";").explode().str.strip().drop_duplicates()
    raw_references = ";".join(raw_references)

    #
    # Loads refernece info from the references database
    references = pd.read_csv(main_file, encoding="utf-8")
    references = references[["article", "title", "authors", "year"]]
    references["first_author"] = references["authors"].str.split(" ").map(lambda x: x[0].lower())
    references["title"] = references["title"].str.lower()
    references = references.dropna()

    references["raw"] = raw_references

    #
    # Prepare the reference info for the search
    def process(x):
        x = (
            x.str.lower()
            .str.replace(".", "")
            .str.replace(",", "")
            .str.replace(":", "")
            .str.replace("-", " ")
            .str.replace("_", " ")
            .str.replace("'", "")
            .str.replace("  ", " ")
        )
        return x

    references["title"] = process(references["title"])
    references["authors"] = process(references["authors"])
    references["year"] = references["year"].astype(str)

    #
    # Cross-product
    references["raw"] = references["raw"].str.split(";")
    references = references.explode("raw")
    references["raw"] = references["raw"].str.strip()
    references["text"] = references["raw"]
    references["text"] = process(references["text"])

    #
    # Reference matching
    references = references.loc[
        references.apply(
            lambda row: row.year in row.text
            and row.first_author in row.text
            and row.title[:50] in row.text,
            axis=1,
        ),
        :,
    ]

    # references = references.drop_duplicates(subset=["text"])

    #
    #
    grouped_references = references.groupby("article", as_index=False).agg(list)

    file_path = pathlib.Path(root_dir) / "local_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in grouped_references.iterrows():
            if row.raw[0] != "":
                file.write(row.article + "\n")
                for ref in row.raw:
                    file.write("    " + ref + "\n")

    print(
        f"--INFO-- {grouped_references.article.drop_duplicates().shape[0]} local references homogenized"
    )

    return True
