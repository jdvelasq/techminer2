# pylint: disable=import-outside-toplevel
"""Test authors_id_importer.py with info from Scopus downloaded in 2023-10-05."""

import os

import numpy as np
import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_authors_id_importer():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "raw_authors_id": [
                    "1",
                    "10040007900; 56255739500; 48361045500; 6506221360",
                    pd.NA,
                    np.nan,
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.ingest.field_importers.authors_id_importer import run_authors_id_importer

    run_authors_id_importer(root_dir="tmp/")

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "authors_id" in test_df.columns
        assert pd.isna(test_df.loc[0, "authors_id"])
        assert test_df.loc[1, "authors_id"] == "10040007900; 56255739500; 48361045500; 6506221360"
