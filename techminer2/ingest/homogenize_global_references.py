# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""

>>> from techminer2.ingest.homogenize_global_references import homogenize_global_references
>>> homogenize_global_references(
...     root_dir="data/regtech/"
... )
--INFO-- Homogenizing global references
--INFO-- 765 global references homogenized

"""
import os
import os.path
import pathlib

import pandas as pd

from ..refine.references.apply_references_thesaurus import apply_references_thesaururs


def homogenize_global_references(root_dir):
    """
    :meta private:
    """

    result = __homogeneize_references(root_dir=root_dir)

    if result:
        apply_references_thesaururs(root_dir=root_dir)


def __homogeneize_references(root_dir):
    #
    # Crates the thesaurus file
    #

    main_file = os.path.join(root_dir, "databases/_main.zip")
    refs_file = os.path.join(root_dir, "databases/_references.zip")

    if not os.path.exists(refs_file):
        return False

    #
    # Loads raw references from the main database
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")
    raw_references = data["raw_global_references"].dropna()
    raw_references = raw_references.str.split(";").explode().str.strip().drop_duplicates()
    raw_references = ";".join(raw_references)

    #
    # Loads refernece info from the references database
    references = pd.read_csv(refs_file, encoding="utf-8", compression="zip")
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
    #
    references["raw"] = references.apply(
        lambda row: [t for t in row.raw if row.first_author in t.lower()], axis=1
    )
    references["raw"] = references.apply(
        lambda row: [t for t in row.raw if row.year in t.lower()], axis=1
    )
    references["raw"] = references["raw"].map(lambda x: pd.NA if x == [] else x)
    references = references.dropna()
    #
    references = references.explode("raw")
    references["raw"] = references["raw"].str.strip()
    references["text"] = references["raw"]
    references["text"] = process(references["text"])

    #
    # Reference matching
    selected_references = references.loc[
        references.apply(
            lambda row: row.year in row.text
            and row.first_author in row.text
            and row.title[:50] in row.text,
            axis=1,
        ),
        :,
    ]

    #
    #
    grouped_references = selected_references.groupby("article", as_index=False).agg(list)

    file_path = pathlib.Path(root_dir) / "global_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in grouped_references.iterrows():
            if row.raw[0] != "":
                file.write(row.article + "\n")
                for ref in sorted(row.raw):
                    file.write("    " + ref + "\n")

    print(
        f"     ---> {grouped_references.article.drop_duplicates().shape[0]} global references homogenized"
    )

    #
    # Check not recognized references
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")
    raw_references = data["raw_global_references"].dropna()
    raw_references = raw_references.str.split(";").explode().str.strip()

    not_recognized = raw_references[~raw_references.isin(selected_references.raw)]
    not_recognized = not_recognized.value_counts()

    file_path = pathlib.Path(root_dir) / "not_recognized_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for ref, value in zip(not_recognized.index, not_recognized.values):
            file.write(str(value) + "\n")
            file.write("    " + ref + "\n")

    return True
