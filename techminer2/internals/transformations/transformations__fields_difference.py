# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES
from ...prepare.operations.merge_database_fields import merge_database_fields


def transformations__fields_difference(
    compare_field,
    to_field,
    output_field,
    #
    # DATABASE PARAMS:
    root_dir,
):
    #
    # Merge the two fields
    merge_database_fields(
        sources=[compare_field, to_field],
        dest=output_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

    #
    # Computes the intersection per database
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)

        #
        # Compute terms in both columns
        first_terms = (
            data[compare_field]
            .dropna()
            .str.split("; ")
            .explode()
            .str.strip()
            .drop_duplicates()
            .tolist()
        )

        second_terms = (
            data[to_field]
            .dropna()
            .str.split("; ")
            .explode()
            .str.strip()
            .drop_duplicates()
            .tolist()
        )

        common_terms = list(set(first_terms).difference(set(second_terms)))

        #
        # Update columns
        data[output_field] = (
            data[output_field]
            .str.split("; ")
            .map(lambda x: [z for z in x if z in common_terms], na_action="ignore")
        )
        data[output_field] = data[output_field].map(
            lambda x: "; ".join(x) if isinstance(x, list) else x, na_action="ignore"
        )

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
