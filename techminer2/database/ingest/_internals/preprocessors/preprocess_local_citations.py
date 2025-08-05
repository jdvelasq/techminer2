# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib
import sys

import pandas as pd  # type: ignore

from ....._internals.log_message import internal__log_message


def internal__preprocess_local_citations(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO  Counting local citations\n")
    sys.stderr.flush()

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "data/processed/database.csv.zip",
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    # counts the appareances of each document in the local references
    # and save as a dictionary
    if dataframe["local_references"].isna().all():

        dataframe["local_citations"] = 0

    else:

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
        dataframe["local_citations"] = dataframe["local_citations"].astype(int)

    # finish
    dataframe.to_csv(
        pathlib.Path(root_dir) / "data/processed/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
