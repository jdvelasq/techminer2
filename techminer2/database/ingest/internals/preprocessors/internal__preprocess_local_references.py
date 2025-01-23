# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""

# >>> from techminer2.ingest._homogenize_global_references import homogenize_global_references
# >>> homogenize_global_references(
# ...     root_dir="example/", 
# ... )
# -- 001 -- Homogenizing global references
#      ---> 1093 global references homogenized
# --INFO-- The example/global_references.txt thesaurus file was applied to global_references in 'main' database

"""
import pathlib

import pandas as pd  # type: ignore

from ...message import message


def internal__preprocess_local_references(root_dir):
    """:meta private:"""

    message("Homogenizing local references")

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    main_records_id = dataframe[dataframe.db_main].record_id.to_list()

    dataframe["local_references"] = pd.NA
    dataframe["local_references"] = dataframe["global_references"]

    # dataframe.loc[dataframe.db_main, "local_references"] = dataframe.loc[
    #     dataframe.db_main, "global_references"
    # ]
    dataframe["local_references"] = dataframe["local_references"].str.split("; ")
    dataframe["local_references"] = dataframe["local_references"].map(
        lambda x: [y for y in x if y in main_records_id], na_action="ignore"
    )
    dataframe["local_references"] = dataframe["local_references"].map(
        lambda x: pd.NA if len(x) == 0 else x, na_action="ignore"
    )
    dataframe["local_references"] = dataframe["local_references"].str.join("; ")

    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
