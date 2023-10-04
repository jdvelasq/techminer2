# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Count Terms per Record
===============================================================================

>>> from techminer2.refine.fields import count_terms_per_record
>>> count_terms_per_record(  # doctest: +SKIP 
...     src_field="raw_author_keywords",
...     dst_field="num_raw_author_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def count_terms_per_record(
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

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src_field in data.columns:
            data[dst_field] = data[src_field].str.split("; ").map(len, na_action="ignore")
            data[dst_field] = data[dst_field].fillna(0).astype(int)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
