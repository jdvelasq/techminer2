# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Copy a Field
===============================================================================

## >>> from techminer2.fields import copy_field
## >>> copy_field(  # doctest: +SKIP 
## ...     source="author_keywords",
## ...     dest="author_keywords_copy",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""
import glob
import os.path

import pandas as pd  # type: ignore

from .._dtypes import DTYPES
from .protected_fields import PROTECTED_FIELDS


def copy_field(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _copy_field(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _copy_field(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    """:meta private:"""

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        if source in data.columns:
            data[dest] = data[source].copy()
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
