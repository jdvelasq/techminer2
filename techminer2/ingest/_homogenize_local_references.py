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
import os
import os.path
import pathlib
import re

import pandas as pd
from tqdm import tqdm

from ..thesaurus._core.load_inverted_thesaurus_as_dict import load_inverted_thesaurus_as_dict
from ._message import message


def homogenize_local_references(root_dir):
    """
    :meta private:
    """

    message("Homogenizing local references")

    result = ___homogeneize_references(root_dir=root_dir)

    if result:
        __apply_thesaururs(root_dir=root_dir)


def __apply_thesaururs(root_dir):
    #
    # Apply the thesaurus to raw_global_references
    #

    #
    # Loads the thesaurus
    file_path = pathlib.Path(root_dir) / "reports/local_references.txt"
    th = load_inverted_thesaurus_as_dict(file_path=file_path)

    #
    # Loadas the main database
    main_file = os.path.join(root_dir, "databases/_main.csv.zip")
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")

    #
    # Replace raw_global_references
    data["local_references"] = data["raw_global_references"].str.split("; ")
    data["local_references"] = data["local_references"].map(lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore")
    data["local_references"] = data["local_references"].map(lambda x: pd.NA if x == [] else x, na_action="ignore")
    data["local_references"] = data["local_references"].map(lambda x: ";".join(sorted(x)) if isinstance(x, list) else x)

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
    data_frame = data_frame[["article", "document_title", "authors", "year"]]
    data_frame["first_author"] = data_frame["authors"].astype(str).str.split(" ").map(lambda x: x[0].lower())
    data_frame["document_title"] = data_frame["document_title"].astype(str).str.lower()
    data_frame = data_frame.dropna()

    data_frame["document_title"] = process(data_frame["document_title"])
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
        refs = refs.loc[refs.key.str.lower().str.contains(row.first_author.lower()), :]
        refs = refs.loc[refs.key.str.lower().str.contains(row.year), :]
        refs = refs.loc[
            refs.key.str.lower().str.contains(re.escape(row.document_title[:50].lower())),
            :,
        ]

        refs = refs.text.tolist()
        if refs != []:
            thesaurus[row.article] = sorted(refs)

    file_path = pathlib.Path(root_dir) / "reports/local_references.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for key in sorted(thesaurus.keys()):
            values = thesaurus[key]
            file.write(key + "\n")
            for value in sorted(values):
                file.write("    " + value + "\n")

    print(f"     ---> {len(thesaurus.keys())} local references homogenized")

    return True
