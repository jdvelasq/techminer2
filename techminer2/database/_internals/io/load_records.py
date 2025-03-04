# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

>>> from techminer2._internals.params_mixin import Params
>>> from techminer2.database._internals.io import internal__load_records
>>> (
...     internal__load_records(
...         Params(
...             database="main",
...             record_years_range=(None, None),
...             record_citations_range=(None, None),
...             records_order_by=None,
...             records_match=None,
...             root_directory="example/",
...         )
...     ).head() # doctest: +ELLIPSIS
... ) 
                                                link  ... raw_abstract_copy
0  https://www.scopus.com/inward/record.uri?eid=2...  ...               NaN
1  https://www.scopus.com/inward/record.uri?eid=2...  ...               NaN
2  https://www.scopus.com/inward/record.uri?eid=2...  ...               NaN
3  https://www.scopus.com/inward/record.uri?eid=2...  ...               NaN
4  https://www.scopus.com/inward/record.uri?eid=2...  ...               NaN
<BLANKLINE>
[5 rows x 77 columns]



"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from .get_database_file_path import internal__get_database_file_path


def internal__load_records(params):
    """:meta private:"""

    file_path = internal__get_database_file_path(params)
    records = pd.read_csv(
        file_path,
        encoding="utf-8",
        compression="zip",
    )

    return records


# =============================================================================
