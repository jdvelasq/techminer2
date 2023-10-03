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
...     root_dir="example/", 
... )
--INFO-- Homogenizing local references
--INFO-- 27 local references homogenized

"""
import os
import os.path
import pathlib

import pandas as pd
from tqdm import tqdm

from .._common.thesaurus_lib import load_system_thesaurus_as_dict_reversed


def homogenize_local_references(root_dir):
    """
    :meta private:
    """

    result = ___homogeneize_references(root_dir=root_dir)

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
    main_file = os.path.join(root_dir, "databases/_main.csv.zip")
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")

    #
    # Replace raw_global_references
    data["local_references"] = data["raw_global_references"].str.split("; ")
    data["local_references"] = data["local_references"].map(
        lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
    )
    data["local_references"] = data["local_references"].map(
        lambda x: pd.NA if x == [] else x, na_action="ignore"
    )
    data["local_references"] = data["local_references"].map(
        lambda x: ";".join(sorted(x)) if isinstance(x, list) else x
    )

    data.to_csv(main_file, index=False, encoding="utf-8", compression="zip")


#
# Prepare the reference info for the search
def process(x):
    x = (
        x.str.lower()
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
    return x


def load_raw_global_references_from_main_zip(main_file):
    #
    # Loads raw references from the main database
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")
    raw_references = data["raw_global_references"].dropna()
    raw_references = raw_references.str.split(";").explode().str.strip().drop_duplicates().to_list()
    raw_references = pd.DataFrame({"text": raw_references})
    raw_references["key"] = process(raw_references["text"])
    return raw_references


def load_dataframe_from_main_zip(main_file):
    data_frame = pd.read_csv(main_file, encoding="utf-8", compression="zip")
    data_frame = data_frame[["article", "title", "authors", "year"]]
    data_frame["first_author"] = (
        data_frame["authors"].astype(str).str.split(" ").map(lambda x: x[0].lower())
    )
    data_frame["title"] = data_frame["title"].astype(str).str.lower()
    data_frame = data_frame.dropna()

    data_frame["title"] = process(data_frame["title"])
    data_frame["authors"] = process(data_frame["authors"])
    data_frame["year"] = data_frame["year"].astype(str)
    data_frame = data_frame.sort_values(by=["article"])

    return data_frame.copy()


def ___homogeneize_references(root_dir):
    #
    main_file = os.path.join(root_dir, "databases/_main.csv.zip")
    raw_references = load_raw_global_references_from_main_zip(main_file)
    data_frame = load_dataframe_from_main_zip(main_file)

    thesaurus = {}
    for _, row in tqdm(data_frame.iterrows(), total=data_frame.shape[0]):
        refs = raw_references.copy()
        refs = refs.loc[refs.key.str.contains(row.first_author), :]
        refs = refs.loc[refs.key.str.contains(row.year), :]
        refs = refs.loc[refs.key.str.contains(row.title[:50]), :]

        refs = refs.text.tolist()
        if refs != []:
            thesaurus[row.article] = sorted(refs)

    file_path = pathlib.Path(root_dir) / "local_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for key in sorted(thesaurus.keys()):
            values = thesaurus[key]
            file.write(key + "\n")
            for value in sorted(values):
                file.write("    " + value + "\n")

    print(f"     ---> {len(thesaurus.keys())} local references homogenized")

    return True


def xxx__homogeneize_references(root_dir):
    #
    # Crates the thesaurus file
    #

    main_file = os.path.join(root_dir, "databases/_main.csv.zip")
    raw_references = load_raw_global_references_from_main_zip(main_file)
    references = load_dataframe_from_main_zip(main_file)

    references["raw"] = raw_references

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
                for ref in sorted(row.raw):
                    file.write("    " + ref + "\n")

    print(
        f"     ---> {grouped_references.article.drop_duplicates().shape[0]} local references homogenized"
    )

    #
    # Check not recognized references
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")
    raw_references = data["raw_global_references"].dropna()
    raw_references = raw_references.str.split(";").explode().str.strip()

    not_recognized = raw_references[~raw_references.isin(references.raw)]
    not_recognized = not_recognized.value_counts()

    file_path = pathlib.Path(root_dir) / "not_recognized_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for ref, value in zip(not_recognized.index, not_recognized.values):
            file.write(str(value) + "\n")
            file.write("    " + ref + "\n")

    return True
