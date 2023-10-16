# pylint: disable=import-outside-toplevel
"""Test Query class."""

from ..constansts import TEST_DIR
from ..query import Query


def test_query(example_df):
    """Test query."""

    result_df = Query(
        #
        # DATABASE PARAMS
        root_dir=TEST_DIR,
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    ).execute("SELECT * FROM database")

    assert "authors" in result_df.columns
    assert "year" in result_df.columns
    assert len(result_df) == len(example_df)
    assert result_df["year"].to_list() == example_df["year"].to_list()
    assert result_df["authors"].to_list() == example_df["authors"].to_list()
