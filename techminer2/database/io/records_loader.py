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
Records Loader
===============================================================================

>>> from techminer2.database.load import RecordsLoader
>>> (
...     RecordsLoader()
...     .where_directory_is("example/")
...     .build()
... ).head() # doctest: +ELLIPSIS



"""
import pathlib

import pandas as pd  # type: ignore

from ...internals.mixins import InputFunctionsMixin


class RecordsLoader(
    InputFunctionsMixin,
):
    # -------------------------------------------------------------------------
    def build(self):

        file_path = pathlib.Path(self.params.root_dir) / "databases/database.csv.zip"
        records = pd.read_csv(
            file_path,
            encoding="utf-8",
            compression="zip",
        )

        return records


# =============================================================================
