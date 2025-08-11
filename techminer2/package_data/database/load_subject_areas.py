# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
from importlib.resources import files

import pandas as pd  # type: ignore


def internal__load_subject_areas():
    """:meta private:"""

    data_path = files("techminer2.package_data.database.data").joinpath(
        "subject_areas.csv"
    )
    data_path = str(data_path)

    return pd.read_csv(data_path, encoding="utf-8")
