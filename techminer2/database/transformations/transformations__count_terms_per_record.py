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

>>> from techminer2.database.transformations import transformations__count_terms_per_record
>>> transformations__count_terms_per_record(  
...     source="authors",
...     dest="test_num_authors",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> from techminer2.database.tools import Query
>>> (
...     Query()
...     .set_analysis_params(
...         expr="SELECT authors, test_num_authors FROM database LIMIT 5;",
...     ).set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
                                authors  test_num_authors
0  Kim Y.; Choi J.; Park Y.-J.; Yeon J.                 4
1                   Shim Y.; Shin D.-H.                 2
2                             Chen L./1                 1
3              Romanova I.; Kudinska M.                 2
4                   Gabor D.; Brooks S.                 2

"""

from ..internals.field_operations.internal__count_terms_per_record import (
    internal__count_terms_per_record,
)
from ..operations.operations__protected_fields import PROTECTED_FIELDS


def transformations__count_terms_per_record(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    internal__count_terms_per_record(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
