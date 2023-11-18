# pylint: disable=import-outside-toplevel
"""Test rename_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_rename_field():
    """Test rename_field."""

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
    from techminer2.fields import rename_field

    rename_field(
        source="col_a",
        dest="col_b",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "col_a" not in test_df.columns
        assert "col_b" in test_df.columns
