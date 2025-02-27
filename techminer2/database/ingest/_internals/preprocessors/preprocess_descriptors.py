# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import os
import pathlib
import sys

import pandas as pd  # type: ignore

from ....._internals.log_message import internal__log_message
from ..operators.copy_field import internal__copy_field


def internal__preprocess_descriptors(root_dir):

    sys.stdout.write("\nINFO  Processing 'descriptors' column.")
    sys.stdout.flush()
    internal__copy_field(
        source="raw_descriptors",
        dest="descriptors",
        root_dir=root_dir,
    )

    raw_descriptors = extract_raw_decriptors(root_dir)
    write_thesaurus_file(root_dir=root_dir, raw_descriptors=raw_descriptors)


def extract_raw_decriptors(root_dir):

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    return (
        dataframe["raw_descriptors"]
        .dropna()
        .str.split("; ", expand=False)
        .explode()
        .str.strip()
        .drop_duplicates()
        .sort_values()
        .to_list()
    )


def write_thesaurus_file(root_dir, raw_descriptors):
    """Write the thesaurus file with the given descriptors."""

    thesaurus_file = os.path.join(root_dir, "thesaurus/descriptors.the.txt")

    with open(thesaurus_file, "w", encoding="utf-8") as f:
        for word in raw_descriptors:
            f.write(word + "\n")
            f.write("    " + word + "\n")
