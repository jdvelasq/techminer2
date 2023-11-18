# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extract My Keywords
===============================================================================

>>> from techminer2.fields.further_processing import extract_my_keywords
>>> with open("example/my_keywords/keywords.txt", "w", encoding="utf-8") as file: # doctest: +SKIP 
...    print("REGTECH", file=file)
...    print("FINTECH", file=file)
...    print("REGULATORY_COMPLIANCE", file=file)
...    print("REGULATORY_TECHNOLOGY", file=file)
...    print("ANTI_MONEY_LAUNDERING", file=file)

>>> extract_my_keywords(   # doctest: +SKIP 
...     source="author_keywords",
...     dest="my_keywords",
...     file_name="keywords.txt",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd

from ..._dtypes import DTYPES
from ..protected_fields import PROTECTED_FIELDS


def extract_my_keywords(
    source,
    dest,
    file_name,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _extract_my_keywords(
        source=source,
        dest=dest,
        file_name=file_name,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _extract_my_keywords(
    source,
    dest,
    file_name,
    #
    # DATABASE PARAMS:
    root_dir,
):
    #
    # Reads my keywords from file
    file_path = os.path.join(root_dir, "my_keywords", file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        my_keywords = [line.strip() for line in file.readlines()]
        my_keywords = [keyword for keyword in my_keywords if keyword != ""]

    #
    # Computes the intersection per database
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)

        #
        #
        data[dest] = data[source].copy()
        data[dest] = (
            data[dest]
            .str.split("; ")
            .map(lambda x: [z for z in x if z in my_keywords], na_action="ignore")
            .map(set, na_action="ignore")
            .map(sorted, na_action="ignore")
            .str.join("; ")
        )

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
