# pylint: disable=import-outside-toplevel
"""Test rename_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_extract_my_keywords():
    """Test rename_field."""

    # Test data:
    if not os.path.exists("tmp/my_keywords"):
        os.makedirs("tmp/my_keywords")
    with open("tmp/my_keywords/my_keywords.txt", "w", encoding="utf-8") as out_fp:
        out_fp.write("aaa\n")
        out_fp.write("bbb\n")

    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "col_a": ["aaa; bbb", "bbb; ccc", "ccc", pd.NA],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.refine.fields import extract_my_keywords

    extract_my_keywords(
        source="col_a",
        dest="col_b",
        file_name="my_keywords.txt",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "col_b" in test_df.columns
        assert test_df["col_b"][0] == "aaa; bbb"
        assert test_df["col_b"][1] == "bbb"
        assert pd.isna(test_df["col_b"][2])
        assert pd.isna(test_df["col_b"][3])
