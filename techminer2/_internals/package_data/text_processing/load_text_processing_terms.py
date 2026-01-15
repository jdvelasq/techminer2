# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Loads connectors."""
from importlib.resources import files


def internal__load_text_processing_terms(file_name):
    """:meta private:"""

    data_path = files(
        "techminer2._internals.package_data.text_processing.data"
    ).joinpath(file_name)
    data_path = str(data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]
