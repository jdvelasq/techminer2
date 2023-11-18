# pylint: disable=import-outside-toplevel
"""Test test_count_terms_per_record.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_count_terms_per_record():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "col_a": ["aaa; bbb", "ccc", pd.NA],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.fields.further_processing import count_terms_per_record

    count_terms_per_record(
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
        assert test_df["col_b"].to_list() == [2, 1, 0]
