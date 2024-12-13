# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Remove Multiple Spaces
===============================================================================

>>> from techminer2.fields.further_processing import change_to_upper_case
>>> change_to_upper_case(  # doctest: +SKIP  
...     source="abstract",
...     dest="abstract",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd  # type: ignore

from ..fields.protected_fields import PROTECTED_FIELDS


def change_to_upper_case(
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

    _change_to_upper_case(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _change_to_upper_case(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data[dest] = data[source].str.upper()
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
