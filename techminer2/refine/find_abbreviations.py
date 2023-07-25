# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Find Abbreviations 
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.

>>> from techminer2.refine import find_abbreviations
>>> find_abbreviations(
...     #
...     # THESAURUS PARAMS:
...     thesaurus_file="descriptors.txt",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
... )
--INFO-- The file data/regtech/descriptors.txt has been reordered.

"""
import os.path

import pandas as pd

from ..thesaurus_lib import load_system_thesaurus_as_dict, load_system_thesaurus_as_frame


def find_abbreviations(
    #
    # THESAURUS PARAMS:
    thesaurus_file="descriptors.txt",
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Find abbreviations and reorder the thesaurus to reflect the search.

    :meta private:
    """

    ###

    file_path = os.path.join(root_dir, thesaurus_file)
    frame = load_system_thesaurus_as_frame(file_path)
    frame["value"] = frame["value"].str.replace("_", " ")

    frame["abbreviation"] = frame["value"].map(_extract_abbreviation)
    abbreviations = frame["abbreviation"].dropna().drop_duplicates().to_list()

    for abbr in abbreviations:
        frame["found"] = False
        frame["found"] = frame["found"] | frame["value"].map(lambda x: x == abbr)
        frame["found"] = frame["found"] | frame["value"].map(lambda x: "(" + abbr + ")" in x)
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
