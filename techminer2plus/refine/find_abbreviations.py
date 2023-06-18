# flake8: noqa
"""
Find Abbreviations 
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.refine.find_abbreviations(
...     root_dir=root_dir,
... )
--INFO-- The file data/regtech/descriptors.txt has been reordered.


# pylint: disable=line-too-long
"""
import os.path

import pandas as pd

from ..thesaurus import (
    load_system_thesaurus_as_dict,
    load_system_thesaurus_as_frame,
)


def find_abbreviations(
    thesaurus_file="descriptors.txt",
    root_dir="./",
):
    """Find abbreviations and reorder the thesaurus to reflect the search."""

    ###

    file_path = os.path.join(root_dir, thesaurus_file)
    frame = load_system_thesaurus_as_frame(file_path)
    frame["value"] = frame["value"].str.replace("_", " ")

    frame["abbreviation"] = frame["value"].map(_extract_abbreviation)
    abbreviations = frame["abbreviation"].dropna().drop_duplicates().to_list()

    for abbr in abbreviations:
        frame["found"] = False
        frame["found"] = frame["found"] | frame["value"].map(
            lambda x: x == abbr
        )
        frame["found"] = frame["found"] | frame["value"].map(
            lambda x: "(" + abbr + ")" in x
        )
        frame["found"] = frame["found"] | frame["value"].str.contains(
            r"\b" + abbr + r"\b", regex=True
        )
        frame.loc[frame["found"], "abbreviation"] = abbr

    frame = frame[~frame.abbreviation.isna()]
    frame = frame.sort_values(["abbreviation", "key", "value"])

    keys_with_abbr = frame.key.drop_duplicates().to_list()
    thesaurus = load_system_thesaurus_as_dict(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        for key in keys_with_abbr:
            file.write(key + "\n")
            for item in thesaurus[key]:
                file.write("    " + item + "\n")

        for key, items in thesaurus.items():
            if key not in keys_with_abbr:
                file.write(key + "\n")
                for item in items:
                    file.write("    " + item + "\n")

    print(f"--INFO-- The file {file_path} has been reordered.")


def _extract_abbreviation(x):
    """Extracts the abbreviation."""

    if "(" in x:
        abbreviation = x[x.find("(") + 1 : x.find(")")]
        return abbreviation
    return pd.NA
