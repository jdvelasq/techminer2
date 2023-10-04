# pylint: disable=import-outside-toplevel
"""Test merge_fields.py"""


import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]

DATA = """col_a,col_b
a; b,A
c,B; C
d,D
,E
F,
g,
h,
,
"""


def merge_fields_test():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        with open(file[:-4], "wt", encoding="utf-8") as out_fp:
            out_fp.write(DATA)
        pd.read_csv(file[:-4]).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.refine.fields import merge_fields

    merge_fields(
        fields_to_merge=["col_a", "col_b"],
        dst_field="col_c",
        #
        # DATABASE PARAMS:
        root_dir="tmp/",
    )

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")
        assert "col_c" in test_df.columns
        assert test_df["col_c"].tolist()[:7] == [
            "A; a; b",
            "B; C; c",
            "D; d",
            "E",
            "F",
            "g",
            "h",
        ]
        assert pd.isna(test_df["col_c"].tolist()[7])
