# flake8: noqa
"""Compress all CSV files in the root_dir/raw_data/ subdirectories."""

import os
import sys

import pandas as pd  # type: ignore
from langdetect import detect  # type: ignore

from .get_subdirectories import internal__get_subdirectories


def internal__remove_non_english_abstracts(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO  Removing non-english abstracts\n")
    sys.stderr.flush()

    raw_dir = os.path.join(root_dir, "raw-data")
    folders = internal__get_subdirectories(raw_dir)
    for folder in folders:
        csv_files = os.listdir(os.path.join(raw_dir, folder))
        csv_files = [f for f in csv_files if f.endswith(".csv")]
        for csv_file in csv_files:
            csv_file_path = os.path.join(raw_dir, folder, csv_file)
            df = pd.read_csv(csv_file_path, encoding="utf-8", low_memory=False)
            n_records_before = len(df)
            df["abs_lang"] = df["Abstract"].map(lambda x: detect(x), na_action="ignore")
            df = df[df["abs_lang"] == "en"]
            df = df.drop(columns=["abs_lang"])
            n_records_after = len(df)
            if n_records_before != n_records_after:
                sys.stderr.write(
                    f"  The file {csv_file} has {n_records_before - n_records_after} non-English abstracts.\n"
                )
                sys.stderr.flush()
            df.to_csv(csv_file_path, encoding="utf-8", index=False)
