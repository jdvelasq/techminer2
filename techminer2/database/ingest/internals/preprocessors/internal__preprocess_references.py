# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace journal name in references. """

import pathlib

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ....._dtypes import DTYPES
from ...message import message


def _get_sources_info(root_dir):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    database = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        dtype=DTYPES,
    )
    sources_info = database[["source", "abbr_source_title"]]
    sources_info = sources_info.dropna()
    sources_info = sources_info.drop_duplicates()
    sources_info = sources_info.reset_index(drop=True)

    return sources_info


def internal__preprocess_references(root_dir):
    """Replace journal name in references."""

    message("Replacing journal name in references")

    abbrs = _get_sources_info(root_dir)

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        dtype=DTYPES,
    )

    for source, abbr_source_title in tqdm(
        zip(abbrs.source, abbrs.abbr_source_title), total=len(abbrs)
    ):

        dataframe["raw_global_references"] = dataframe[
            "raw_global_references"
        ].str.replace(source, abbr_source_title, regex=False)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
