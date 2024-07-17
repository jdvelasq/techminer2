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

>>> from techminer2.refine.thesaurus.descriptors import list_abbreviations
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

from ...core.thesaurus.load_thesaurus_as_dict import load_thesaurus_as_frame

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def list_abbreviations(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    file_path = os.path.join(root_dir, THESAURUS_FILE)
    frame = load_thesaurus_as_frame(file_path)
    frame = frame.loc[frame.value.str.contains("(", regex=False), :]
    frame = frame.loc[frame.value.str.contains(")", regex=False), :]
    frame = frame[["value"]].drop_duplicates()
    frame = frame.sort_values(by="value")

    for _, row in frame.iterrows():
        print(row.value)
