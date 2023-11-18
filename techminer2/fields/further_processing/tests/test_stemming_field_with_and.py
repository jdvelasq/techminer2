# pylint: disable=import-outside-toplevel
"""Test rename_field.py"""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_stemming_and():
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
    from techminer2.fields.further_processing import stemming_field_with_and

    stemming_field_with_and(
        items=["CONTROL_SYSTEM"],
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
        assert test_df["col_b"][1] == "SYSTEM_CONTROL"
        assert test_df["col_b"][2] == "CONTROL_SYSTEMS_COMPUTER_APPLICATIONS"
        assert pd.isna(test_df["col_b"][3])
        assert pd.isna(test_df["col_b"][4])
        assert pd.isna(test_df["col_b"][5])
