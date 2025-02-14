# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Loads connectors."""

import pkg_resources  # type: ignore


def internal__load_common_starting_words():
    """:meta private:"""

    data_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/text_processing/data/common_starting_words.txt",
    )

    with open(data_path, "r", encoding="utf-8") as file:
        connectors = file.readlines()

    return [stopword.strip() for stopword in connectors]
