# pylint: disable=import-outside-toplevel
"""Test authors_importer.py with info from Scopus downloaded in 2023-10-05."""

import os

import numpy as np
import pandas as pd

DATABASE_FILES = [
    "tmp/databases/_cited_by.csv.zip",
    "tmp/databases/_main.csv.zip",
    "tmp/databases/_references.csv.zip",
]


def test_authors_importer():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "raw_authors": [
                    "Chang V.; Chen Y.; (Justin) Zhang Z.; Xu Q.A.; Baudier P.; Liu B.S.C.",
                    "Guo Y., (1); Klink A., (2); Bartolo P., (1); Guo W.G.",
                    "Huang (黃新棫) X.-Y.; Chen (陳怡妏) Y.-W.; Yang (楊鏡堂) J.-T.",
                    "ALSHAREEF M.; Chang, V.-T.",
                    "[No author name available]",
                    "Anonymous",
                    "Anon",
                    pd.NA,
                    np.nan,
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.ingest.field_importers.authors_importer import run_authors_importer

    run_authors_importer(root_dir="tmp/")

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "authors" in test_df.columns
        assert (
            test_df.loc[0, "authors"]
            == "Chang V.; Chen Y.; (Justin) Zhang Z.; Xu Q.A.; Baudier P.; Liu B.S.C."
        )
        assert test_df.loc[1, "authors"] == "Guo Y.; Klink A.; Bartolo P.; Guo W.G."
        assert test_df.loc[2, "authors"] == "Huang (黃新棫) X.-Y.; Chen (陳怡妏) Y.-W.; Yang (楊鏡堂) J.-T."
        assert test_df.loc[3, "authors"] == "Alshareef M.; Chang, V.-T."
        assert pd.isna(test_df.loc[4, "authors"])
        assert pd.isna(test_df.loc[5, "authors"])
        assert pd.isna(test_df.loc[6, "authors"])
        assert pd.isna(test_df.loc[7, "authors"])
        assert pd.isna(test_df.loc[8, "authors"])
