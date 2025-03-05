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
Records Writer
===============================================================================

>>> from techminer2.database._internals.io import internal__write_records
>>> internal__write_records(params, records) # doctest: +SKIP


"""
from .get_database_file_path import internal__get_database_file_path


def internal__write_records(params, records):

    file_path = internal__get_database_file_path(params)

    records.to_csv(
        file_path,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


# =============================================================================
