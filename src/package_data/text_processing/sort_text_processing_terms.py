# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts connectors.

>>> from techminer2.package_data.text_processing import (
...     internal__sort_text_processing_terms,
... )
>>> internal__sort_text_processing_terms()

"""
import glob

import pkg_resources  # type: ignore


def get_file_names():
    dir_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/database/data/*.txt",
    )
    file_names = glob.glob(dir_path)
    return file_names


def sort_file(file_name):

    with open(file_name, "r", encoding="utf-8") as file:
        connectors = file.readlines()

    connectors = [
        connector.lower().strip().replace("_", " ") for connector in connectors
    ]
    connectors = sorted(set(connectors))
    connectors = [connector.strip() for connector in connectors]
    connectors = [connector for connector in connectors if len(connector.split()) > 1]

    with open(file_name, "w", encoding="utf-8") as file:
        for connector in connectors:
            file.write(connector + "\n")


def internal__sort_text_processing_terms():
    """:meta private:"""

    file_names = get_file_names()
    for file_name in file_names:
        sort_file(file_name)
