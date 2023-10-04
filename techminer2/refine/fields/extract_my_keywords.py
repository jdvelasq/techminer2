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

>>> from techminer2.refine.fields import extract_my_keywords, delete_field
>>> with open("example/my_keywords/keywords.txt", "w", encoding="utf-8") as file:
...    print("REGTECH", file=file)
...    print("FINTECH", file=file)
...    print("REGULATORY_COMPLIANCE", file=file)
...    print("REGULATORY_TECHNOLOGY", file=file)
...    print("ANTI_MONEY_LAUNDERING", file=file)

>>> extract_my_keywords(
...     src_field="author_keywords",
...     dst_field="my_keywords",
...     file_name="keywords.txt",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='my_keywords',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head(10)
my_keywords
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
ANTI_MONEY_LAUNDERING     6
REGULATORY_COMPLIANCE     1
Name: OCC, dtype: int64


>>> delete_field(
...     field="my_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def extract_my_keywords(
    src_field,
    dst_field,
    file_name,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dst_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dst_field}` is protected")

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
        data = pd.read_csv(file, encoding="utf-8", compression="zip")

        #
        #
        data[dst_field] = data[src_field].copy()
        data[dst_field] = (
            data[dst_field]
            .str.split("; ")
            .map(lambda x: [z for z in x if z in my_keywords], na_action="ignore")
            .map(set, na_action="ignore")
            .map(sorted, na_action="ignore")
            .str.join("; ")
        )

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
