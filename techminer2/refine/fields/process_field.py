# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Process a Field
===============================================================================

>>> from techminer2.refine.fields import copy_field, process_field, delete_field
>>> copy_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> process_field(
...     field="author_keywords_copy",
...     process_func=lambda x: x.str.lower(),
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='author_keywords_copy',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head()
author_keywords_copy
regtech                  28
fintech                  12
regulatory_technology     7
compliance                7
anti_money_laundering     6
Name: OCC, dtype: int64

>>> delete_field(
...     field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def process_field(
    field,
    process_func,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{field}` is protected")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if field in data.columns:
            if data[field].dropna().shape[0] > 0:
                data[field] = process_func(data[field])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
