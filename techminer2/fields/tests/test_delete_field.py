# pylint: disable=import-outside-toplevel
"""Test delete_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_delete_field():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "col_a": ["a", "b", "c"],
                "col_b": ["a", "b", "c"],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.fields import delete_field

    delete_field(
        field="col_b",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")
        assert "col_b" not in test_df.columns
