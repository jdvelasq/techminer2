"""Compress all CSV files in the root_dir/raw_data/ subdirectories."""

import os

import pandas as pd  # type: ignore

from ._get_subdirectories import get_subdirectories
from ._message import message


def compress_csv_files_in_raw_data_subdirectories(root_dir):
    """Converts the original data files downloaded from Scopus to *.csv.zip files.

    All the functions of the package operate with *.csv.zip files.
    """

    message("Compressing raw data files")
    raw_dir = os.path.join(root_dir, "raw-data")
    folders = get_subdirectories(raw_dir)
    for folder in folders:
        csv_files = os.listdir(os.path.join(raw_dir, folder))
        csv_files = [f for f in csv_files if f.endswith(".csv")]
        for csv_file in csv_files:
            csv_file_path = os.path.join(raw_dir, folder, csv_file)
            zip_file_path = os.path.join(raw_dir, folder, csv_file + ".zip")
            df = pd.read_csv(csv_file_path, encoding="utf-8")
            df.to_csv(zip_file_path, encoding="utf-8", index=False, compression="zip")
            os.remove(csv_file_path)
