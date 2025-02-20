# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Apply Thesaurus
===============================================================================


## >>> from techminer2.thesaurus.abbreviations import ApplyThesaurus
## >>> (
## ...     ApplyThesaurus()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The file example/thesaurus/descriptors.the.txt has been modified.

"""
import os.path
import re

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from .._internals.load_thesaurus_as_mapping import internal__load_thesaurus_as_mapping

DESCRIPTORS_FILE = "thesaurus/descriptors.the.txt"
ABBREVIATIONS_FILE = "thesaurus/abbreviations.the.txt"


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    descriptors_file = os.path.join(root_dir, DESCRIPTORS_FILE)
    abbreviations_file = os.path.join(root_dir, ABBREVIATIONS_FILE)

    # -------------------------------------------------------------------------------------------
    def load_descriptors_as_dict():
        if not os.path.isfile(descriptors_file):
            raise FileNotFoundError(f"The file {descriptors_file} does not exist.")
        descriptors_dict = internal__load_thesaurus_as_mapping(descriptors_file)
        return descriptors_dict

    #
    descriptors_dict = load_descriptors_as_dict()

    # -------------------------------------------------------------------------------------------
    def dict_to_dataframe(descriptors_dict):
        reversed_th = {
            value: key for key, values in descriptors_dict.items() for value in values
        }
        data_frame = pd.DataFrame(
            {
                "value": reversed_th.keys(),
                "key": reversed_th.values(),
            }
        )
        return data_frame

    #
    data_frame = dict_to_dataframe(descriptors_dict)

    # -------------------------------------------------------------------------------------------
    def load_abbreviations_as_dict():
        if not os.path.isfile(abbreviations_file):
            raise FileNotFoundError(f"The file {abbreviations_file} does not exist.")
        abbreviations_dict = internal__load_thesaurus_as_mapping(abbreviations_file)
        return abbreviations_dict

    #
    abbreviations_dict = load_abbreviations_as_dict()

    # -------------------------------------------------------------------------------------------
    for abbr, values in tqdm(
        abbreviations_dict.items(), desc="Reemplacing abbreviations"
    ):
        #
        # Replace abbreviations in descriptor keys
        for value in values:
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + "$"), value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + "_"), value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + " "), value + " ", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + "$"), "_" + value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + "$"), " " + value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + "_"), "_" + value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + "_"), " " + value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + " "), "_" + value + " ", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + " "), " " + value + " ", regex=True
            )

    # -------------------------------------------------------------------------------------------
    data_frame = data_frame.sort_values(by="key")
    data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})

    # -------------------------------------------------------------------------------------------
    def save_thesaurus():
        with open(descriptors_file, "w", encoding="utf-8") as file:
            for _, row in data_frame.iterrows():
                file.write(row.key + "\n")
                for item in row.value:
                    file.write("    " + item + "\n")

    save_thesaurus()
    print("--INFO-- The file example/thesaurus/descriptors.the.txt has been modified.")
