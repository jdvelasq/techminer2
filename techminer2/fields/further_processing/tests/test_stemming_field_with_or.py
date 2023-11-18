# pylint: disable=import-outside-toplevel
"""Test test_stemming_or.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_stemming_or():
    """Test rename_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")
    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "col_a": [
                    "COMPUTER_CONTROL_SYSTEMS; CONTROL_SYSTEMS_COMPUTER_APPLICATIONS",
                    "SYSTEM_CONTROL; STEREO_VISION",
                    "CONTROL_SYSTEMS_COMPUTER_APPLICATIONS",
                    "COMPUTER_SOFTWARE",
                    "SOFTWARE_ENGINEERING",
                    pd.NA,
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.fields.further_processing import stemming_field_with_or

    stemming_field_with_or(
        items=["COMPUTER_SOFTWARE"],
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
        assert (
            test_df["col_b"][0]
            == "COMPUTER_CONTROL_SYSTEMS; CONTROL_SYSTEMS_COMPUTER_APPLICATIONS"
        )
        assert pd.isna(test_df["col_b"][1])
        assert test_df["col_b"][2] == "CONTROL_SYSTEMS_COMPUTER_APPLICATIONS"
        assert test_df["col_b"][3] == "COMPUTER_SOFTWARE"
        assert test_df["col_b"][4] == "SOFTWARE_ENGINEERING"
        assert pd.isna(test_df["col_b"][5])
