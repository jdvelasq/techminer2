# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import os
import pathlib

import pandas as pd  # type: ignore

from .....prepare.thesaurus.descriptors.apply_thesaurus import (
    apply_thesaurus as apply_descriptors_thesaurus,
)


def generate_descriptors_list(dataframe):
    """Generate a sorted list of unique descriptors from the dataframe."""

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


def write_thesaurus_file(descriptors, thesaurus_file):
    """Write the thesaurus file with the given descriptors."""

    with open(thesaurus_file, "w", encoding="utf-8") as f:
        for word in descriptors:
            f.write(word + "\n")
            f.write("    " + word + "\n")


def preprocessing__descriptors(root_dir):

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    descriptors = generate_descriptors_list(dataframe)

    thesaurus_file = os.path.join(root_dir, "thesauri/descriptors.the.txt")
    write_thesaurus_file(descriptors, thesaurus_file)

    apply_descriptors_thesaurus(root_dir)
