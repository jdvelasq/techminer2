# pylint: disable=import-outside-toplevel
"""Test merge_fields.py"""


import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_merge_fields():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            [
                {"col_a": "a; b", "col_b": "A"},
                {"col_a": "c", "col_b": "B; C"},
                {"col_a": "d", "col_b": "D"},
                {"col_a": pd.NA, "col_b": "E"},
                {"col_a": "e", "col_b": pd.NA},
                {"col_a": pd.NA, "col_b": pd.NA},
            ]
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.refine.fields import merge_fields

    merge_fields(
        sources=["col_a", "col_b"],
        dest="col_c",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")
        assert "col_c" in test_df.columns
        assert test_df["col_c"][0] == "A; a; b"
        assert test_df["col_c"][1] == "B; C; c"
        assert test_df["col_c"][2] == "D; d"
        assert test_df["col_c"][3] == "E"
        assert test_df["col_c"][4] == "e"
        assert pd.isna(test_df["col_c"][5])
