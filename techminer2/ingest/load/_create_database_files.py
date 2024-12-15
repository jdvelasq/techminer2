"""Create database files."""

# Create databse files by:
# 1. Concatenating raw ZIP files in the specified directory
# 2. Saving the concatenated file in the database directory
# 3. Creating a _DO_NOT_TOUCH_.txt file in the database directory

import os

import pandas as pd  # type: ignore

from ._get_subdirectories import get_subdirectories
from ._message import message


def create_database_files(root_dir):
    """Creates a database *.csv.zip files, one for each directory in raw-data/."""

    message("Creating database files")

    raw_dir = os.path.join(root_dir, "raw-data")
    processed_dir = os.path.join(root_dir, "databases")

    folders = get_subdirectories(raw_dir)
    for folder in folders:
        data = concat_zip_files_in_raw_data_subdirectories(
            os.path.join(raw_dir, folder)
        )
        #
        if len(data) < 500:
            os.environ["TQDM_DISABLE"] = "True"
        else:
            os.environ["TQDM_DISABLE"] = "False"
        #
        file_name = f"_{folder}.csv.zip"
        file_path = os.path.join(processed_dir, file_name)
        data.to_csv(
            file_path, sep=",", encoding="utf-8", index=False, compression="zip"
        )

    file_path = os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt")
    with open(file_path, "w", encoding="utf-8"):
        pass


def concat_zip_files_in_raw_data_subdirectories(path):
    """Concatenate raw ZIP files in the specified directory"""

    files = get_zip_files(path)
    if not files:
        raise FileNotFoundError(f"No ZIP files found in {path}")

    message(f"Concatenating raw files in {path}/")
    data = []
    for file_name in files:
        file_path = os.path.join(path, file_name)
        data.append(pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip"))

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()
    data = data.reset_index(drop=True)

    return data


def get_zip_files(directory):
    """
    Get a list of ZIP files in a directory.

    Args:
        directory (str): The directory to get the CSV files from.

    Returns:
        A list of ZIP files.

    :meta private:
    """
    csv_files = os.listdir(directory)
    csv_files = [f for f in csv_files if f.endswith(".zip")]
    return csv_files
