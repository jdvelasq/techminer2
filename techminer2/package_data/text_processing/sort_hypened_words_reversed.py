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
...     internal__sort_hypened_words_reversed,
... )
>>> internal__sort_hypened_words_reversed()

"""

import pathlib

import pkg_resources  # type: ignore


def internal__sort_hypened_words_reversed():
    """:meta private:"""

    data_path = pathlib.Path("package_data/text_processing/data/") / "hypened_words.txt"
    data_path = str(data_path)
    data_path = pkg_resources.resource_filename("techminer2", data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [(line, line.split("_")[-1] + "_" + line) for line in lines]
    lines = sorted(lines, key=lambda x: x[1])
    lines = [line[0] for line in lines]

    with open(data_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
