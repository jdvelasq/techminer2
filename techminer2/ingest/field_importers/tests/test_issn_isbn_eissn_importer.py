# pylint: disable=import-outside-toplevel
"""Test importers with info from Scopus downloaded in 2023-10-05."""

import os

import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_isbn_importer():
    """Test."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "isbn": [
                    "008045108x; 978-008045108-4",
                    "0780357728",
                    "979-888697185-9; 979-888697052-4",
                    pd.NA,
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.ingest.field_importers.issb_isbn_eissn_importer import (
        run_issb_isbn_eissn_importer,
    )

    run_issb_isbn_eissn_importer(root_dir="tmp/")

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip", dtype={"issn": str})

        assert "isbn" in test_df.columns

        assert test_df.loc[0, "isbn"] == "008045108x; 978-008045108-4"
        assert test_df.loc[1, "isbn"] == "0780357728"
        assert test_df.loc[2, "isbn"] == "979-888697185-9; 979-888697052-4"
        assert pd.isna(test_df.loc[3, "isbn"])


def test_issn_importer():
    """Test."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "issn": [
                    "00010782",
                    pd.NA,
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.ingest.field_importers.issb_isbn_eissn_importer import (
        run_issb_isbn_eissn_importer,
    )

    run_issb_isbn_eissn_importer(root_dir="tmp/")

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip", dtype={"issn": str})

        assert "issn" in test_df.columns

        assert test_df.loc[0, "issn"] == "00010782"
        assert pd.isna(test_df.loc[1, "issn"])
