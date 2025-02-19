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

>>> from techminer2.database.internals.io import intenal__load_records
>>> (
...     RecordsLoader()
...     .where_directory_is("example/")
...     .build()
... ).head() # doctest: +ELLIPSIS



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
