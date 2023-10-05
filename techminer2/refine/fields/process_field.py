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

>>> from techminer2.refine.fields import process_field
>>> process_field(  # doctest: +SKIP
...     field="author_keywords_copy",
...     process_func=lambda x: x.str.lower(),
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
    source,
    dest,
    func,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _process_field(
        field=source,
        dest=dest,
        func=func,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _process_field(
    field,
    dest,
    func,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if field in data.columns:
            if data[field].dropna().shape[0] > 0:
                data[dest] = func(data[field])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
