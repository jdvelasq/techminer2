# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts connectors.

>>> from techminer2.package_data.database.internal__sort_connectors import (
...     internal__sort_connectors,
... )
>>> internal__sort_connectors()

"""

import pkg_resources  # type: ignore


def internal__sort_connectors():
    """:meta private:"""

    file_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/database/data/connectors.txt",
    )

    with open(file_path, "r", encoding="utf-8") as file:
        connectors = file.readlines()

    connectors = [
        connector.lower().strip().replace("_", " ") for connector in connectors
    ]
    connectors = sorted(set(connectors))
    connectors = [connector.strip() for connector in connectors]
    connectors = [connector for connector in connectors if len(connector.split()) > 1]

    with open(file_path, "w", encoding="utf-8") as file:
        for connector in connectors:
            file.write(connector + "\n")
