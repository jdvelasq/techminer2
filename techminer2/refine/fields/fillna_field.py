# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fill NA
===============================================================================

>>> from techminer2.refine.fields import fillna
>>> fillna(  # doctest: +SKIP 
...     fill_field="author_keywords",
...     with_field="index_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def fillna_field(
    fill_field,
    with_field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if fill_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{fill_field}` is protected")

    _fillna_field(
        fill_field=fill_field,
        with_field=with_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _fillna_field(
    fill_field,
    with_field,
    #
    # DATABASE PARAMS:
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if fill_field in data.columns:
            data[fill_field].mask(data[fill_field].isnull(), data[with_field])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
