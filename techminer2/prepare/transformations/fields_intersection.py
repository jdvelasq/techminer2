# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields Intersection
===============================================================================

>>> from techminer2.fields.further_processing import fields_intersection
>>> fields_intersection(  # doctest: +SKIP
...     first_field="author_keywords",
...     second_field="index_keywords",
...     dest="intersection",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES
from ..operations.merge_database_fields import merge_database_fields
from ..operations.protected_database_fields import PROTECTED_FIELDS


def fields_intersection(
    compare_field,
    to_field,
    output_field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if output_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{output_field}` is protected")

    transformations__fields_intersection(
        compare_field=compare_field,
        to_field=to_field,
        output_field=output_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
