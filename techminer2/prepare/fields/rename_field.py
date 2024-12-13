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

>>> from techminer2.fields import rename_field
>>> rename_field(  # doctest: +SKIP
...     source="author_keywords",
...     dest="author_keywords_new",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES
from .protected_fields import PROTECTED_FIELDS


def rename_field(
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

    _rename_field(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _rename_field(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    rename = {source: dest}

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        data = data.rename(columns=rename)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
