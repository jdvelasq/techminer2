"""Fixtures for tests"""

import os

import pandas as pd
import pytest

from ..constansts import DATABASE_NAMES_TO_FILE_NAMES, TEST_DIR

DATABASE_NAME = "main"


@pytest.fixture
def example_df():
    """Example dataframe."""

    file_name = DATABASE_NAMES_TO_FILE_NAMES[DATABASE_NAME]
    file = os.path.join(TEST_DIR, "databases", file_name)
    pdf = pd.DataFrame(
        {
            "authors": [
                "Doe J.; Smith J.",
                "Doe J.",
                "Parker P.",
                "Stark T.",
                None,
            ],
            "year": [2010, 2010, 2011, 2012, 2012],
        }
    )
    pdf.to_csv(file, index=False, compression="zip")
    return pdf
