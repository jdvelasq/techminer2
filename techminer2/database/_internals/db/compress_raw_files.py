# flake8: noqa
"""Compress all CSV files in the root_dir/raw_data/ subdirectories."""
import os
import sys

import pandas as pd  # type: ignore

from techminer2.database._internals.db.get_subdirectories import (
    internal__get_subdirectories,
)


def internal__compress_raw_files(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO: Compressing raw data files.\n")
    sys.stderr.flush()

    raw_dir = os.path.join(root_dir, "data/raw/")
    folders = internal__get_subdirectories(raw_dir)
    for folder in folders:
        csv_files = os.listdir(os.path.join(raw_dir, folder))
        csv_files = [f for f in csv_files if f.endswith(".csv")]
        for csv_file in csv_files:
            csv_file_path = os.path.join(raw_dir, folder, csv_file)
            zip_file_path = os.path.join(raw_dir, folder, csv_file + ".zip")
            df = pd.read_csv(csv_file_path, encoding="utf-8", low_memory=False)
            df.to_csv(zip_file_path, encoding="utf-8", index=False, compression="zip")
            os.remove(csv_file_path)


#
