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

Example:
    >>> from techminer2._internals.params_mixin import Params
    >>> from techminer2.database._internals.io import internal__load_all_records_from_database
    >>> df = internal__load_all_records_from_database(
    ...         Params(root_directory="examples/fintech/")
    ... ).head()
    >>> df # doctest: +SKIP
                        abbr_source_title  ...  year
    0             Int. J. Appl. Eng. Res.  ...  2016
    1                   Telecommun Policy  ...  2016
    2                 Comput. Hum. Behav.  ...  2016
    3                      China Econ. J.  ...  2016
    4  Contemp. Stud. Econ. Financ. Anal.  ...  2016
    <BLANKLINE>
    [5 rows x 80 columns]



"""
import pandas as pd  # type: ignore

from techminer2._internals.user_data.get_database_file_path import (
    internal__get_database_file_path,
)


def load_all_records_from_database(params):
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
