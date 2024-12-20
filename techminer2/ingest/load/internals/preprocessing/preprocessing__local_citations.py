# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib

import pandas as pd  # type: ignore

from ..message import message


def preprocessing__local_citations(root_dir):
    """:meta private:"""

    message("Counting local citations")

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    # counts the appareances of each document in the local references
    # and save as a dictionary
    local_references = dataframe.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each document in documents database
    dataframe["local_citations"] = dataframe.record_id
    dataframe["local_citations"] = dataframe["local_citations"].map(values_dict)
    dataframe["local_citations"] = dataframe["local_citations"].fillna(0)

    # finish
    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
