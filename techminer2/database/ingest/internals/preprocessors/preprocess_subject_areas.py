# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import os.path  # type: ignore
import pathlib

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from .....internals.log_info_message import log_info_message
from .....package_data.database.load_subject_areas import internal__load_subject_areas


def internal__preprocess_subject_areas(
    #
    # DATABASE PARAMS:
    root_dir="./",
):

    log_info_message("Assign subject_areas to each record")

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    subject_areas_df = internal__load_subject_areas()
    subject_areas_by_issn_mapping = build_subject_areas_by_issn_mapping(
        subject_areas_df
    )
    subject_areas_by_eissn_mapping = build_subject_areas_by_eissn_mapping(
        subject_areas_df
    )

    dataframe["subject_areas"] = None
    for i_row, row in dataframe.iterrows():
        if not pd.isna(row.issn):
            if row.issn in subject_areas_by_issn_mapping:
                dataframe.loc[i_row, "subject_areas"] = subject_areas_by_issn_mapping[
                    row.issn
                ]
            else:
                if row.issn in subject_areas_by_eissn_mapping:
                    dataframe.loc[i_row, "subject_areas"] = (
                        subject_areas_by_eissn_mapping[row.issn]
                    )

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def build_subject_areas_by_issn_mapping(subject_areas_df):
    subject_areas_df = subject_areas_df.copy()
    subject_areas_df = subject_areas_df[["issn", "subject_areas"]]
    subject_areas_df = subject_areas_df.dropna()
    mapping = dict(zip(subject_areas_df.issn, subject_areas_df.subject_areas))
    return mapping


def build_subject_areas_by_eissn_mapping(subject_areas_df):
    subject_areas_df = subject_areas_df.copy()
    subject_areas_df = subject_areas_df[["eissn", "subject_areas"]]
    subject_areas_df = subject_areas_df.dropna()
    mapping = dict(zip(subject_areas_df.eissn, subject_areas_df.subject_areas))
    return mapping
