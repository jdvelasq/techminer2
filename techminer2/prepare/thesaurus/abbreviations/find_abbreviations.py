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

>>> from techminer2.thesaurus.abbreviations import find_abbreviations
>>> find_abbreviations(
...     #
...     # DATABASE PARAMS:
...    root_dir="example/", 
... )
--INFO-- The file example/thesauri/descriptors.the.txt has been reordered.

"""
import os.path
import re

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ..internals.thesaurus__read_as_dataframe import thesaurus__read_as_dataframe
from ..internals.thesaurus__read_as_dict import thesaurus__read_as_dict

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def find_abbreviations(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    #
    # Load thesaurus as a data frame
    file_path = os.path.join(root_dir, THESAURUS_FILE)
    frame = thesaurus__read_as_dataframe(file_path)

    #
    # Find abbreviations
    def extract_abbreviation(x):
        if "(" in x:
            abbreviation = x[x.find("(") + 1 : x.find(")")]
            return abbreviation
        return pd.NA

    #
    # List abbreviations
    def list_abbreviations_as_tuples(frame):
        """:meta private:"""

        #
        # Preserve dataframe for checking
        data_frame_org = frame.copy()

        #
        # Search for abbreviations
        frame = frame.copy()
        frame = frame.loc[frame.value.str.contains("(", regex=False), :]
        frame = frame.loc[frame.value.str.contains(")", regex=False), :]
        frame = frame[["value"]].drop_duplicates()
        frame["abbreviation"] = frame["value"].map(extract_abbreviation)
        regex = r"\((" + "|".join(frame.abbreviation.dropna().to_list()) + r")\)"
        frame["value"] = frame["value"].str.replace(regex, "", regex=True)
        frame["value"] = frame["value"].str.strip()
        frame = frame.loc[frame.abbreviation != "", :]
        frame = frame.loc[
            frame.value.map(lambda x: " " not in x, na_action="ignore"), :
        ]
        frame = frame.sort_values(by="abbreviation")

        #
        # Check if there is replacements
        frame["valid"] = False
        data_frame_org["value"] = data_frame_org["value"].str.replace(
            regex, "", regex=True
        )
        for index, row in frame.iterrows():
            #
            data_frame = data_frame_org.copy()
            data_frame["valid"] = False
            #
            # contains:
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"_" + row.abbreviation + r"_", regex=False)
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"\b" + row.abbreviation + r"_", regex=True)
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"_" + row.abbreviation + r"\b", regex=True)
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"\b" + row.abbreviation + r"\b", regex=True)
            #
            # ends with:
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"_" + row.abbreviation + r"$", regex=True)
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r" " + row.abbreviation + r"$", regex=True)
            #
            # starts with:
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"^" + row.abbreviation + r"_", regex=True)
            data_frame["valid"] = data_frame["valid"] | data_frame[
                "value"
            ].str.contains(r"^" + row.abbreviation + r" ", regex=True)
            #
            frame.loc[index, "valid"] = data_frame["valid"].any()

        #
        # Select only abbreviations that exists in other rows
        frame = frame.loc[frame.valid, :]

        #
        # Print abbreviations
        # for _, row in frame.iterrows():
        #    print(f"{row.abbreviation}\t{row.value}")

    list_abbreviations_as_tuples(frame)

    #
    # Replace "_" by " "
    frame["value"] = frame["value"].str.replace("_", " ")

    frame["abbreviation"] = frame["value"].map(extract_abbreviation)
    abbreviations = frame["abbreviation"].dropna().drop_duplicates().to_list()
    abbreviations = [abbr for abbr in abbreviations if abbr.strip() != ""]

    #
    # Find terms with abbreviations
    for abbr in tqdm(abbreviations, total=len(abbreviations)):
        abbr = re.escape(abbr)
        frame["found"] = False
        frame["found"] = frame["found"] | frame["value"].map(lambda x: x == abbr)
        frame["found"] = frame["found"] | frame["value"].map(
            lambda x: "(" + abbr + ")" in x
        )
        frame["found"] = frame["found"] | frame["value"].str.contains(
            r"\b" + abbr + r"\b", regex=True
        )
        frame.loc[frame["found"], "abbreviation"] = abbr

    frame = frame[~frame.abbreviation.isna()]
    frame = frame.sort_values(["abbreviation", "key", "value"])

    #
    # Reorder thesaurus
    keys_with_abbr = frame.key.drop_duplicates().to_list()
    thesaurus = thesaurus__read_as_dict(file_path)

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
