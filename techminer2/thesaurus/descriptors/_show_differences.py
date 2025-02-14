# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Show Differences
===============================================================================

## >>> from techminer2.prepare.thesaurus.descriptors import show_differences
## >>> show_differences(  
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ... )
--INFO-- The example/thesauri/_changes_.the.txt has been generated.

"""
import os

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from .._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)
from .._internals.load_thesaurus_as_data_frame import (
    internal__load_thesaurus_as_data_frame,
)

USER_THESAURUS_FILE = "thesauri/descriptors.the.txt"
RAW_THESAURUS_FILE = "thesauri/_descriptors_.the.txt"

tqdm.pandas()


#
#
# MAIN CODE:
#
#
def show_differences(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    user_th_file = os.path.join(root_dir, USER_THESAURUS_FILE)
    user_data_frame = internal__load_thesaurus_as_data_frame(user_th_file)

    raw_th_file = os.path.join(root_dir, RAW_THESAURUS_FILE)
    raw_th = internal__load_reversed_thesaurus_as_mapping(raw_th_file)

    user_data_frame["same"] = True

    for idx, row in user_data_frame.iterrows():

        current_key = row["key"]
        current_value = row["value"]
        raw_key = raw_th[current_value]
        user_data_frame.loc[idx, "is_different"] = current_key != raw_key

    user_data_frame = user_data_frame[user_data_frame["is_different"]]
    user_data_frame = user_data_frame.groupby("key").agg({"value": list}).reset_index()

    file_path = os.path.join(root_dir, "thesauri/_changes_.the.txt")

    with open(file_path, "w", encoding="utf-8") as file:

        for idx, row in user_data_frame.iterrows():
            file.write(row["key"] + "\n")
            for item in sorted(row["value"]):
                file.write("    " + item + "\n")

    print(f"--INFO-- The {file_path} has been generated.")
