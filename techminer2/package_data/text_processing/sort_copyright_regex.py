# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts copyright regex.

>>> from techminer2.package_data.text_processing import (
...     internal__sort_copyright_regex,
... )
>>> internal__sort_copyright_regex()

"""
import pathlib
import re

import pkg_resources  # type: ignore


def internal__sort_copyright_regex():
    """:meta private:"""

    data_path = (
        pathlib.Path("package_data/text_processing/data/") / "copyright_regex.txt"
    )
    data_path = str(data_path)
    data_path = pkg_resources.resource_filename("techminer2", data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.replace("_", " ").lower() for line in lines]
    lines = list(set(lines))
    lines = [(len(line.split(" ")), line) for line in lines]
    # lines = sorted(lines, key=lambda x: x[0], reverse=True)
    lines = sorted(lines, reverse=True)
    lines = [line[1] for line in lines]

    with open(data_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
