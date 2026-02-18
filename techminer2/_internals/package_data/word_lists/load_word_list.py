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


def load_word_list(file_name):
    """:meta private:"""

    data_path = files("techminer2._internals.package_data.word_lists.data").joinpath(
        file_name
    )
    data_path = str(data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]

    return lines
