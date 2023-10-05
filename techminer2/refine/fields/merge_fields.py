# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Merge Fields
===============================================================================

>>> from techminer2.refine.fields import merge_fields
>>> merge_fields(  # doctest: +SKIP
...     fields_to_merge=["author_keywords", "index_keywords"],
...     dest="merged_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def merge_fields(
    sources,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _merge_fields(
        sources=sources,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _merge_fields(
    sources,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Load data
        data = pd.read_csv(file, encoding="utf-8", compression="zip")

        #
        # Merge fields
        new_field = None
        for field in sources:
            if field in data.columns:
                if new_field is None:
                    new_field = data[field].astype(str).str.split("; ")
                else:
                    new_field = new_field + data[field].astype(str).str.split("; ")

        #
        # Remove duplicates and sort
        new_field = new_field.map(lambda x: [z for z in x if z != "nan"])
        new_field = new_field.map(lambda x: sorted(set(x)), na_action="ignore")
        new_field = new_field.map("; ".join, na_action="ignore")
        new_field = new_field.map(lambda x: x if x != "" else pd.NA)

        #
        # Create the new field
        data[dest] = new_field

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
