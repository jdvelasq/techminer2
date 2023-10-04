# pylint: disable=import-outside-toplevel
"""Test process_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_process_field():
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
    from techminer2.refine.fields import process_field

    process_field(
        field="col_a",
        process_func=lambda x: x.str.upper(),
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert test_df["col_a"].to_list() == ["A", "B", "C"]
