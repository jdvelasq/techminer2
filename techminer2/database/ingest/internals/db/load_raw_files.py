# flake8: noqa
"""Create database files."""

# Create databse files by:
# 1. Concatenating raw ZIP files in the specified directory
# 2. Saving the concatenated file in the database directory
# 3. Creating a _DO_NOT_TOUCH_.txt file in the database directory

import os
import pathlib

import pandas as pd  # type: ignore

from .....internals.log_message import internal__log_message
from .get_subdirectories import internal__get_subdirectories


def list_zip_filenames_in_raw_data(root_dir):
    """:meta private:"""

    raw_dir = os.path.join(root_dir, "raw-data")
    folders = internal__get_subdirectories(raw_dir)
    files = []

    for folder in folders:
        filenames = os.listdir(os.path.join(raw_dir, folder))
        filenames = [
            (folder, os.path.join(raw_dir, folder, f))
            for f in filenames
            if f.endswith(".zip")
        ]
        files.extend(filenames)
    return files


def add_db_source_columns(dataframe, links):
    """:meta private:"""

    dataframe["db_main"] = False
    dataframe["db_cited_by"] = False
    dataframe["db_references"] = False

    for folder, link in links.items():
        selected = dataframe.Link.isin(link)
        dataframe.loc[selected, "db_" + folder] = True

    return dataframe


def custom_agg(series):
    return series.dropna().iloc[0] if not series.dropna().empty else pd.NA


def read_and_concatenate_files(files):
    """:meta private:"""

    data = []
    links = {}

    for folder, file_name in files:
        dataframe = pd.read_csv(file_name, encoding="utf-8", on_bad_lines="skip")
        data.append(dataframe)
        links[folder] = dataframe.Link.to_list()

    concatenated_data = pd.concat(data, ignore_index=True)
    concatenated_data = concatenated_data.groupby("Link").agg(custom_agg).reset_index()
    # concatenated_data = concatenated_data.drop_duplicates(subset=["Link"])
    # concatenated_data = concatenated_data.reset_index(drop=True)
    concatenated_data = add_db_source_columns(concatenated_data, links)
    return concatenated_data


def internal__load_raw_files(root_dir):
    """:meta private:"""

    internal__log_message(
        msgs="Creating database file.",
        counter_flag=True,
    )

    files = list_zip_filenames_in_raw_data(root_dir)
    dataframe = read_and_concatenate_files(files)

    os.environ["TQDM_DISABLE"] = "True" if len(dataframe) < 500 else "False"

    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
