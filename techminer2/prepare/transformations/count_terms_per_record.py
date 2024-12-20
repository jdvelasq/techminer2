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

from ..._dtypes import DTYPES
from ..operations.protected_database_fields import PROTECTED_FIELDS


def count_terms_per_record(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    transformations__count_terms_per_record(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
