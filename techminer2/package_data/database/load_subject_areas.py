# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd  # type: ignore
import pkg_resources  # type: ignore


def internal__load_subject_areas():
    """:meta private:"""

    data_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/database/data/subject_areas.csv",
    )

    return pd.read_csv(data_path, encoding="utf-8")
