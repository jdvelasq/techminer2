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

>>> from techminer2.fields.further_processing import count_terms_per_record
>>> count_terms_per_record(  # doctest: +SKIP 
...     source="raw_author_keywords",
...     dest="num_raw_author_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES
from ..fields.protected_fields import PROTECTED_FIELDS


def count_terms_per_record(
    source,
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

    _count_terms_per_record(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _count_terms_per_record(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        if source in data.columns:
            data[dest] = data[source].str.split("; ").map(len, na_action="ignore")
            data[dest] = data[dest].fillna(0).astype(int)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
