# pylint: disable=import-outside-toplevel
"""Test fields_difference.py"""


import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_fields_intersection():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            [
                {"col_a": "bbb; aaa; ggg", "col_b": "www; xxx"},
                {"col_a": "aaa", "col_b": "bbb; www"},
                {"col_a": "ggg", "col_b": "aaa"},
                {"col_a": pd.NA, "col_b": "zzz"},
                {"col_a": pd.NA, "col_b": "aaa"},
            ]
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.fields.further_processing import fields_intersection

    fields_intersection(
        compare_field="col_a",
        to_field="col_b",
        output_field="col_c",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")
        assert "col_c" in test_df.columns
        assert test_df["col_c"][0] == "aaa; bbb"
        assert test_df["col_c"][1] == "aaa; bbb"
        assert test_df["col_c"][2] == "aaa"
        assert pd.isna(test_df["col_c"][3])
        assert test_df["col_c"][4] == "aaa"
