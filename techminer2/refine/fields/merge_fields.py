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

>>> from techminer2.refine.fields import merge_fields, delete_field
>>> merge_fields(
...     fields_to_merge=["raw_author_keywords", "raw_index_keywords"],
...     dst_field="keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='keywords_copy',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head()
keywords_copy
NAN                      36
REGTECH                  28
FINTECH                  12
REGULATORY_COMPLIANCE     9
COMPLIANCE                7
Name: OCC, dtype: int64

>>> delete_field(
...     field="keywords_copy",
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
    fields_to_merge,
    dst_field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dst_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dst_field}` is protected")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Load data
        data = pd.read_csv(file, encoding="utf-8", compression="zip")

        #
        # Merge fields
        new_field = None
        for field in fields_to_merge:
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
        data[dst_field] = new_field

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
