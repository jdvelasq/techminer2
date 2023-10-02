# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Rename a Field
===============================================================================

>>> from techminer2.refine.fields import copy_field, rename_field, delete_field
>>> copy_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> rename_field(
...     src_field="author_keywords_copy",
...     dst_field="author_keywords_renamed",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='author_keywords_renamed',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head()
author_keywords_renamed
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
ANTI_MONEY_LAUNDERING     6
Name: OCC, dtype: int64

>>> delete_field(
...     field="author_keywords_renamed",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def rename_field(
    src_field,
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

    rename = {src_field: dst_field}

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data = data.rename(columns=rename)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
