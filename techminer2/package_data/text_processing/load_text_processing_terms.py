# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Loads connectors."""

import pathlib

import pkg_resources  # type: ignore


def internal__load_text_processing_terms(file_name):
    """:meta private:"""

    data_path = pathlib.Path("package_data/text_processing/data/") / file_name
    data_path = str(data_path)
    data_path = pkg_resources.resource_filename("techminer2", data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]
