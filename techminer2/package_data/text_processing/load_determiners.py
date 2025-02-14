# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Loads determiners in English language."""

import pkg_resources  # type: ignore


def internal__load_determiners():
    """:meta private:"""

    data_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/text_processing/data/determiners.txt",
    )

    with open(data_path, "r", encoding="utf-8") as file:
        determiners = file.readlines()

    return [determiner.strip() for determiner in determiners]
