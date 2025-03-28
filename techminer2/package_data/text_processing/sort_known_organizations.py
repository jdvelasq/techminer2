# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts knwon organizations names.

>>> from techminer2.package_data.text_processing import (
...     internal__sort_known_organizations,
... )
>>> internal__sort_known_organizations()

"""
import pathlib
import re
import unicodedata  # type: ignore

import pkg_resources  # type: ignore


def internal__sort_known_organizations():
    """:meta private:"""

    data_path = (
        pathlib.Path("package_data/text_processing/data/") / "known_organizations.txt"
    )
    data_path = str(data_path)
    data_path = pkg_resources.resource_filename("techminer2", data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    # remove accents
    lines = [unicodedata.normalize("NFKD", line) for line in lines]
    lines = [line.encode("ASCII", "ignore") for line in lines]
    lines = [line.decode() for line in lines]

    lines = [line.replace("_", " ") for line in lines]
    lines = list(set(lines))

    lines = sorted(lines)

    with open(data_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
