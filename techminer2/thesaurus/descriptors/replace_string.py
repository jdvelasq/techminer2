# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace String 
===============================================================================

>>> from techminer2.thesaurus.descriptors import replace_string
>>> replace_string( # doctest: +SKIP
...     #
...     # SEARCH PARAMS:
...     contains='ARTIFICIAL_INTELLIGENCE',
...     startswith=None,
...     endswith=None,
...     #
...     # REPLACE PARAMS:
...     replace_by='AI',
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/descriptors.the.txt has been processed.

"""
import os.path
import re

import pandas as pd  #  type: ignore

from .._core.load_thesaurus_as_dict import load_thesaurus_as_dict

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def replace_string(
    #
    # SEARCH PARAMS:
    contains=None,
    startswith=None,
    endswith=None,
    #
    # REPLACE PARAMS:
    replace_by=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    _replace_string(
        #
        # SEARCH PARAMS:
        contains=contains,
        startswith=startswith,
        endswith=endswith,
        #
        # REPLACE PARAMS:
        replace_by=replace_by,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    print(f"--INFO-- The file {th_file} has been processed.")


def _replace_string(
    #
    # SEARCH PARAMS:
    exact=None,
    contains=None,
    startswith=None,
    endswith=None,
    #
    # REPLACE PARAMS:
    replace_by=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    th_dict = load_thesaurus_as_dict(
        file_path=th_file,
    )

    # -------------------------------------------------------------------------------------------
    def dict_to_dataframe(th_dict):
        reversed_th = {value: key for key, values in th_dict.items() for value in values}
        data_frame = pd.DataFrame(
            {
                "value": reversed_th.keys(),
                "key": reversed_th.values(),
            }
        )
        return data_frame

    #
    data_frame = dict_to_dataframe(th_dict)

    # -------------------------------------------------------------------------------------------
    def check_parameters():
        if exact is None and contains is None and startswith is None and endswith is None:
            raise ValueError("No filter provided")

        n_params = 0
        n_params += 1 if exact is not None else 0
        n_params += 1 if contains is not None else 0
        n_params += 1 if startswith is not None else 0
        n_params += 1 if endswith is not None else 0
        if n_params > 1:
            raise ValueError("More than one filter provided")

        if replace_by is None:
            raise ValueError("No replace_by provided")

    #
    check_parameters()

    # -------------------------------------------------------------------------------------------
    if exact is not None:
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + exact + "$"), replace_by, regex=True)

    # -------------------------------------------------------------------------------------------
    if contains is not None:
        #
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + contains + "$"), replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + contains + "_"), replace_by + "_", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + contains + " "), replace_by + " ", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("_" + contains + "$"), "_" + replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile(" " + contains + "$"), " " + replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("_" + contains + "_"), "_" + replace_by + "_", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile(" " + contains + "_"), " " + replace_by + "_", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("_" + contains + " "), "_" + replace_by + " ", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile(" " + contains + " "), " " + replace_by + " ", regex=True)

    if startswith is not None:
        #
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + startswith + "$"), replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + startswith + "_"), replace_by + "_", regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + startswith + " "), replace_by + " ", regex=True)

    if endswith is not None:
        #
        data_frame["key"] = data_frame["key"].str.replace(re.compile("^" + endswith + "$"), replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile("_" + endswith + "$"), "_" + replace_by, regex=True)
        data_frame["key"] = data_frame["key"].str.replace(re.compile(" " + endswith + "$"), " " + replace_by, regex=True)

    data_frame = data_frame.sort_values(by="key")
    data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})

    # -------------------------------------------------------------------------------------------
    def save_thesaurus():
        with open(th_file, "w", encoding="utf-8") as file:
            for _, row in data_frame.iterrows():
                file.write(row.key + "\n")
                for item in row.value:
                    file.write("    " + item + "\n")

    save_thesaurus()
