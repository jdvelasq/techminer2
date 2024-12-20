# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with OR
===============================================================================

>>> from techminer2.fields.further_processing import stemming_field_with_or
>>> stemming_field_with_or(  # doctest: +SKIP
...     items="FINANCIAL_TECHNOLOGY",
...     source="keywords",
...     dest="stemming",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""

from ..._dtypes import DTYPES
from ..operations.protected_database_fields import PROTECTED_FIELDS


def stemming_field_with_or(
    items,
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    transformations__stemming_with_or(
        items=items,
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
