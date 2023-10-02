# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields Difference
===============================================================================

>>> from techminer2.refine.fields import fields_difference, delete_field
>>> fields_difference(
...     first_field="author_keywords",
...     second_field="index_keywords",
...     dst_field="difference",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='difference',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head()
difference
DATA_PROTECTION          4
INNOVATION               3
SUPTECH                  3
SEMANTIC_TECHNOLOGIES    2
CHARITYTECH              2
Name: OCC, dtype: int64

>>> delete_field(
...     field="difference",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd

from .merge_fields import merge_fields
from .protected_fields import PROTECTED_FIELDS


def fields_difference(
    first_field,
    second_field,
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

    #
    # Merge the two fields
    merge_fields(
        fields_to_merge=[first_field, second_field],
        dst_field=dst_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

    #
    # Computes the intersection per database
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip")

        #
        # Compute terms in both columns
        first_terms = (
            data[first_field]
            .dropna()
            .str.split("; ")
            .explode()
            .str.strip()
            .drop_duplicates()
            .tolist()
        )

        second_terms = (
            data[second_field]
            .dropna()
            .str.split("; ")
            .explode()
            .str.strip()
            .drop_duplicates()
            .tolist()
        )

        common_terms = list(set(first_terms).difference(set(second_terms)))

        #
        # Update columns
        data[dst_field] = (
            data[dst_field]
            .str.split("; ")
            .map(lambda x: [z for z in x if z in common_terms], na_action="ignore")
        )
        data[dst_field] = data[dst_field].map(
            lambda x: "; ".join(x) if isinstance(x, list) else x, na_action="ignore"
        )

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
