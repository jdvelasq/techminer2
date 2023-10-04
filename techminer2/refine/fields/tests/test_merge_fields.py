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


def test_merge_fields():
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
        assert test_df["col_c"][0] == "A; a; b"
        assert test_df["col_c"][1] == "B; C; c"
        assert test_df["col_c"][2] == "D; d"
        assert test_df["col_c"][3] == "E"
        assert test_df["col_c"][4] == "F"
        assert test_df["col_c"][5] == "g"
        assert test_df["col_c"][6] == "h"
        assert pd.isna(test_df["col_c"][7])
