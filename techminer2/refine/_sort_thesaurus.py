# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


import os.path

import pandas as pd

from ..thesaurus_lib import load_system_thesaurus_as_dict

THESAURUS_FILE = "words.txt"


def _sort_thesaurus(
    #
    # THESAURURS FILE:
    thesaurus_file,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    #
    # Loads the thesaurus file as a dict
    th_file = os.path.join(root_dir, thesaurus_file)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    th_dict = load_system_thesaurus_as_dict(th_file)

    #
    # Saves the sorted thesaurus to the file
    with open(th_file, "w", encoding="utf-8") as file:
        for key in sorted(th_dict.keys()):
            file.write(key + "\n")
            for item in sorted(th_dict[key]):
                file.write("    " + item + "\n")

    print(f"--INFO-- The file {th_file} has been sorted.")
