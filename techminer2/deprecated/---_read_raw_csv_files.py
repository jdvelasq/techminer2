"""Read a bunch of csv files in a directory"""

import os
import os.path

import pandas as pd


def read_raw_csv_files(directory):
    """Load raw csv files in a directory."""

    files = [f for f in os.listdir(directory) if f.endswith(".csv")]
    if len(files) == 0:
        raise FileNotFoundError(f"No CSV files found in {directory}")

    data = []
    for file_name in files:
        data.append(
            pd.read_csv(
                os.path.join(directory, file_name),
                encoding="utf-8",
                error_bad_lines=False,
                warn_bad_lines=True,
            )
        )

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()

    logging.info(f"{data.shape[0]} raw records found in {directory}.")
    return data
