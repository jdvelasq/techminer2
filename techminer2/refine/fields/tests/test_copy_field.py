# pylint: disable=import-outside-toplevel
"""Test copy_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_copy_field():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "col_a": ["a", "b", "c"],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.refine.fields import copy_field

    copy_field(
        source="col_a",
        dest="col_b",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "col_b" in test_df.columns
        assert test_df["col_a"].equals(test_df["col_b"])
