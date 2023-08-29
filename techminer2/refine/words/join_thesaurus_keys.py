# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Join Keys
===============================================================================

>>> from techminer2.refine.words import join_keys
>>> join_keys(
...     contains=("MULTI_LAYER", "MULTILAYER"),
...     #
...     # DATABASE PARAMS:
...     root_dir="data/tm2/",
... )
>>> from techminer2.refine.words import find_string
>>> find_string(
...     #
...     # SEARCH PARAMS:
...     contains=["MULTILAYER"],
...     startswith=None,
...     endswith=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/tm2/",
)

"""
import re
from os.path import isfile, join

import pandas as pd

from ...thesaurus_lib import load_system_thesaurus_as_dict

THESAURUS_FILE = "words.txt"


def join_thesaurus_keys(
    #
    # SEARCH PARAMS:
    equals=None,
    contains=None,
    startswith=None,
    endswith=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    #
    # Load the thesaurus file from disk
    th_file = join(root_dir, THESAURUS_FILE)
    if not isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    thesaurus = load_system_thesaurus_as_dict(th_file)

    #
    # Transforms the thesaurus to a dataframe
    keys = [key for key, values in thesaurus.items() for value in values]
    values = [value for values in thesaurus.values() for value in values]
    data_frame = pd.DataFrame({"key": keys, "value": values})

    #
    # Extracts the list of keys to be replaced
    if equals is not None:
        #
        main_term = contains[0]
        secondary_term = contains[1]
        data_frame.loc[data_frame.key == secondary_term, "key"] = main_term
        #
    elif contains is not None:
        #
        main_term = contains[0]
        secondary_term = contains[1]
        data_frame["key"] = data_frame["key"].str.replace(secondary_term, main_term, regex=False)
        #
    elif startswith is not None:
        #
        main_term = startswith[0]
        secondary_term = startswith[1]
        regex = re.compile(f"^{secondary_term}")
        data_frame["key"] = data_frame["key"].str.replace(regex, main_term, regex=True)
        #
    elif endswith is not None:
        #
        main_term = endswith[0]
        secondary_term = endswith[1]
        regex = re.compile(f"{secondary_term}$")
        data_frame["key"] = data_frame["key"].str.replace(regex, main_term, regex=True)
        #
    else:
        raise ValueError(
            "You must specify at least one of the following parameters: equals, contains, startswith, endswith."
        )

    #
    # Checks non grouped keys
    thesaurus = {row.value: row.key for _, row in data_frame.iterrows()}
    data_frame["key"] = data_frame["key"].map(thesaurus)

    #
    # Saves the new thesaurus to disk
    grouped_data_frame = data_frame.groupby("key", as_index=False).agg(list)
    with open(th_file, "w", encoding="utf-8") as file:
        for _, row in grouped_data_frame.iterrows():
            file.write(row.key + "\n")
            for item in sorted(row.value):
                file.write("    " + item + "\n")

    print(f"--INFO-- The keys in file {th_file} has been replaced.")
