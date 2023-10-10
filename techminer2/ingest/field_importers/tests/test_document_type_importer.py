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


def test_document_type_importer():
    """Test copy_field."""

    # Test data:
    if not os.path.exists("tmp/databases"):
        os.makedirs("tmp/databases")

    for file in DATABASE_FILES:
        pd.DataFrame(
            {
                "raw_document_type": [
                    "Article",
                    "Book",
                    "Book chapter",
                    "Conference paper",
                    "Conference review",
                    "Data paper",
                    "Editorial",
                    "Erratum",
                    "Letter",
                    "Note",
                    "Retracted",
                    "Review",
                    "Short survey",
                ],
            }
        ).to_csv(file, index=False, compression="zip")

    # Run:
    from techminer2.ingest.field_importers.document_type_importer import run_document_type_importer

    run_document_type_importer(root_dir="tmp/")

    # Check:
    for file in DATABASE_FILES:
        test_df = pd.read_csv(file, compression="zip")

        assert "document_type" in test_df.columns

        assert test_df.loc[0, "document_type"] == "Article"
        assert test_df.loc[1, "document_type"] == "Book"
        assert test_df.loc[2, "document_type"] == "Book chapter"
        assert test_df.loc[3, "document_type"] == "Conference paper"
        assert test_df.loc[4, "document_type"] == "Conference review"
        assert test_df.loc[5, "document_type"] == "Data paper"
        assert test_df.loc[6, "document_type"] == "Editorial"
        assert test_df.loc[7, "document_type"] == "Erratum"
        assert test_df.loc[8, "document_type"] == "Letter"
        assert test_df.loc[9, "document_type"] == "Note"
        assert test_df.loc[10, "document_type"] == "Retracted"
        assert test_df.loc[11, "document_type"] == "Review"
        assert test_df.loc[12, "document_type"] == "Short survey"
