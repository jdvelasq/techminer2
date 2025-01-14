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

## >>> from techminer2.prepare.transformations import extract_my_keywords
## >>> with open("example/my_keywords/keywords.txt", "w", encoding="utf-8") as file: # doctest: +SKIP 
## ...    print("REGTECH", file=file)
## ...    print("FINTECH", file=file)
## ...    print("REGULATORY_COMPLIANCE", file=file)
## ...    print("REGULATORY_TECHNOLOGY", file=file)
## ...    print("ANTI_MONEY_LAUNDERING", file=file)

## >>> extract_my_keywords(   # doctest: +SKIP 
## ...     source="author_keywords",
## ...     dest="my_keywords",
## ...     file_name="keywords.txt",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )


"""
import glob
import os.path

import pandas as pd  # type: ignore

from ...._dtypes import DTYPES
from ...operations.operations__protected_fields import PROTECTED_FIELDS


def extract_my_keywords(
    source,
    dest,
    file_name,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    transformations__extract_my_keywords(
        source=source,
        dest=dest,
        file_name=file_name,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
