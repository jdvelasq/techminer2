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
>>> from techminer2.database._internals.io import internal__load_all_records_from_database
>>> (
...     internal__load_all_records_from_database(
...         Params(root_directory="example/")
...     ).head() # doctest: +ELLIPSIS
... )
    abbr_source_title abstract  ... volume  year
0          Econ. Soc.      NaN  ...     30  2001
1       Psychometrika      NaN  ...     46  1981
2  Strategic Manage J      NaN  ...     20  1999
3         J. Classif.      NaN  ...      5  1988
4         Theor Decis      NaN  ...      9  1978
<BLANKLINE>
[5 rows x 75 columns]




"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from .get_database_file_path import internal__get_database_file_path


def internal__load_all_records_from_database(params):
    """:meta private:"""

    file_path = internal__get_database_file_path(params)
    records = pd.read_csv(
        file_path,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    columns = sorted(records.columns)
    records = records[columns]

    return records


# =============================================================================
