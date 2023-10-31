# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
List Abbreviations 
===============================================================================

>>> from techminer2.refine.thesaurus.words import list_abbreviations
>>> list_abbreviations(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
CLASSIFICATION (OF_INFORMATION)
COMPETITION (ECONOMICS)
FINANCIAL_TECHNOLOGY (FINTECH)
INTERNET_OF_THING (IOT)
NETWORKS (CIRCUITS)
PRESSES (MACHINE_TOOLS)

"""
import os.path

from ...._common.thesaurus_lib import load_system_thesaurus_as_frame

THESAURUS_FILE = "thesauri/words.the.txt"


def list_abbreviations(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Find abbreviations and reorder the thesaurus to reflect the search.

    :meta private:
    """

    file_path = os.path.join(root_dir, THESAURUS_FILE)
    frame = load_system_thesaurus_as_frame(file_path)
    frame = frame.loc[frame.value.str.contains("(", regex=False), :]
    frame = frame.loc[frame.value.str.contains(")", regex=False), :]
    frame = frame[["value"]].drop_duplicates()
    frame = frame.sort_values(by="value")

    for _, row in frame.iterrows():
        print(row.value)
